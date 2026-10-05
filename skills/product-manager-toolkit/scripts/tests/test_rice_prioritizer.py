"""
Tests for rice_prioritizer.py

Run with: pytest skills/product-manager-toolkit/scripts/tests/test_rice_prioritizer.py
"""

import sys
from pathlib import Path
import pytest

# Add parent directory to sys.path to import rice_prioritizer
sys.path.insert(0, str(Path(__file__).parent.parent))

from rice_prioritizer import RICECalculator, format_output, load_features_from_csv, create_sample_csv


class TestRICECalculator:
    """Test cases for RICECalculator class methods."""

    def test_calculate_rice_normal(self):
        calculator = RICECalculator()
        # reach: 1000, impact: 'high' (2.0), confidence: 'high' (1.0), effort: 'm' (5)
        # Score: (1000 * 2.0 * 1.0) / 5 = 400.0
        score = calculator.calculate_rice(1000, 'high', 'high', 'm')
        assert score == 400.0

    def test_calculate_rice_zero_effort(self):
        calculator = RICECalculator()
        # Force effort_score to 0 via mock/override if needed or test mapping defaults
        calculator.effort_map['zero'] = 0
        score = calculator.calculate_rice(1000, 'high', 'high', 'zero')
        assert score == 0

    def test_calculate_rice_fallback_defaults(self):
        calculator = RICECalculator()
        # Unknown impact -> default 1.0, confidence -> default 50/100=0.5, effort -> default 5
        # Score: (500 * 1.0 * 0.5) / 5 = 50.0
        score = calculator.calculate_rice(500, 'unknown_impact', 'unknown_confidence', 'unknown_effort')
        assert score == 50.0

    def test_prioritize_features(self):
        calculator = RICECalculator()
        features = [
            {'name': 'Feature Low', 'reach': 100, 'impact': 'low', 'confidence': 'low', 'effort': 'xl'},
            {'name': 'Feature High', 'reach': 10000, 'impact': 'massive', 'confidence': 'high', 'effort': 'xs'},
        ]
        prioritized = calculator.prioritize_features(features)
        assert len(prioritized) == 2
        assert prioritized[0]['name'] == 'Feature High'
        assert prioritized[0]['rice_score'] > prioritized[1]['rice_score']

    def test_analyze_portfolio_empty(self):
        calculator = RICECalculator()
        assert calculator.analyze_portfolio([]) == {}

    def test_analyze_portfolio(self):
        calculator = RICECalculator()
        features = [
            {'name': 'Quick Win 1', 'impact': 'high', 'effort': 'xs', 'reach': 1000, 'rice_score': 100.0},
            {'name': 'Big Bet 1', 'impact': 'massive', 'effort': 'xl', 'reach': 2000, 'rice_score': 50.0},
        ]
        analysis = calculator.analyze_portfolio(features)
        assert analysis['total_features'] == 2
        assert analysis['total_effort_months'] == 1 + 13
        assert analysis['total_reach'] == 3000
        assert analysis['average_rice'] == 75.0
        assert analysis['quick_wins'] == 1
        assert analysis['big_bets'] == 1

    def test_generate_roadmap(self):
        calculator = RICECalculator()
        features = [
            {'name': 'Feature 1', 'effort': 'l', 'rice_score': 100},  # effort 8
            {'name': 'Feature 2', 'effort': 's', 'rice_score': 90},   # effort 3 -> moves to Q2
        ]
        quarters = calculator.generate_roadmap(features, team_capacity=10)
        assert len(quarters) == 2
        assert quarters[0]['quarter'] == 1
        assert quarters[0]['capacity_used'] == 8
        assert quarters[0]['capacity_available'] == 2
        assert len(quarters[0]['features']) == 1

        assert quarters[1]['quarter'] == 2
        assert quarters[1]['capacity_used'] == 3
        assert quarters[1]['capacity_available'] == 7
        assert len(quarters[1]['features']) == 1


class TestFormatOutput:
    """Test cases for format_output function."""

    def test_format_output_complete(self):
        features = [
            {
                'name': 'Feature A',
                'rice_score': 120.5,
                'reach': 5000,
                'impact': 'high',
                'confidence': 'high',
                'effort': 'm'
            },
            {
                'name': 'Feature B',
                'rice_score': 80.0,
                'reach': 2000,
                'impact': 'medium',
                'confidence': 'medium',
                'effort': 's'
            }
        ]

        analysis = {
            'total_features': 2,
            'total_effort_months': 8,
            'total_reach': 7000,
            'average_rice': 100.25,
            'quick_wins': 1,
            'quick_wins_list': [{'name': 'Feature B', 'rice_score': 80.0}],
            'big_bets': 1,
            'big_bets_list': [{'name': 'Feature A', 'rice_score': 120.5}]
        }

        roadmap = [
            {
                'quarter': 1,
                'capacity_used': 8,
                'capacity_available': 2,
                'features': features
            }
        ]

        output = format_output(features, analysis, roadmap)

        assert "RICE PRIORITIZATION RESULTS" in output
        assert "1. Feature A" in output
        assert "RICE Score: 120.5" in output
        assert "2. Feature B" in output
        assert "Total Features: 2" in output
        assert "Total Effort: 8 person-months" in output
        assert "Total Reach: 7,000 users" in output
        assert "Average RICE Score: 100.25" in output
        assert "Quick Wins: 1 features" in output
        assert "• Feature B (RICE: 80.0)" in output
        assert "Big Bets: 1 features" in output
        assert "• Feature A (RICE: 120.5)" in output
        assert "Q1 - Capacity: 8/10 person-months" in output

    def test_format_output_empty_or_defaults(self):
        features = []
        analysis = {}
        roadmap = []

        output = format_output(features, analysis, roadmap)

        assert "RICE PRIORITIZATION RESULTS" in output
        assert "Total Features: 0" in output
        assert "Total Effort: 0 person-months" in output
        assert "Total Reach: 0 users" in output
        assert "Average RICE Score: 0" in output
        assert "Quick Wins: 0 features" in output
        assert "Big Bets: 0 features" in output
        assert "SUGGESTED ROADMAP" in output

    def test_format_output_unnamed_feature(self):
        features = [
            {
                'rice_score': 50.0,
                'reach': 100,
                'impact': 'low',
                'confidence': 'low',
                'effort': 'xs'
            }
        ]
        analysis = {'quick_wins_list': [{'rice_score': 50.0}]}
        roadmap = [{'quarter': 1, 'capacity_used': 1, 'capacity_available': 9, 'features': features}]

        output = format_output(features, analysis, roadmap)

        assert "1. Unnamed" in output
        assert "• Unnamed (RICE: 50.0)" in output


class TestCSVHelpers:
    """Test CSV helper functions."""

    def test_create_sample_and_load_csv(self, tmp_path):
        sample_csv = tmp_path / "sample.csv"
        create_sample_csv(str(sample_csv))
        assert sample_csv.exists()

        features = load_features_from_csv(str(sample_csv))
        assert len(features) == 10
        assert features[0]['name'] == 'User Dashboard Redesign'
        assert features[0]['reach'] == 5000
        assert features[0]['impact'] == 'high'
        assert features[0]['confidence'] == 'high'
        assert features[0]['effort'] == 'l'

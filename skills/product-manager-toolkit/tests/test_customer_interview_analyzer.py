import sys
from pathlib import Path
import pytest

# Ensure scripts directory is in path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from customer_interview_analyzer import aggregate_interviews, InterviewAnalyzer


def test_aggregate_interviews_empty():
    """Test aggregating an empty list of interviews."""
    result = aggregate_interviews([])
    assert result['total_interviews'] == 0
    assert result['common_pain_points'] == {}
    assert result['common_requests'] == {}
    assert result['jobs_to_be_done'] == []
    assert result['overall_sentiment'] == {'positive': 0, 'negative': 0, 'neutral': 0}
    assert result['top_themes'] == {}
    assert result['metrics_summary'] == []
    assert result['competitors_mentioned'] == {}


def test_aggregate_interviews_single():
    """Test aggregating a single interview."""
    interview = {
        'pain_points': [{'quote': 'The app is slow', 'indicator': 'slow'}],
        'feature_requests': [{'quote': 'Add dark mode', 'type': 'ui_improvement'}],
        'jobs_to_be_done': [{'job': 'When I login, I want to see dashboard'}],
        'sentiment_score': {'label': 'positive'},
        'key_themes': ['performance', 'speed'],
        'metrics_mentioned': ['10 hours'],
        'competitors_mentioned': ['CompetitorA']
    }

    result = aggregate_interviews([interview])
    assert result['total_interviews'] == 1
    assert result['common_pain_points'] == {'slow': ['The app is slow']}
    assert result['common_requests'] == {'ui_improvement': ['Add dark mode']}
    assert result['jobs_to_be_done'] == [{'job': 'When I login, I want to see dashboard'}]
    assert result['overall_sentiment'] == {'positive': 1, 'negative': 0, 'neutral': 0}
    assert result['top_themes'] == {'performance': 1, 'speed': 1}
    assert set(result['metrics_summary']) == {'10 hours'}
    assert result['competitors_mentioned'] == {'CompetitorA': 1}


def test_aggregate_interviews_multiple():
    """Test aggregating multiple interviews with overlapping and distinct data."""
    interview1 = {
        'pain_points': [
            {'quote': 'The export is slow', 'indicator': 'slow'},
            {'quote': 'Confusing UI', 'indicator': 'confus'}
        ],
        'feature_requests': [
            {'quote': 'Need CSV export', 'type': 'new_feature'}
        ],
        'jobs_to_be_done': [{'job': 'Job 1'}],
        'sentiment_score': {'label': 'negative'},
        'key_themes': ['export', 'ui'],
        'metrics_mentioned': ['50%'],
        'competitors_mentioned': ['CompA', 'CompB']
    }

    interview2 = {
        'pain_points': [
            {'quote': 'Search is slow', 'indicator': 'slow'}
        ],
        'feature_requests': [
            {'quote': 'Fix UI bug', 'type': 'ui_improvement'}
        ],
        'jobs_to_be_done': [{'job': 'Job 2'}],
        'sentiment_score': {'label': 'positive'},
        'key_themes': ['export', 'search'],
        'metrics_mentioned': ['100 dollars'],
        'competitors_mentioned': ['CompA']
    }

    result = aggregate_interviews([interview1, interview2])
    assert result['total_interviews'] == 2
    assert len(result['common_pain_points']['slow']) == 2
    assert result['common_pain_points']['confus'] == ['Confusing UI']
    assert result['common_requests']['new_feature'] == ['Need CSV export']
    assert result['common_requests']['ui_improvement'] == ['Fix UI bug']
    assert len(result['jobs_to_be_done']) == 2
    assert result['overall_sentiment'] == {'positive': 1, 'negative': 1, 'neutral': 0}
    assert result['top_themes']['export'] == 2
    assert result['top_themes']['ui'] == 1
    assert result['top_themes']['search'] == 1
    assert set(result['metrics_summary']) == {'50%', '100 dollars'}
    assert result['competitors_mentioned']['CompA'] == 2
    assert result['competitors_mentioned']['CompB'] == 1


def test_aggregate_interviews_missing_or_default_keys():
    """Test aggregating interviews with missing optional keys or missing indicators/types."""
    interview_empty = {}
    interview_partial = {
        'pain_points': [{'quote': 'Some pain'}], # missing indicator
        'feature_requests': [{'quote': 'Some req'}], # missing type
        'sentiment_score': {} # missing label
    }

    result = aggregate_interviews([interview_empty, interview_partial])
    assert result['total_interviews'] == 2
    assert result['common_pain_points'] == {'unknown': ['Some pain']}
    assert result['common_requests'] == {'general': ['Some req']}
    assert result['overall_sentiment']['neutral'] == 2


def test_integration_with_analyzer():
    """Integration test: Analyze raw text with InterviewAnalyzer then aggregate."""
    analyzer = InterviewAnalyzer()
    text1 = "I struggle with the slow dashboard. I need to export data quickly because my goal is to report results. I used CompetitorA instead."
    text2 = "I love the simple layout. It saves 5 hours every week. I wish it had dark mode feature."

    analysis1 = analyzer.analyze_interview(text1)
    analysis2 = analyzer.analyze_interview(text2)

    aggregated = aggregate_interviews([analysis1, analysis2])
    assert aggregated['total_interviews'] == 2
    assert aggregated['overall_sentiment']['neutral'] >= 0
    assert len(aggregated['metrics_summary']) > 0

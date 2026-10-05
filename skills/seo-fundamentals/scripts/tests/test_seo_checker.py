"""
Tests for seo_checker.py

Run with: pytest skills/seo-fundamentals/scripts/tests/test_seo_checker.py -v
"""

import sys
from pathlib import Path
import pytest

# Add scripts directory to path so seo_checker can be imported
sys.path.insert(0, str(Path(__file__).parent.parent))

from seo_checker import is_page_file, find_pages, check_page


class TestIsPageFile:
    """Test suite for is_page_file function."""

    @pytest.mark.parametrize("file_path_str", [
        "src/config.py",
        "src/setup_helper.js",
        "src/util.ts",
        "src/helpers.ts",
        "src/useAuthHook.ts",
        "src/AuthContext.tsx",
        "src/userStore.ts",
        "src/apiService.ts",
        "src/user_api.ts",
        "src/lib.ts",
        "src/constant_values.ts",
        "src/user_type.d.ts",
        "src/user_interface.ts",
        "src/mock_handlers.ts",
        "src/components/Button.test.tsx",
        "src/components/Button.spec.jsx",
        "src/components/Button_test.tsx",
        "src/components/Button_spec.jsx",
        # Skip pattern precedence over page directories/names
        "pages/api.tsx",
        "app/config_page.tsx",
        "routes/helper.jsx",
    ])
    def test_is_page_file_skip_patterns(self, file_path_str):
        """Files matching skip patterns in filename should return False."""
        file_path = Path(file_path_str)
        assert is_page_file(file_path) is False

    @pytest.mark.parametrize("file_path_str", [
        "pages/dashboard.tsx",
        "src/pages/index.jsx",
        "app/profile/settings.tsx",
        "src/routes/login.tsx",
        "src/views/UserView.jsx",
        "src/screens/HomeScreen.tsx",
        # Case insensitive directory matching
        "PAGES/dashboard.tsx",
        "src/APP/main.tsx",
    ])
    def test_is_page_file_page_directories(self, file_path_str):
        """Files within recognized page directories should return True."""
        file_path = Path(file_path_str)
        assert is_page_file(file_path) is True

    @pytest.mark.parametrize("file_path_str", [
        "components/page.tsx",
        "components/index.jsx",
        "src/home_hero.tsx",
        "src/about_us.jsx",
        "src/contact_form.tsx",
        "src/blog_list.tsx",
        "src/post_view.tsx",
        "src/article_detail.tsx",
        "src/product_card.tsx",
        "src/landing_banner.tsx",
        "src/main_layout.tsx",
        # Case insensitivity stem indicators
        "src/ABOUT.jsx",
        "src/LandingHero.tsx",
    ])
    def test_is_page_file_filename_indicators(self, file_path_str):
        """Files with recognized page indicators in stem should return True."""
        file_path = Path(file_path_str)
        assert is_page_file(file_path) is True

    @pytest.mark.parametrize("file_path_str", [
        "custom/mypage.html",
        "public/about.htm",
        "docs/index.HTML",
        "static/contact.HTM",
    ])
    def test_is_page_file_html_extensions(self, file_path_str):
        """HTML and HTM files should return True."""
        file_path = Path(file_path_str)
        assert is_page_file(file_path) is True

    @pytest.mark.parametrize("file_path_str", [
        "components/Card.tsx",
        "src/Header.jsx",
        "styles/main.css",
        "scripts/build.js",
        "data/users.json",
    ])
    def test_is_page_file_non_page_files(self, file_path_str):
        """Files that do not meet any page criteria should return False."""
        file_path = Path(file_path_str)
        assert is_page_file(file_path) is False


class TestFindPages:
    """Test suite for find_pages function."""

    def test_find_pages_filters_and_skips(self, tmp_path):
        """Test find_pages correctly discovers page files and skips excluded directories/patterns."""
        # Setup mock directory structure
        pages_dir = tmp_path / "pages"
        pages_dir.mkdir()
        (pages_dir / "index.jsx").write_text("<title>Home</title>")
        (pages_dir / "about.html").write_text("<title>About</title>")
        (pages_dir / "api.tsx").write_text("export default function handler() {}")

        skip_dir = tmp_path / "node_modules" / "pages"
        skip_dir.mkdir(parents=True)
        (skip_dir / "ignored.jsx").write_text("<title>Ignored</title>")

        found = find_pages(tmp_path)
        found_names = [f.name for f in found]

        assert "index.jsx" in found_names
        assert "about.html" in found_names
        assert "api.tsx" not in found_names
        assert "ignored.jsx" not in found_names


class TestCheckPage:
    """Test suite for check_page function."""

    def test_check_page_no_issues(self, tmp_path):
        """Test check_page on a valid HTML file with all SEO elements."""
        file_path = tmp_path / "valid.html"
        content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Valid Title</title>
            <meta name="description" content="Valid description">
            <meta property="og:title" content="OG Title">
        </head>
        <body>
            <h1>Single H1 Heading</h1>
            <img src="logo.png" alt="Company Logo">
        </body>
        </html>
        """
        file_path.write_text(content, encoding='utf-8')

        result = check_page(file_path)
        assert result["file"] == "valid.html"
        assert result["issues"] == []

    def test_check_page_detects_seo_issues(self, tmp_path):
        """Test check_page detects missing elements and multiple H1 tags."""
        file_path = tmp_path / "layout_with_issues.html"
        content = """
        <html>
        <head>
        </head>
        <body>
            <h1>Heading 1</h1>
            <h1>Heading 2</h1>
            <img src="test1.png">
            <img src="test2.png" alt="">
        </body>
        </html>
        """
        file_path.write_text(content, encoding='utf-8')

        result = check_page(file_path)
        assert result["file"] == "layout_with_issues.html"
        assert "Missing <title> tag" in result["issues"]
        assert "Missing meta description" in result["issues"]
        assert "Missing Open Graph tags" in result["issues"]
        assert "Multiple H1 tags (2)" in result["issues"]
        assert "Image missing alt attribute" in result["issues"] or "Image has empty alt attribute" in result["issues"]

    def test_check_page_file_read_error(self, tmp_path):
        """Test check_page handles file read errors gracefully."""
        non_existent = tmp_path / "non_existent.html"
        result = check_page(non_existent)
        assert result["file"] == "non_existent.html"
        assert len(result["issues"]) == 1
        assert result["issues"][0].startswith("Error:")

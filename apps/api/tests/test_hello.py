"""Hello unit test module."""

from apps.api.api.main import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello api"

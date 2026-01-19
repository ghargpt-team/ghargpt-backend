"""Hello unit test module."""

from mongodb_serve.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello mongodb-serve"

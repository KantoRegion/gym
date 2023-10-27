"""Hello unit test module."""

from rhydon_modal.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello pygym"

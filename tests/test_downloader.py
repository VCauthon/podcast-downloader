
import pytest
from downloader import downloader


def test_downloader_youtube():
    url = "https://www.youtube.com/watch?v=PrVgdrsp-b8"
    result = downloader(url)
    assert isinstance(result, bytes)
    assert len(result) > 0


def test_downloader_spotify():
    url = "https://open.spotify.com/track/7xGfFoTpQ2E7fRF5lN10tr"
    with pytest.raises(ValueError):
        downloader(url)


def test_detect_platform_youtube():
    url = "https://www.youtube.com/watch?v=PrVgdrsp-b8"
    platform = "__youtube"
    result = __interface_ABC.detect_platform(url)
    assert result == platform


def test_detect_platform_unsupported():
    url = "https://example.com/video"
    with pytest.raises(ValueError):
        __interface_ABC.detect_platform(url)

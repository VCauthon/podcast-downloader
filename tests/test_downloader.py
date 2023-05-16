import sys

sys.path.append("../src")
from podcast_downloader.downloader import downloader  # noqa: E402


def test_downloader_youtube():
    url = (
        "https://www.youtube.com/watch?v=52Gg9CqhbP8&list="
        "PLlVaFbgtYyJfgQAoHqDjz5MDmVLwARcWo&index=3"
    )
    result = downloader.downloader(url)
    assert (
        isinstance(result.bytes, bytes) and len(result.bytes) > 0
    ), "The download hasn't been successful"
    assert result.title, "The download hasn't been successful"


# def test_downloader_spotify():
#     url = "https://open.spotify.com/track/7xGfFoTpQ2E7fRF5lN10tr"
#     with pytest.raises(ValueError):
#         downloader(url)


# def test_detect_platform_youtube():
#     url = "https://www.youtube.com/watch?v=PrVgdrsp-b8"
#     platform = "__youtube"
#     result = downloader(url)
#     assert result == platform


# def test_detect_platform_unsupported():
#     url = "https://example.com/video"
#     with pytest.raises(ValueError):
#         downloader(url)

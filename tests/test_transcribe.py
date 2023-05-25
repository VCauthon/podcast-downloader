import pytest

import sys

sys.path.append("../src")
from podcast_downloader.transcribe import Transcribe  # noqa: E402


@pytest.fixture
def transcribe_instance() -> Transcribe:
    return Transcribe("./tests/testing.mp4")


def test_transcribe(transcribe_instance: Transcribe):
    result = transcribe_instance.transcribe()
    assert isinstance(result, str)
    assert len(result) > 0


def test_transcribe_sections(transcribe_instance: Transcribe):
    result = transcribe_instance.transcribe(start_time=10, end_time=20)
    assert isinstance(result, str)
    assert len(result) > 0

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


def test_return_audio(transcribe_instance: Transcribe):
    audio = transcribe_instance.RetrieveAudio.return_audio()
    assert isinstance(audio, bytes)
    assert len(audio) > 0


def test_concrete_sections_of_the_video(transcribe_instance: Transcribe):
    start_time = 10  # Provide a start time in seconds
    end_time = 20  # Provide an end time in seconds
    result = (
        transcribe_instance.RetrieveAudio._Transcribe__concrete_sections_of_the_video(
            start_time, end_time
        )
    )
    assert isinstance(result, str)
    assert len(result) > 0

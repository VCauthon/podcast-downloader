from unittest.mock import Mock

import sys

sys.path.append("../src")
from podcast_downloader.summary import get_summary  # noqa: E402


def test_get_summary(requests_mock):
    # Mock the requests.post method
    mock_response = Mock()
    mock_response.text = "This is a summary"
    requests_mock.post("CHATGPT_API_URL", text=mock_response.text)

    # Call the get_summary function
    summary = get_summary("This is the text to summarize")

    # Assertions
    assert summary == "This is a summary"
    assert requests_mock.called
    assert requests_mock.last_request.json() == {
        "text": "This is the text to summarize"
    }

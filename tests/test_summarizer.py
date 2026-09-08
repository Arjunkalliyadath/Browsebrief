import pytest

from summarizer import summarize, MAX_CHARS


class FakeResponse:
    def __init__(self, content):
        self.content = content


class FakeLLM:
    def invoke(self, prompt):
        return FakeResponse("fake summary")


def test_summarize_returns_llm_content():
    assert summarize("Some short webpage text.", FakeLLM()) == "fake summary"


def test_summarize_empty_input_raises():
    with pytest.raises(ValueError):
        summarize("   ", FakeLLM())


def test_summarize_truncates_long_content():
    long_text = "a" * (MAX_CHARS + 500)
    result = summarize(long_text, FakeLLM())
    assert "truncated" in result

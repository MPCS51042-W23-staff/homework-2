import problem6
import pytest

lines = ["I went to Poland.", "He went to Spain.", "She is very happy."]


def test_example1():
    gen = problem6.grep("went", lines)
    assert list(gen) == [
        "I went to Poland.",
        "He went to Spain.",
    ]

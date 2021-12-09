import pytest

from hugtools.nlp import align_tokens


@pytest.fixture
def tokens_for_align_tokens():
    tokens_a = [
        "This",
        "is",
        "a",
        "sentence",
        "-",
        "like",
        "thingy",
        ",",
        "that",
        "will",
        "need",
        "to",
        "be",
        "broken",
        "up",
        "into",
        "subwords",
    ]
    tokens_b = [
        "This",
        "is",
        "a",
        "sentence",
        "-",
        "like",
        "thing",
        "##y",
        ",",
        "that",
        "will",
        "need",
        "to",
        "be",
        "broken",
        "up",
        "into",
        "sub",
        "##words",
    ]
    return tokens_a, tokens_b


def test_align_tokens_success(tokens_for_align_tokens):
    tokens_a, tokens_b = tokens_for_align_tokens
    align_map = align_tokens(tokens_a, tokens_b)
    assert align_map == {
        0: [0],
        1: [1],
        2: [2],
        3: [3],
        4: [4],
        5: [5],
        6: [6],
        7: [6],
        8: [7],
        9: [8],
        10: [9],
        11: [10],
        12: [11],
        13: [12],
        14: [13],
        15: [14],
        16: [15],
        17: [16],
        18: [16],
    }


def test_align_tokens_too_many_characters(tokens_for_align_tokens):
    tokens_a, tokens_b = tokens_for_align_tokens
    tokens_a += ["more", "characters"]
    with pytest.raises(ValueError):
        align_tokens(tokens_a, tokens_b)


def test_align_tokens_character_mismatch(tokens_for_align_tokens):
    tokens_a, tokens_b = tokens_for_align_tokens
    tokens_b[1] = "as"
    with pytest.raises(RuntimeError):
        align_tokens(tokens_a, tokens_b)

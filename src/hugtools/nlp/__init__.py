from copy import copy
from typing import Dict, List


def align_tokens(tokens_a: List[str], tokens_b: List[str], subword_prefix: str = "##") -> Dict[int, List[int]]:
    """
    Given two different lists of tokens from different tokenizers, we can align the indices to each other

    Example:

    >>> tokens_a = ['This', 'is', 'a', 'sentence', '-', 'like', 'thingy', ',', \
    'that', 'will', 'need', 'to', 'be', 'broken', 'up', 'into', 'subwords']
    >>> tokens_b = ['This', 'is', 'a', 'sentence', '-', 'like', 'thing', '##y', \
    ',', 'that', 'will', 'need', 'to', 'be', 'broken', 'up', 'into', 'sub', '##words']
    >>> align_tokens(tokens_a, tokens_b)
    {0: [0], 1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 6: [6], 7: [6], 8: [7], 9: [8], 10: [9], 11: [10], 12: [11], \
    13: [12], 14: [13], 15: [14], 16: [15], 17: [16], 18: [16]}


    Args:
        tokens_a (list[str]): A list of tokens
        tokens_b (list[str]): A second list of tokens, that should contain the same text as the first, though
                              differently tokenized
        subword_prefix: A prefix if you have subwords, e.g. "##" common for BERT family models (default: "##")

    Returns:
        dict[int, list[int]: A mapping of tokens_a indexes to their corresponding tokens_b token

    """
    token_map: Dict[int, List[int]] = {}

    tokens_a_queue, tokens_b_queue = copy(tokens_a), copy(tokens_b)
    token_a_idx, token_b_idx = 0, 0

    ts1, tn1 = tokens_a_queue.pop(0), tokens_b_queue.pop(0)
    try:
        while True:
            if ts1 == tn1:
                token_map[token_b_idx] = token_map.get(token_b_idx, []) + [token_a_idx]
                token_a_idx += 1
                token_b_idx += 1

                ts1, tn1 = tokens_a_queue.pop(0), tokens_b_queue.pop(0)
                ts1 = ts1[2:] if ts1.startswith(subword_prefix) else ts1
                tn1 = tn1[2:] if tn1.startswith(subword_prefix) else tn1

            elif tn1.startswith(ts1):
                token_map[token_b_idx] = token_map.get(token_b_idx, []) + [token_a_idx]
                token_a_idx += 1
                tn1 = tn1[len(ts1) :]

                ts1 = tokens_a_queue.pop(0)
                ts1 = ts1[2:] if ts1.startswith(subword_prefix) else ts1
            elif ts1.startswith(tn1):
                token_map[token_b_idx] = token_map.get(token_b_idx, []) + [token_a_idx]
                token_b_idx += 1
                ts1 = ts1[len(tn1) :]

                tn1 = tokens_b_queue.pop(0)
                tn1 = tn1[2:] if tn1.startswith(subword_prefix) else tn1
            else:
                raise RuntimeError(f"Something went wrong, {ts1} or {tn1} is not a part of the one of the token lists")
    except IndexError as e:
        if str(e) != "pop from empty list":
            raise e

    if len(tokens_a_queue) + len(tokens_b_queue) != 0:
        raise ValueError("One of the lists of tokens had more characters than the other.")
    return token_map

from typing import List, Union

_BYTE_LOOKUP_TABLE: List[str] = [
    "B",
    "KB",
    "MB",
    "GB",
    "TB",
    "PB",
    "EB",
    "ZB",
    "This is probably enough",
]


def byteconv(original: Union[float, int], target_type: str, original_type: str = "B") -> float:
    """
    Convert some byte -> xbyte, intended to be used for logging mostly, but can be used anywhere of course. Base 2,
    because who uses base 10

    Args:
        original (number): the initial value of the input
        target_type (str): the type we are going to, e.g. `MB`
        original_type (str): where we are coming from, defaults to `B`


    Returns:
        converted number
    """
    original_exp = 0 if original_type == "B" else _BYTE_LOOKUP_TABLE.index(original_type.upper()) * 10
    target_exp = 0 if target_type == "B" else _BYTE_LOOKUP_TABLE.index(target_type.upper()) * 10
    return float(original * 2 ** (original_exp - target_exp))

import os.path

import pytest

from src.hugtools.util import get_if_exception, trimdent


def test_trimdent():
    assert (
        trimdent(
            """
    This is indented by
         4 and then 8
    or something
    """
        )
        == "\nThis is indented by\n     4 and then 8\nor something\n    "
    )


def test_get_if_exception():
    # with pytest.raises()
    assert (
        get_if_exception(os.path.isdir, "By default this will catch everything")
        == "By default this will catch everything"
    )
    assert get_if_exception(os.path.isdir, "Gotta add the argument!", TypeError) == "Gotta add the argument!"
    with pytest.raises(TypeError, match=r"isdir\(\) missing 1 required positional argument: 's'"):
        get_if_exception(os.path.isdir, "Gotta add the argument!", (SyntaxError, OSError))

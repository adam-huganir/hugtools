""" description goes here """

from hugtools import Dummy, __version__


def test_version():
    assert __version__ == "0.1.0a2"


def test_from_json():
    dummy = Dummy.from_json({"my": "value"})
    assert dummy.__dict__ == {"my": "value"}

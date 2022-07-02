from hugtools.misc import byteconv


def test_byteconv():
    assert byteconv(1024, "KB") == 1.0
    assert byteconv(1024, "KB", "KB") == 1024.0
    assert byteconv(1024, "MB", "KB") == 1.0

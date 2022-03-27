from pdmp import __version__

from pdmp.core import add


def test_version():
    assert __version__ == '0.1.0'


def test_add():
    input_1 = 10
    input_2 = 15
    expected = 25
    assert expected == add(input_1, input_2)

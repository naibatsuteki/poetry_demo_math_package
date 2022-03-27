from pdmp import __version__

from pdmp.core import add, substruct


def test_version():
    assert __version__ == '0.1.0'


def test_add():
    input_1 = 10
    input_2 = 15
    expected = 25
    assert expected == add(input_1, input_2)


def test_substract():
    input_1 = 15
    input_2 = 10
    expected = 5
    assert expected == substruct(input_1, input_2)

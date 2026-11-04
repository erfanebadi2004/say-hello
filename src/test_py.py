import pytest
from hello import say_hello


def test_func():
    assert say_hello() == "hello, world!"
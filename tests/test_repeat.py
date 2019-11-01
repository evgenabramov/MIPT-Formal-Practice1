import pytest
import math

from main import (
    State,
    repeat
)


@pytest.fixture(scope="module")
def result1():
    state = State()
    state.can_be_one_symbol_word = True
    state.max_one_symbol_length = math.inf
    state.max_one_symbol_prefix = math.inf
    return state


@pytest.fixture(scope="module")
def result2():
    state = State()
    state.can_be_one_symbol_word = True
    state.max_one_symbol_length = 0
    state.max_one_symbol_prefix = 3
    return state


def test_one_symbol_word(one_symbol_word_state, result1):
    next_state = repeat(one_symbol_word_state)
    assert next_state == result1


def test_one_symbol_zero_length(one_symbol_word_zero_length_state, result2):
    next_state = repeat(one_symbol_word_zero_length_state)
    assert next_state == result2

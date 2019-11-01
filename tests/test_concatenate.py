import pytest

from main import (
    State,
    concatenate
)


@pytest.fixture(scope="module")
def result1():
    state = State()
    state.can_be_one_symbol_word = True
    state.max_one_symbol_length = 2
    state.max_one_symbol_prefix = 3
    return state


@pytest.fixture(scope="module")
def result2():
    state = State()
    state.can_be_one_symbol_word = True
    state.max_one_symbol_length = 2
    state.max_one_symbol_prefix = 6
    return state


@pytest.fixture(scope="module")
def result3():
    state = State()
    state.can_be_one_symbol_word = False
    state.max_one_symbol_length = 0
    state.max_one_symbol_prefix = 5
    return state


def test_one_symbol_word(one_symbol_word_state, result1):
    next_state = concatenate(one_symbol_word_state, one_symbol_word_state)
    assert next_state == result1


def test_one_symbol_word_long_left_prefix(one_symbol_word_state,
                                          one_symbol_word_with_long_prefix_state,
                                          result2):
    next_state = concatenate(one_symbol_word_with_long_prefix_state,
                             one_symbol_word_state)
    assert next_state == result2


def test_not_one_symbol_word(one_symbol_word_state,
                             few_symbols_word_state,
                             result3):
    next_state = concatenate(one_symbol_word_state, few_symbols_word_state)
    assert next_state == result3

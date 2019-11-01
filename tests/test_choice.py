import pytest

from main import (
    State,
    choice
)


@pytest.fixture(scope="module")
def result1():
    state = State()
    state.can_be_one_symbol_word = True
    state.max_one_symbol_length = 1
    state.max_one_symbol_prefix = 4
    return state


def test_both_one_symbol_words(one_symbol_word_state,
                               one_symbol_word_with_long_prefix_state):
    next_state = choice(one_symbol_word_state,
                        one_symbol_word_with_long_prefix_state)
    assert next_state == one_symbol_word_with_long_prefix_state


def test_diffferent_types_words(one_symbol_word_state,
                                few_symbols_word_state,
                                result1):
    next_state = choice(one_symbol_word_state, few_symbols_word_state)
    assert next_state == result1


def test_both_few_symbols_words(few_symbols_word_state,
                                second_few_symbols_word_state):
    next_state = choice(few_symbols_word_state, second_few_symbols_word_state)
    assert next_state == few_symbols_word_state

import pytest

from main import State


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, State) and isinstance(right, State) and op == "==":
        return [
            "Comparing State instances:",
            "   can_be_one_symbol_word: {} != {} or".format(left.can_be_one_symbol_word,
                                                            right.can_be_one_symbol_word),
            "   max_one_symbol_length: {} != {} or".format(left.max_one_symbol_length,
                                                           right.max_one_symbol_length),
            "   max_one_symbol_prefix: {} != {}".format(left.max_one_symbol_prefix,
                                                        right.max_one_symbol_prefix)
        ]


@pytest.fixture(scope="module")
def one_symbol_word_state():
    state = State()
    state.can_be_one_symbol_word = True
    state.max_one_symbol_length = 1
    state.max_one_symbol_prefix = 2
    return state


@pytest.fixture(scope="module")
def one_symbol_word_with_long_prefix_state():
    state = State()
    state.can_be_one_symbol_word = True
    state.max_one_symbol_length = 1
    state.max_one_symbol_prefix = 6
    return state


@pytest.fixture(scope="module")
def one_symbol_word_zero_length_state():
    state = State()
    state.can_be_one_symbol_word = False
    state.max_one_symbol_length = 0
    state.max_one_symbol_prefix = 3
    return state


@pytest.fixture(scope="module")
def few_symbols_word_state():
    state = State()
    state.can_be_one_symbol_word = False
    state.max_one_symbol_length = 0
    state.max_one_symbol_prefix = 4
    return state


@pytest.fixture(scope="module")
def second_few_symbols_word_state():
    state = State()
    state.can_be_one_symbol_word = False
    state.max_one_symbol_length = 0
    state.max_one_symbol_prefix = 2
    return state

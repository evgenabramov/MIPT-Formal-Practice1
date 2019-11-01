import pytest

from main import State


@pytest.fixture(scope="module")
def prefix_symbol_state():
    symbol = 'a'
    return State(symbol, symbol)


@pytest.fixture(scope="module")
def other_symbol_state():
    symbol = 'a'
    prefix_symbol = 'b'
    return State(symbol, prefix_symbol)


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

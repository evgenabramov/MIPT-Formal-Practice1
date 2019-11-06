import pytest

from main import (
    State,
    get_final_state
)


@pytest.fixture(scope="module")
def correct_regex1():
    return "ab+c.aba.*.bac.+.+*"


@pytest.fixture(scope="module")
def final_state1_a():
    state = State()
    state.can_be_one_symbol_word = True
    state.max_one_symbol_length = 0
    state.max_one_symbol_prefix = 2
    return state


@pytest.fixture(scope="module")
def final_state1_b():
    state = State()
    state.can_be_one_symbol_word = True
    state.max_one_symbol_length = 0
    state.max_one_symbol_prefix = 1
    return state


@pytest.fixture(scope="module")
def final_state1_c():
    state = State()
    state.can_be_one_symbol_word = True
    state.max_one_symbol_length = 0
    state.max_one_symbol_prefix = 0
    return state


@pytest.fixture(scope="module")
def correct_regex2():
    return "acb..bab.c.*.ab.ba.+.+*a."


@pytest.fixture(scope="module")
def final_state2_a():
    state = State()
    state.can_be_one_symbol_word = True
    state.max_one_symbol_length = 1
    state.max_one_symbol_prefix = 1
    return state


@pytest.fixture(scope="module")
def final_state2_b():
    state = State()
    state.can_be_one_symbol_word = False
    state.max_one_symbol_length = 0
    state.max_one_symbol_prefix = 2
    return state


@pytest.fixture(scope="module")
def final_state2_c():
    state = State()
    state.can_be_one_symbol_word = False
    state.max_one_symbol_length = 0
    state.max_one_symbol_prefix = 0
    return state


@pytest.fixture(scope="module")
def incorrect_regex_unknown_symbol():
    return "ab.c+ed.+*"


@pytest.fixture(scope="module")
def incorrect_regex_bad_notation():
    return "ab.+c"


@pytest.fixture(scope="module")
def incorrect_regex_stack_not_empty():
    return "ab.c*"


def test_correct_regex1(correct_regex1, final_state1_a, final_state1_b,
                        final_state1_c):
    final_state_a = get_final_state(correct_regex1, 'a')
    final_state_b = get_final_state(correct_regex1, 'b')
    final_state_c = get_final_state(correct_regex1, 'c')
    assert final_state_a == final_state1_a
    assert final_state_b == final_state1_b
    assert final_state_c == final_state1_c


def test_correct_regex2(correct_regex2, final_state2_a, final_state2_b,
                        final_state2_c):
    final_state_a = get_final_state(correct_regex2, 'a')
    final_state_b = get_final_state(correct_regex2, 'b')
    final_state_c = get_final_state(correct_regex2, 'c')
    assert final_state_a == final_state2_a
    assert final_state_b == final_state2_b
    assert final_state_c == final_state2_c


def test_unknown_symbol(incorrect_regex_unknown_symbol):
    with pytest.raises(Exception) as excinfo:
        get_final_state(incorrect_regex_unknown_symbol, 'a')
    assert "unexpected symbol" in str(excinfo.value)


def test_bad_notation(incorrect_regex_bad_notation):
    with pytest.raises(Exception) as excinfo:
        get_final_state(incorrect_regex_bad_notation, 'a')
    assert "inconsistent regular expression" in str(excinfo.value)


def test_stack_not_empty(incorrect_regex_stack_not_empty):
    with pytest.raises(Exception) as excinfo:
        get_final_state(incorrect_regex_stack_not_empty, 'a')
    assert "inconsistent regular expression" in str(excinfo.value)

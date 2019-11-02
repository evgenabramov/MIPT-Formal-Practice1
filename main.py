#!usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import math

alphabet = {'a', 'b', 'c', '1'}
operations = {'.', '+', '*'}


class State:
    def __init__(self, letter=None, prefix_symbol=None):
        if letter == prefix_symbol:
            # Независимые величины (могут соответствовать разным словам)
            self.can_be_one_symbol_word = True
            self.max_one_symbol_prefix = 1
            self.max_one_symbol_length = 1
        else:
            self.can_be_one_symbol_word = False
            self.max_one_symbol_prefix = 0
            self.max_one_symbol_length = 0

    def __eq__(self, other):
        if isinstance(other, State):
            return self.can_be_one_symbol_word == other.can_be_one_symbol_word and \
                self.max_one_symbol_length == other.max_one_symbol_length and \
                self.max_one_symbol_prefix == other.max_one_symbol_prefix
        return False


def concatenate(left_state, right_state):
    next_state = State()
    next_state.can_be_one_symbol_word = left_state.can_be_one_symbol_word and right_state.can_be_one_symbol_word

    if next_state.can_be_one_symbol_word:
        next_state.max_one_symbol_length = left_state.max_one_symbol_length + \
            right_state.max_one_symbol_length
    else:
        next_state.max_one_symbol_length = 0

    if left_state.can_be_one_symbol_word:
        next_state.max_one_symbol_prefix = max(
            left_state.max_one_symbol_length + right_state.max_one_symbol_prefix, left_state.max_one_symbol_prefix)
    else:
        next_state.max_one_symbol_prefix = left_state.max_one_symbol_prefix

    return next_state


def choice(left_state, right_state):
    next_state = State()
    next_state.can_be_one_symbol_word = left_state.can_be_one_symbol_word or right_state.can_be_one_symbol_word

    next_state.max_one_symbol_length = max(left_state.max_one_symbol_length,
                                           right_state.max_one_symbol_length)

    next_state.max_one_symbol_prefix = max(left_state.max_one_symbol_prefix,
                                           right_state.max_one_symbol_prefix)

    return next_state


def repeat(state):
    next_state = State()
    next_state.can_be_one_symbol_word = True

    if state.max_one_symbol_length:
        next_state.max_one_symbol_length = math.inf
        next_state.max_one_symbol_prefix = math.inf
    else:
        next_state.max_one_symbol_length = 0
        next_state.max_one_symbol_prefix = state.max_one_symbol_prefix

    return next_state


def get_final_state(regex, prefix_symbol):
    state_stack = []

    for regex_symbol in regex:
        try:
            if regex_symbol in alphabet:
                state = State(prefix_symbol, regex_symbol)
                state_stack.append(state)
            elif regex_symbol in operations:
                if regex_symbol == '.':
                    right_state = state_stack.pop()
                    left_state = state_stack.pop()
                    state_stack.append(concatenate(left_state, right_state))
                elif regex_symbol == '+':
                    right_state = state_stack.pop()
                    left_state = state_stack.pop()
                    state_stack.append(choice(left_state, right_state))
                elif regex_symbol == '*':
                    state = state_stack.pop()
                    state_stack.append(repeat(state))
            else:
                raise Exception('ERROR: unexpected symbol')
        except IndexError:
            raise Exception('ERROR: inconsistent regular expression')

    if len(state_stack) > 1:
        raise Exception('ERROR: inconsistent regular expression')

    return state_stack.pop()


def check_has_prefix(regex, prefix_symbol, number):
    final_state = get_final_state(regex, prefix_symbol)

    return final_state.max_one_symbol_prefix >= number


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-r", "--regex",
                        dest="regex",
                        help="Regular expression in Reverse Polish notation (describes the language)",
                        required=True)

    parser.add_argument("-x", "--symbol",
                        dest="symbol",
                        help="Symbol of prefix to search",
                        required=True)

    parser.add_argument("-k", "--number",
                        dest="number",
                        help="Number of symbol repetitions in prefix",
                        type=int,
                        required=True)

    args = parser.parse_args()

    try:
        print('YES' if check_has_prefix(
            args.regex, args.symbol, args.number) else 'NO')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

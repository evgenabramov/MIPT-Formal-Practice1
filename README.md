# Practice on regular expressions

[![Build Status](https://travis-ci.com/evgenabramov/MIPT-Formal-Practice1.svg?token=BTLs4oCWwqfaRL1pjb6t&branch=dev)](https://travis-ci.com/evgenabramov/MIPT-Formal-Practice1)
[![codecov](https://codecov.io/gh/evgenabramov/MIPT-Formal-Practice1/branch/dev/graph/badge.svg?token=i777yrlJt9)](https://codecov.io/gh/evgenabramov/MIPT-Formal-Practice1)

> ### [Русская версия](README_ru.md)

## Problem description

Designation: `α` - a regular expression in reverse Polish notation specifying the language `L`. `α` is given in the alphabet `{a, b, c, 1,., +, *}`.

Given `α`, letter `x` and natural number `k`. The task is to check if the language `L` contains any words with the prefix `x ^ k` (`k` `x`-characters in a row).

In case the input string is not a correct regular expression in reverse Polish notation, an `ERROR` message should occur.

## Solution

Let's denote the character being searched by `x`.
Also let's assign to each regular expression the structure `State`, which stores the following information about the language `L`, given by the regular expression `α`:

1. Does `L` contain a word consisted only of `x`-characters

2. Maximum length of a word from `L` containing only `x`-characters

3. Length of longest prefix containing only `x` characters among words from `L`

Note that these values are independent, that is, for the same regular expression, their values can correspond to different words from `L`.

Let's solve the problem using dynamic programming.

Let's read the regular expression character by character. Since the expression is parsed in reverse Polish notation, it is convenient to use the stack with the current states to restore the operands to which the next operation is applied. Then the last operation is applied to the last two values on the stack.

At the same time, when reading *a letter*, a new state is always added to the stack, which is uniquely determined based on whether it is equal to `x` or not. When reading *an operation*, the top two states on the stack are replaced with one common one.

It is easy to show (using case analysis) that based on the values for two operands from the stack stored in the `State` structure, it is possible to unambiguously restore the corresponding values for the result state obtained after applying the next operation.

Thus, after sequential reading of the regular expression, the **final state** will be obtained, which corresponds to the language `L`.

To get an answer, it is enough to compare the value for the final state of the length of the longest prefix containing only characters `x` with the number `k` from the input.

## Usage

```bash
python3 main.py --regex [REGEX] --symbol [SYMBOL] --number [NUMBER]
```

Где:

- `REGEX` - regular expression specifing the language `L`
- `SYMBOL` - symbol being used to search
- `NUMBER` - the number of occurrences of the `SYMBOL` character in the prefix of a word from `L`

**Run tests** with coverage information (the required configuration file is already in the root of the repository):

```bash
pytest
```

In addition, there is up-to-date information on passing tests obtained from [Travis-CI](https://travis-ci.org) and detailed information on test coverage with a beautiful interface [Codecov](https://codecov.io/) (accessed via badges at the top of this file).

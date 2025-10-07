#!/bin/bash
# bash check_test_methods.bash

FILE="tests/test_exercise_2.py"

if ! grep -q "test_fizz_buzz(self)" "$FILE"; then
    exit 2
fi

if ! grep -q "test_is_palindrome(self)" "$FILE"; then
    exit 3
fi

if ! grep -q "test_factorial(self)" "$FILE"; then
    exit 4
fi

if ! grep -q "test_are_anagrams(self)" "$FILE"; then
    exit 5
fi

exit 0
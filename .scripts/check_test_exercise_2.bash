#!/bin/bash
# bash .scripts/check_test_exercise_2.bash

FILE="tests/test_exercise_2.py"

if [ -e "$FILE" ]; then
    bash .scripts/check_test_methods.bash
    exit $?
fi

exit 1
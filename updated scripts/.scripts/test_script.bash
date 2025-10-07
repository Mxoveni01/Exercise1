#!/bin/bash

# Run check script to validate the test file and methods
bash .scripts/check_test_exercise_2.bash
FILE_CHECK_RESULTS=$?
TOTAL_PASSED=0
CHECKS=0

echo ""
echo "____________RESULTS___________"
echo ""
case $FILE_CHECK_RESULTS in
    1)
        echo "❌ ERROR: The test file 'test_exercise_2.py' does not exist in the 'tests' folder."
        echo ""
        (( CHECKS++ ))
        ;;
    2)
        echo "❌ ERROR: Missing or incorrectly named method to test 'fizz_buzz'."
        echo "➡️  Expected method name: 'test_fizz_buzz(self)'"
        echo ""
        (( CHECKS++ ))
        ;;
    3)
        echo "❌ ERROR: Missing or incorrectly named method to test 'is_palindrome'."
        echo "➡️  Expected method name: 'test_is_palindrome(self)'"
        echo ""
        (( CHECKS++ ))
        ;;
    4)
        echo "❌ ERROR: Missing or incorrectly named method to test 'factorial'."
        echo "➡️  Expected method name: 'test_factorial(self)'"
        echo ""
        (( CHECKS++ ))
        ;;
    5)
        echo "❌ ERROR: Missing or incorrectly named method to test 'are_anagrams'."
        echo "➡️  Expected method name: 'test_are_anagrams(self)'"
        echo ""
        (( CHECKS++ ))
        ;;
esac

if (( CHECKS > 0 ));then
  echo "❌ ERROR: THERE ARE CHECK FAILURES"
else
  echo "✅ All checks passed. Running unit tests..."
  echo ""
fi

# Function to run tests and parse results
run_tests() {
  local test_file=$1
  echo ""
  echo "🔍 Running tests from: $test_file"

  # Run unittest and capture output
  TEST_OUTPUT=$(python3 -m unittest "$test_file" 2>&1)
  echo "$TEST_OUTPUT"

  # Extract tests run
  TESTS_RUN=$(echo "$TEST_OUTPUT" | grep -oP 'Ran \K[0-9]+')

  # Determine if tests passed or failed
  if echo "$TEST_OUTPUT" | grep -q "OK"; then
    FAILURES=0
    ERRORS=0
  else
    # Extract failures and errors (default to 0 if not found)
    FAILURES=$(echo "$TEST_OUTPUT" | grep -oP 'failures=\K[0-9]+' || echo 0)
    ERRORS=$(echo "$TEST_OUTPUT" | grep -oP 'errors=\K[0-9]+' || echo 0)
  fi

  PASSED=$(( TESTS_RUN - FAILURES - ERRORS ))
  ((TOTAL_PASSED+=$PASSED))

  # Calculate passing percentage
  if [ "$TESTS_RUN" -eq 0 ]; then
    PASS_PERCENT=0
  else
    PASS_PERCENT=$(awk "BEGIN {printf \"%.2f\", ($PASSED / $TESTS_RUN) * 100}")
  fi

  echo "✅ Tests run: $TESTS_RUN, Passed: $PASSED, Failures: $FAILURES, Errors: $ERRORS"
  echo "📊 Passing percentage: $PASS_PERCENT%"
  echo ""

  return 0
}


run_tests tests/test_data_structures.py || exit 1
run_tests tests/test_exercise_2.py || exit 1
run_tests tests/test_hidden.py || exit 1

RESULT=""
TOTAL_PERCENTAGE=$(( $TOTAL_PASSED * 100 / 23 ))

if (( $TOTAL_PERCENTAGE > 50 )); then
  RESULT="PASSED"
else
  RESULT="FAILED"
fi

FLOAT_PERCENTAGE=$(awk "BEGIN {printf \"%.2f\", ($TOTAL_PASSED / 23) * 100}")


echo ""
echo "✅ TOTAL PASSED OUT OF 23 TEST CASES : $TOTAL_PASSED cases"
echo "📊 TOTAL PERCENTAGE : $FLOAT_PERCENTAGE%, $RESULT"
echo ""
echo "_________END OF RESULTS__________"
# Problems - Stats WTC

## Exercise 1


* Modify `data_structures.py` to solve the problem as stated in doc strings.
* You can test technical correctness by running the unittests as in the section *To Test* below.

### To Test

* To run all the unittests: `python3 -m unittest tests/test_data_structures.py`
* To run a specific step's unittest, e.g step *1*: `python3 -m unittest tests.test_data_structures.TestFunctions.test_find_max`
* _Note_: at the minimum, these (*unedited*) tests must succeed before you may submit the solution for review.


## Exercise 2

For this exercise create a file named `test_exercise_2.py` where you'll be writing your tests.

### 1. FIZZBUZZ
- Write a function named `fizz_buzz` that returns:
  - `"Fizz"` if divisible by 3
  - `"Buzz"` if divisible by 5
  - `"FizzBuzz"` if divisible by 3
  - The number otherwise


### 2. Palindrome Checker
- A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.

- Write a function `is_palindrome` that returns True if a string is a palindrome.


### 3. Factorial
- Write `factorial(n)` to return the factorial of a number.

### 4. Anagram Checker
- Anagrams are words or phrases that can be rearranged to make an entirely different word or phrase

- Write a function `are_anagrams(str1, str2)` that checks if given strings are anagrams.

# Important

To get your results run the command `bash .scripts/test_script.bash`
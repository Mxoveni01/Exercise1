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

## FINAL BOSS

Generates Pascal's triangle `pascal_triangle(n:int)` and returns the final row as a list.

    Parameters:
    n (int): The row number of Pascal's triangle to generate (0-based index).

    Returns:
    list: The final row of Pascal's triangle as a list.

    Formula for Pascal's Triangle:
    Each element in Pascal's triangle can be calculated using the following formula:

    C(n, k) = n! / (k! * (n-k)!)

    Where:
    - n is the row number (0-based index)
    - k is the column number (0-based index)
    - C(n, k) represents the value at row n and column k in Pascal's triangle
    - n! represents the factorial of n

    To generate a row of Pascal's triangle, iterate over the columns from 0 to n.
    Calculate each element using the formula and store them in a list to form the row.
    Repeat this process for each row up to the desired row number.

    Example:
     * Input: n = 6
     * Output:
     *           1
     *         1   1
     *       1   2   1
     *     1   3   3   1
     *   1   4   6   4   1
     * 1   5  10   10  5   1

No need for writing your own test.


# Important

To get your results run the command `bash .scripts/test_script.bash`
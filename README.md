# Homework 2

The purpose of this homework is to practice functional programming.

As a result the following restrictions apply for Problems 1-5:

- You may not use `while`, `len`, indexing such as `seq[n]` or `seq[n:m]`, or sequence methods like `list.append`, etc.
- You may not use the `for` or `if` statement, aside from within comprehensions.
- No global variables.
- You may write helper functions, but they too must obey these restrictions.
- You may use `functools.reduce`, but no other functions that require an import.
    - https://docs.python.org/3/library/functools.html#functools.reduce
    - https://realpython.com/python-reduce-function/
- Builtin functions like `map`, `filter` and `list` are allowed. `list(...)` can be useful to convert the result of a generator into a `list`.
- You may use unpacking syntax like `a, b = (1, 2)`.

If in doubt about a function or language feature, you should ask on `Ed Discussion` (If your question requires you to post code please be sure to post private messages.) and we will gladly clarify for everyone.

Please take special care to follow these instructions, use of a disallowed function or construct will result in a significant loss of points for the problem.

**You will also notice that each problem requires you to create a new file, in contrast to the function stubs we provided previously.  Be sure to document your functions!**

## Problems

### Problem 1

Implement the `satisfy` and `satisfy_all` functions in a new file named `problem1/problem1.py`.

`satisfy` takes in two predicate functions (`func1` and `func2`) and a list of integers (`values`).

The function should return a list of two-element tuples. The first component of the tuple should be the integer from `values` and the second is `True` if both predicate functions return `True` and `False` otherwise.

Example:

```python
>>> import problem1
>>> problem1.satisfy(lambda x: x > 10, lambda y: y < 100, [1, 20, 200])
[(1, False), (20, True), (200, False)]

>>> problem1.satisfy(lambda x: x > 10, lambda y: y < 100, [])
[]

>>> problem1.satisfy(lambda x: x > 10, lambda y: y < 100, [2])
[(2, False)]
```

`satisfy_all` takes a list of predicates (`funcs`) and a list of integers (`values`).

The function should return a list of two-element tuples.
The first component is an integer from `values` and the second is a list of the return values from calling each predicate function with the integer.

```python
>>> import problem1
>>> funcs = [lambda x: x > 10, lambda y: y < 100]

>>> problem1.satisfy_all(funcs, [1, 20, 200])
[(1, [False, True]), (20, [True, True]), (200, [True, False])]

>>> problem1.satisfy_all(funcs, [])
[]

>>> funcs = [lambda x: x > 10, lambda y: y < 100, lambda z: False]
>>> problem1.satisfy_all(funcs, [1, 20, 200])
[(1, [False, True, False]), (20, [True, True, False]), (200, [True, False, False])]
```

Tests are provided in `problem1/test_problem1.py`.

### Problem 2

Implement a `count_all` function that takes in a list of lists and returns the total count of objects inside the nested lists.

```python
>>> import problem2

>>> problem2.count_all([[1, 2, 3], ["a"], [3, 4, 5]])
7
>>> problem2.count_all([])
0
>>> problem2.count_all([[1], [], [3]])
2
```

**Restriction**

Remember, you may not use `len`, you may want to use `functools.reduce` to reimplement it.

### Problem 3

Implement a `duplicate` function that takes a list of integers `values` and an additional integer `num`.

This function returns a list of tuples where each tuple contains an integer from `values` duplicated `num` times.

Example:
```python
>>> import problem3

>>> problem3.duplicate([1,2,3], 3)
[(1, 1, 1), (2, 2, 2), (3, 3, 3)]

>>> problem3.duplicate([], 3)
[]

>>> problem3.duplicate([1,2,3], 0)
[(), (), ()]

>>> problem3.duplicate([1,2,3], 1)
[(1,), (2,), (3,)]
```

**Restriction**

Remember, you may not use the `*` repetition operator for sequence types for this problem. You are free to write a helper function to perform this for you.

### Problem 4

Implement a `calc` function that takes in a string `op` representing an operation and two operands `a` and `b` and returns the result of a given calculation.

Example:
```python
>>> import problem4

>>> problem4.calc("+", 1, 2)
3

>>> problem4.calc("/", 5, 2)
2.5

>>> problem4.calc("*", "!", 4)
"!!!!"
```

Possible values for `op` are: `"+"`, `"-"`, `"*"`, and `"/"`.

Note: You do not need to handle cases where the operation performed would be illegal (e.g. `calc("!", "4")`).

**Restrictions**

Remember, you may not use an `if` statement.


### Problem 5

Implement the function `list_range` which takes a two-element tuple `bounds` and a list of integer lists `values`.

The function should return a list that includes each integer list from `values` where every member is within `bounds`.

`bounds` should be inclusive on both ends, so if `bounds = (1, 3)`, the list `[1, 2, 3]` is within bounds.

You may assume that the first component of bounds is always less than or equal to the second component.

Examples:
```python
>>> problem5.list_range((1, 3), [[1, 3, 2], [9, 3, 1], [2, 1]])
[[1, 3, 2], [2, 1]]

>>> problem5.list_range((1, 100), [[1, 3, 2], [9, 3, 1], [2, 1]])
[[1, 3, 2], [9, 3, 1], [2, 1]]

>>> problem5.list_range((1, 3), [])
[]

>>> problem5.list_range((1, 1), [[1, 3, 2], [9, 3, 1], [2, 1]])
[]
```

### Problem 6

Implement the function `grep` with the following definition:

```
def grep(pattern, lines, ignore_case=False):
    pass
```

`pattern` is a string that represents text we're searching for within each line.

`lines` is an iterable of strings to search within.

`ignore_case` indicates whether or not the comparison should be done in a case-sensitive manner or not.

**You must implement grep as a generator function.  It must not return a list.**

The below example shows expected behavior, as well as some useful ways to test your generator function from the REPL:

```python
>>> import problem6

>>> lines = ["I went to Poland.", "He went to Spain.", "She is very happy."]

>>> gen = problem6.grep("went", lines)

# useful to call `list` on the generator to see results all at once
>>> list(gen)
["I went to Poland.", "He went to Spain."]

>>> gen = problem6.grep("he", lines, ignore_case=True)
>>> next(gen)
"He went to Spain."
>>> next(gen)
"She is very happy."
>>> next(gen)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
```

Note:
* The restrictions for problems 1-5 do not apply to problem 6.
* We do not provide a full test suite for this function. Be sure to test various cases in your REPL or any other method you choose.

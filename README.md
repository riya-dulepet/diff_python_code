# diff_python_code

## Instructions to install requirements
ast, re, argparse, difflib, and unittest are all part of the Python standard library. 

## How to run
Similar to how GitHub identifies changes between files I constructed the script such that it parses through two files.
1) Create a python file that we will treat as the original file that we want to find the difference of
2) Create another python file that we have changed and want to compare the first file too
3) Run the following command: python diff_python_code.py file1.py file2.py
4) Run test suite command:  python TestDiffAlgo.py

## Approach explanation
1) Removing Non-Functional Elements: I have a function remove_non_functional_elements(code) that strips away comments, docstrings, and extraneous whitespace from Python code. This preprocessing step helps focus the diff on functional elements of the code only, which are crucial for understanding the nature of changes.
2) Diff Resolution: The resolve_diff(code1, code2) function compares two versions of Python code after they have been stripped of non-functional elements. It uses difflib.Differ to create a line-wise diff, selectively ignoring irrelevant differences (like purely formatting changes). This results in a list of meaningful differences that likely impact functionality.
3) Grouping Changes: The algorithm looks for adjacent lines of deletions and additions, grouping them together as a single change when appropriate.
   
I used the Abstract Syntax Tree (AST) module because it allows for the analysis and manipulation of Python code at a structural level. Utilizing AST, I am essentially parsing Python code into a tree of nodes, where each node represents a specific element of the source code, such as expressions, statements, or constructs. This capability enables tasks such as removing or modifying code elements systematically without altering the underlying functionality.

## Inspirations
https://www.codeproject.com/Articles/5310967/Analyzing-Python-with-the-AST-Package
https://discuss.python.org/t/compiling-evaling-arbitrary-ast-trees/31251/3
https://towardsdatascience.com/find-the-difference-in-python-68bbd000e513





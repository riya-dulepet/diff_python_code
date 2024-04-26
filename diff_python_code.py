import ast
import re
import argparse
import difflib

def remove_non_functional_elements(code):
    # Remove comments
    code = re.sub(r'#.*', '', code)
    code = re.sub(r'""".*?"""', '', code, flags=re.DOTALL)
    code = re.sub(r"'''.*?'''", '', code, flags=re.DOTALL)

    # Remove docstrings
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            if ast.get_docstring(node):
                node.body = node.body[1:]

    # Remove blank lines and trailing whitespace
    code_lines = ast.unparse(tree).split('\n')
    code_lines = [line.rstrip() for line in code_lines if line.strip()]

    # Join the code lines back into a single string
    functional_code = '\n'.join(code_lines)

    return functional_code

def resolve_diff(code1, code2):
    # Remove non-functional elements
    functional_code1 = remove_non_functional_elements(code1)
    functional_code2 = remove_non_functional_elements(code2)

    # Create line-wise diff
    lines1 = functional_code1.split('\n')
    lines2 = functional_code2.split('\n')

    differ = difflib.Differ()

    # Generate a list of differences
    diff = list(differ.compare(lines1, lines2))
    diff = [line for line in diff if not line.startswith('?')]
    grouped_changes = []
    i = 0
    while i < len(diff):
        line = diff[i]
        if line.startswith('- '):
            # Look ahead to check for an addition immediately following a deletion
            if i + 1 < len(diff) and diff[i + 1].startswith('+ '):
                grouped_changes.append(f"{line}\n{diff[i + 1]}")
                i += 1  # Skip the next line as it's already processed as part of a change pair
            else:
                grouped_changes.append(line)
        elif line.startswith('+ ') and (i == 0 or not diff[i - 1].startswith('- ')):
            grouped_changes.append(line)
        i += 1
    return grouped_changes



if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Compare two Python files after removing non-functional elements.')
    parser.add_argument('file1', help='Path to the first Python file')
    parser.add_argument('file2', help='Path to the second Python file')
    args = parser.parse_args()

    # Read the Python code from the input files
    with open(args.file1, 'r') as file:
        code1 = file.read()

    with open(args.file2, 'r') as file:
        code2 = file.read()

    predicted_output = resolve_diff(code1, code2)

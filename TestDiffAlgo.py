import unittest
from diff_python_code import resolve_diff


class TestDiffAlgo(unittest.TestCase):
    def test_basic_1(self):
        with open("test_files/test_a.py", 'r') as file:
            code1 = file.read()
        # print(code1)

        with open("test_files/test_b.py", 'r') as file:
            code2 = file.read()

        predicted_output = resolve_diff(code1, code2)
        desired_output = ['- api_router = APIRouter()\n+ api_router = APIRouter('
                          'redirect_slashes=True)']
        self.assertEqual(desired_output, predicted_output)

    def test_basic_2(self):
        with open("test_files/test_b.py", 'r') as file:
            code1 = file.read()
        # print(code1)

        with open("test_files/test_c.py", 'r') as file:
            code2 = file.read()

        predicted_output = resolve_diff(code1, code2)
        desired_output = []
        self.assertEqual(desired_output, predicted_output)


    def test_change_function_argument(self):
        # Test Case 1: Change in Function Argument
        with open("test_files/test_change_function_argument/test_a.py", 'r') as file:
            code1 = file.read()

        with open("test_files/test_change_function_argument/test_b.py", 'r') as file:
            code2 = file.read()

        predicted_output = resolve_diff(code1, code2)
        desired_output = ["- data = list(range(10))\n+ data = list(range(1, 11))"]
        self.assertEqual(desired_output, predicted_output)

    def test_addition_function_parameter(self):
        # Test Case 2: Addition of a Function Parameter
        with open("test_files/test_addition_function_argument/test_a.py", 'r') as file:
            code1 = file.read()

        with open("test_files/test_addition_function_argument/test_b.py", 'r') as file:
            code2 = file.read()

        predicted_output = resolve_diff(code1, code2)
        desired_output = ["- info = dict(name='Alice')\n+ info = dict(name='Alice', age=30)"]
        self.assertEqual(desired_output, predicted_output)

    def test_decorator(self):
        # Test Case 3: Change in Method Behavior due to Decorator

        with open("test_files/test_decorator/test_a.py", 'r') as file:
            code1 = file.read()

        with open("test_files/test_decorator/test_b.py", 'r') as file:
            code2 = file.read()

        predicted_output = resolve_diff(code1, code2)
        desired_output = ['+ @staticmethod']
        self.assertEqual(desired_output, predicted_output)


    def test_change_in_loop(self):
        # Test Case 4: Change in Loop Structure

        with open("test_files/test_change_in_loop/test_a.py", 'r') as file:
            code1 = file.read()

        with open("test_files/test_change_in_loop/test_b.py", 'r') as file:
            code2 = file.read()

        predicted_output = resolve_diff(code1, code2)
        desired_output = ['- for i in range(5):\n+ for i in range(0, 5, 2):']
        self.assertEqual(desired_output, predicted_output)


    def test_change_in_conditionals(self):
        # Test Case 5: Change in Conditional Logic
        with open("test_files/test_change_in_conditionals/test_a.py", 'r') as file:
            code1 = file.read()

        with open("test_files/test_change_in_conditionals/test_b.py", 'r') as file:
            code2 = file.read()

        predicted_output = resolve_diff(code1, code2)
        desired_output = ['- if x % 2 == 0:\n+ if x % 2 == 0 and x != 0:']
        self.assertEqual(desired_output, predicted_output)


    def test_change_in_conditionals_and_body(self):
        # Test Case 6: Change in Conditional Logic and Change in body
        with open("test_files/test_change_in_conditionals_and_body/test_a.py", 'r') as file:
            code1 = file.read()

        with open("test_files/test_change_in_conditionals_and_body/test_b.py", 'r') as file:
            code2 = file.read()

        predicted_output = resolve_diff(code1, code2)
        desired_output = ['- if x % 2 == 0:\n+ if x % 2 == 0 and x != 0:', "-     print('Odd')\n+     print('Even')"]
        self.assertEqual(desired_output, predicted_output)


    def test_exception_handling(self):
        # Test Case 7: Modification in Exception Handling



        with open("test_files/test_exception_handling/test_a.py", 'r') as file:
            code1 = file.read()

        with open("test_files/test_exception_handling/test_b.py", 'r') as file:
            code2 = file.read()

        predicted_output = resolve_diff(code1, code2)
        desired_output = ['+ except Exception as e:', "+     print('Unexpected error:', e)"]
        self.assertEqual(desired_output, predicted_output)



    def test_class_inheritance(self):
        # Test Case 8: Change in Class Inheritance
        with open("test_files/test_class_inheritance/test_a.py", 'r') as file:
            code1 = file.read()

        with open("test_files/test_class_inheritance/test_b.py", 'r') as file:
            code2 = file.read()

        predicted_output = resolve_diff(code1, code2)
        desired_output = ["- class Vehicle:\n+ class Vehicle(object):"]
        self.assertEqual(desired_output, predicted_output)


    def test_new_variable(self):
        # Test Case 9: Introduction of a New Variable

        with open("test_files/test_new_variable/test_a.py", 'r') as file:
            code1 = file.read()

        with open("test_files/test_new_variable/test_b.py", 'r') as file:
            code2 = file.read()

        predicted_output = resolve_diff(code1, code2)
        desired_output = ['- print(a + b)\n+ avg = (a + b) / 2', "+ print(a + b, 'Average:', avg)"]
        self.assertEqual(desired_output, predicted_output)


    def test_list_comprehension(self):
        # Test Case 10: Modification in List Comprehension

        with open("test_files/test_list_comprehension/test_a.py", 'r') as file:
            code1 = file.read()

        with open("test_files/test_list_comprehension/test_b.py", 'r') as file:
            code2 = file.read()

        predicted_output = resolve_diff(code1, code2)
        desired_output = ['- squares = [x ** 2 for x in numbers]\n+ cubes = [x ** 3 for x in numbers if x % 2 == 1]']
        self.assertEqual(desired_output, predicted_output)



    def test_doc_string(self):
        # Test Case 11: Doc String Difference

        with open("test_files/test_doc_string/test_a.py", 'r') as file:
            code1 = file.read()

        with open("test_files/test_doc_string/test_b.py", 'r') as file:
            code2 = file.read()

        predicted_output = resolve_diff(code1, code2)
        desired_output = []
        self.assertEqual(desired_output, predicted_output)

if __name__ == '__main__':
    unittest.main()

# Extended error handling
try:
    x = 1 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')
except Exception as e:
    print('Unexpected error:', e)
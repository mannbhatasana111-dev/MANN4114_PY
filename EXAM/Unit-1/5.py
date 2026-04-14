# Using lambda function
add = lambda a, b: a + b
print("Using Lambda Function:", add(10, 5))

# Using named function
def add_numbers(a, b):
    return a + b

print("Using Named Function:", add_numbers(10, 5))

'''
Lambda functions are useful for small tasks but difficult to debug and reuse.
Named functions are easier to read, debug, and reuse in many places.
Therefore, named functions are better for long-term maintenance.

'''

"""
The walrus operator, officially known as the assignment expression operator and denoted by :=,
was introduced in Python 3.8. It allows you to assign a value to a variable as part of a larger expression.

"""

# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
    # Output: List is too long (5 elements, expected <= 3)


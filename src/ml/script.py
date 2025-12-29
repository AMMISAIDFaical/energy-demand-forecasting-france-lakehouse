# mock_py_script.py

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

if __name__ == "__main__":
    x = 5
    y = 10
    print("Sum:", add(x, y))
    print("Product:", multiply(x, y))
# Problem 2: Generate odd numbers series

def generate_odd_series(a):
    return [2 * i - 1 for i in range(1, a + 1)]

# Example usage
print(generate_odd_series(4))

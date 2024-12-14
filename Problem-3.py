# Problem 3: Modified odd numbers series

def generate_modified_series(a):
    series = []
    for i in range(1, a + 1):
        if i % 2 != 0:
            series.append(2 * i - 1)
    return series

# Example usage
print(generate_modified_series(5))

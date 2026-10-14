# Used PyCharm AI integration to create a file and update it as well.

# Multiplication Table for x up to x * n

def print_multiplication_table(x: int, n: int) -> None:
    """Print the multiplication table for x from 1 to n."""
    print(f"--- Multiplication Table for {x} (up to {x} x {n}) ---")
    for i in range(1, n + 1):
        print(f"{x} x {i} = {x * i}")


if __name__ == "__main__":
    # Example usage: table for 5 up to 5 x 10
    print_multiplication_table(4, 12)

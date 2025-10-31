# app/app.py
def calculate_total(items):
    """Return sum of items (list of numbers)."""
    total = 0
    for x in items:
        total += x
    return total

if __name__ == "__main__":
    print(calculate_total([1,2,3]))

def linear_search(arr, target):
    """Return the index of `target` in `arr` using linear search.

    Returns -1 if `target` is not present.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    sample = [23, 45, 12, 67, 34, 89, 10]
    target = 67
    idx = linear_search(sample, target)
    if idx != -1:
        print(f"Found {target} at index {idx}")
    else:
        print(f"{target} not found in the list")

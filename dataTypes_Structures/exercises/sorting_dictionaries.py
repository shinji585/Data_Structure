def sort_dict(d: dict) -> list:
    return sorted(d.items(), reverse=True, key=lambda item: item[1])


print(f"Test: {sort_dict(d={3: 1, 2: 2, 1: 3})}")
print(f"Test 2: {sort_dict(d={1: 2, 2: 4, 3: 6})}")
print(f"Test 3: {sort_dict(d={3: 1, 2: 2, 1: 3})}")

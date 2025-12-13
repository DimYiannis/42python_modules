def test_error_types(num, div, file, data, key):

    try:
        print("\nTesting ValueError...")
        x = int(num)
        print(f"{x}")
    except ValueError:
        print("Caught ValueError: invalid literal for int() ")

    try:
        print("\nTesting ZeroDivisionError...")
        y = 10 / div
        print(f"{y}")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    try:
        print("\nTesting FileNotFoundError...")
        with open(file, "r") as f:
            f.read()
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{file}' ")

    try:
        print("\nTesting KeyError...")
        value = data[key]
        print(f"{value}")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    try:
        print("\nTesting multiple errors together...")
        x = int(num)
        y = 10 / div
        with open(file, "r") as f:
            f.read()
        value = data[key]
    except Exception:
        print("Caught an error, but program continues!")


def garden_operations():
    print("=== Garden Error Types Demo ===")

    # test_error_types("abc", 1, "ft_different_errors.py",
    #                 {"plant": 1}, "plant")

    # test_error_types(10, 0, "ft_different_errors.py", {"plant": 1}, "plant")

    # test_error_types(10, 1, "missing.txt", {"plant": 1}, "plant")

    # test_error_types(10, 1, "ft_different_errors.py",
    #        {"plant": 1}, "missing_plant")

    print("Testing multiple errors together...")
    test_error_types("abc", 0, "missing.txt", {}, "missing_plant")
    print("\nAll error types tested successfully!")


garden_operations()

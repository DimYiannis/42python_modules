def check_temperature(temp_str):
    print("=== Garden Temperature Checker ===")

    try:
        t = int(temp_str)
        if t > 40:
            print(f"Error: {t}°C is too hot for plants (max 40°C)")
        elif t < 0:
            print(f"Error: {t}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {t}°C is perfect for plants")

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number ")
    finally:
        print("\nAll tests completed - program didn't crash!")


"""
check_temperature(10)
check_temperature(100)
check_temperature("abc")
check_temperature(-10)

"""

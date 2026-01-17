def crisis_handler(filename: str, is_ok: bool) -> None:
    """
    - Handle archive access during routine operations or crisis situations.
    - open and read file and report whether access is ok or
        triggered by a crisis, and handles common failure.
    """
    try:
        if is_ok:
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{filename}'...")

        with open(filename, "r") as data:
            print(f"SUCCESS: Archive recovered - ``{data.read()}``")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis contained, analysis required\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler("../lost_archive.txt",  is_ok=False)
    crisis_handler("../classified_vault.txt",  is_ok=False)
    crisis_handler("../standard_archive.txt", is_ok=True)
    print("All crisis scenarios handled successfully. Archives secure.")

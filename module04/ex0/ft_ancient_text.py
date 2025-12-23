if __name__ == "__main__":
    """main"""
    fd = "../ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"\nAccessing Storage Vault: {fd}")

    with open(fd, "r") as data:
        print("Connection established...\n")
        print("RECOVERED DATA:")
        for line in data:
            if len(line) > 0 and line[-1] == "\n":
               line = line[:-1]
            print(line)
        print("\nData recovery complete. Storage unit disconnected.")

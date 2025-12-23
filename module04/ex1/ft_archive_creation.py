if __name__ == "__main__":
    """main"""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    print("\n Initializing new storage unit: new_discovery.txt")
    try:
        with open("new_discovery.txt", "w") as data:
            print("\nStorage unit created successfully...")
            str1 = "{[}ENTRY 001{]} New quantum algorithm discovered"
            str2 = "{[}ENTRY 002{]} Efficiency increased by 347%"
            str3 = "{[}ENTRY 003{]} Archived by Data Archivist trainee"
            print("\nConnection established...")
            data.write(f"{str1}")
            data.write("\n")
            data.write(f"{str2}")
            data.write("\n")
            data.write(f"{str3}")
            print(f"{str1}\n{str2}\n{str3}")
        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except Exception:
        print("\nERROR: Storage vault not created.")

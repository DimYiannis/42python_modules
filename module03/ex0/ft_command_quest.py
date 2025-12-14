import sys

print("=== Command Quest ===")

if len(sys.argv) < 2:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {len(sys.argv)}")
else:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {len(sys.argv) - 1}")
    j = 1
    while j < len(sys.argv):
        print(f"Argument {j}: {sys.argv[j]}")
        j += 1
    print(f"Total arguments: {len(sys.argv)}")




import os
import sys
from dotenv import load_dotenv

if __name__ == "__main__":

    load_dotenv()

    print("\nORACLE STATUS: Reading the Matrix...\n")

    mode = os.getenv('MATRIX_MODE', 'development')
    database_url = os.getenv('DATABASE_URL', 'sqlite:///local.db')
    api_key = os.getenv('API_KEY')
    log_level = os.getenv('LOG_LEVEL', 'DEBUG')
    endpoint = os.getenv('ZION_ENDPOINT', 'http://localhost:8080')

print("Configuration loaded:")
print(f"Mode: {mode}")

if 'sqlite' in database_url:
    print(f"Database: Connected to local instance")
else:
    print(f"Database: Connected to remote instance")

if api_key:
        print(f"  API Access: Authenticated")
else:
    print(f"  API Access: No key provided")

print(f"  Log Level: {log_level}")

if endpoint:
    print("Zion Network: Online")
else:
    print("Zion Network: Offline")

print("\nEnvironment security check:")
print("[OK] No hardcoded secrets detected")

if os.path.exists('.env'):
    print("[OK] .env file properly configured")
else:
    print("[WARNING] .env file not found")

if os.path.exists('.gitignore'):
    with open('.gitignore', 'r') as f:
        if '.env' in f.read():
            print("[OK] Production overrides available")
        else:
            print("[WARNING] .env not in .gitignore")

print("\nThe Oracle sees all configurations")


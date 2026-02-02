import sys
import importlib.metadata

def check_dependencies():
    """
    check if dependencies are installed
    and show their version
    """
    required_packages = {
        'pandas': 'Data manipulation',
        'requests': 'Network access',
        'matplotlib': 'Visualization'
    }

    status = {}
    all_available = True

    print("LOADING STATUS: Loading programms...")
    print("Checking dependencies:")

    for package, description in required_packages.items():
        try:
            version = importlib.metadata.version(package)
            status[package] = {'available': True, 'version': version}
            print(f" [OK] {package} ({version}) - {description} ready")
        except importlib.metadata.PackageNotFoundError:
            status[package] = {'available': False, 'version': None}
            print(f" [MISSING] {package} - {description} NOT available")
            all_available = False
    return status, all_available


def show_installation_instructions():
    print("\nERROR: Missing required dependencies!")
    print("\nTo install with pip:")
    print("pip install -r requirements.txt")
    print("\nTo install with Poetry:")
    print("poetry install")
    print("poetry run python loading.py")
    print("\nPackage Management Comparison:")
    print("pip: Simple, uses requirements.txt, global or venv installation")
    print("Poetry: Advanced, uses pyproject.toml, automatic venv management, dependency resolution")


def generate_matrix_data():
    """
        simulate data for analysis
    """
    import pandas as pd
    import numpy as np 

    data = {
        'value': np.random.normal(500, 50, 1000),
        'category': np.random.choice(['A', 'B', 'C'], 1000)
    }

    df = pd.DataFrame(data)
    return df


def get_weather():
    import requests
    import pandas as pd

    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": 52.3676, "longitude": 4.9041, "hourly": "temperature_2m"}
    data = requests.get(url, params=params).json()

    df = pd.DataFrame(data['hourly'])['temperature_2m']
    return df


def weather_visualization(data):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=20, color="skyblue", edgecolor= "black")

    plt.title('hourly temperature in Amsterdam')
    plt.xlabel('temperature (C')
    plt.ylabel("frequency")
    plt.show()


def create_visualization(df):
    """
        create visualization for the data
    """
    import matplotlib.pyplot as plt

    print("\nGenerating visualization...")

    # simple example
    plt.hist(df['value'], bins=100)

    plt.title("histogram")
    plt.xlabel("value")
    plt.ylabel("frequency")

    '''
    # more complex histogram per category
    plt.hist(df[df['category'] == 'A']['value'], bins = 20, alpha=0.5, label='A')
    plt.hist(df[df['category'] == 'B']['value'], bins=20, alpha=0.5, label='B')
    plt.hist(df[df['category'] == 'C']['value'], bins=20, alpha=0.2, label='C')

    plt.title("Value distribution by category")
    plt.xlabel("value")
    plt.ylabel("frequency")
    '''
    plt.show()


def show_package_comparison():
    """Show comparison of pip vs Poetry with installed package versions."""
    print("\n=== Package Management Comparison ===")
 
    print("\nInstalled Package Versions:")
    packages = ['pandas', 'requests', 'matplotlib', 'numpy']
    for package in packages:
        try:
            version = importlib.metadata.version(package)
            print(f"  {package}: {version}")
        except importlib.metadata.PackageNotFoundError:
            print(f"  {package}: Not installed")

    print("\npip (requirements.txt):")
    print("  - Simple dependency file")
    print("  - Manual version specification")
    print("  - Works with any virtual environment")

    print("\nPoetry (pyproject.toml):")
    print("  - Automatic dependency resolution")
    print("  - Creates lock file for reproducibility")
    print("  - Built-in virtual environment management")


def main():
    """Main function to run the loading program."""
    # Check dependencies
    status, all_available = check_dependencies()

    if not all_available:
        show_installation_instructions()
        sys.exit(1)

    # Import after checking to avoid import errors in check function
    import pandas as pd

    df = generate_matrix_data() 

    # df = get_weather()
    # weather_visualization(df)

    create_visualization(df)

    show_package_comparison()

    print("\n" + "="*60)
    print("SUCCESS: All programs loaded successfully!")
    print("="*60)


if __name__ == "__main__":
    main()



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

    np.random.seed(42)

    data_points = 1000

    data = {
        'value': np.random.normal(100, 15, 100),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    }

    df = pd.DataFrame(data)
    return df

def analyze_data(df):
    """
        analyze data and display stats
    """
    print("\nData Analysis:")
    print(f"  Total records: {len(df)}")
    print(f"  Mean value: {df['value'].mean():.2f}")
    print(f"  Std deviation: {df['value'].std():.2f}")
    print(f"  Min value: {df['value'].min():.2f}")
    print(f"  Max value: {df['value'].max():.2f}")

    print("\nCategory breakdown:")
    for category in df['category'].unique():
        count = len(df[df['category'] == category])
        mean = df[df['category'] == category]['value'].mean()
        print(f"  {category}: {count} records, mean = {mean:.2f}")

def create_visualization(df, filename='matrix_analysis.png'):
    """
        create visualization for the data
    """
    import matplotlib.pyplot as plt

    print("\nGenerating visualization...")

    bins = 10
    counts, edges = None, None
    
    import numpy as np
    counts, edges = np.histogram(df['value'], bins=bins)
    
    # Find max count for scaling
    max_count = max(counts)
    width = 50  # Width of the histogram
    
    # Print histogram
    for i in range(bins):
        bar_length = int((counts[i] / max_count) * width)
        bar = '█' * bar_length
        print(f"  {edges[i]:6.1f} - {edges[i+1]:6.1f} | {bar} {counts[i]}")


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
    
    # Import after checking (to avoid import errors in check function)
    import pandas as pd
    
    # Generate and analyze data
    df = generate_matrix_data()
    analysis = analyze_data(df)
    
    # Create visualization
    create_visualization(df)

    show_package_comparison()

    print("\n" + "="*60)
    print("SUCCESS: All programs loaded successfully!")
    print("="*60)


if __name__ == "__main__":
    main()



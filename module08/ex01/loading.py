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
            version = importlib.metadata.version(packages)
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
        'agant_id': [f'AGENT_{i:04d}' for i in range(data_points)],
        'reaction_time': np.random.normal(0.2, 0.05, data_points),
        'accuracy': np.random.beta(8, 2, data_points) * 100,
        'bullets_dodged': np.random.poisson(15, data_points),
        'missions_completed': np.random.randint(0, 50, data_points),
        'red_pill_score': np.random.gamma(2, 2, data_points) * 10
    }

    df = pd.DataFrame(data)
    return df

def analyze_data(df):
    """
        analyze data and display stats
    """
    print("\nAnalyzing Matrix data...")
    print(f"Processing {len(df)} data points...")

    analysis = {
        'total_agents': len(df),
        'avg_reaction_time': df['reaction_time'].mean(),
        'avg_accuracy': df['accuracy'].mean(),
        'total_bullets_dodged': df['bullets_dodged'].sum(),
        'avg_missions':df['missions_completed'].mean(),
        'top_perfomer': df.loc[df['red_pill_score'].idmax(), 'agant_id']
    }

    print(f"\nAnalysis Results:")
    print(f"Total Agents: {analysis['total_agants']}")
    print(f"  Average Reaction Time: {analysis['avg_reaction_time']:.3f}s")
    print(f"  Average Accuracy: {analysis['avg_accuracy']:.1f}%")
    print(f"  Total Bullets Dodged: {analysis['total_bullets_dodged']}")
    print(f"  Average Missions Completed: {analysis['avg_missions']:.1f}")
    print(f"  Top Performer: {analysis['top_performer']}")

    return analysis

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
        'top_performer': df.loc[df['red_pill_score'].idxmax(), 'agant_id']
    }

    print(f"\nAnalysis Results:")
    print(f"Total Agents: {analysis['total_agents']}")
    print(f"  Average Reaction Time: {analysis['avg_reaction_time']:.3f}s")
    print(f"  Average Accuracy: {analysis['avg_accuracy']:.1f}%")
    print(f"  Total Bullets Dodged: {analysis['total_bullets_dodged']}")
    print(f"  Average Missions Completed: {analysis['avg_missions']:.1f}")
    print(f"  Top Performer: {analysis['top_performer']}")

    return analysis

def create_visualization(df, filename='matrix_analysis.png'):
    """
        create visualization for the data
    """
    import matplotlib.pyplot as plt

    print("\nGenerating visualization...")

    #grid for the plots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Matrix Performance Analysis', fontsize=16, fontweight='bold')

    #plot1 reaction time
    axes[0, 0].hist(df['reaction_time'], bins=30, color='green', alpha=0.7, edgecolor='black')
    axes[0, 0].set_title('Reaction time distribution')
    axes[0, 0].set_xlabel('Reaction time in sec')
    axes[0, 0].set_ylabel('frequency')
    axes[0, 0].grid(True, alpha=0.3)

    #plot2 accurqcy vs missions
    scatter = axes[0, 1].scatter(df['missions_completed'], df['accuracy'],
                                 c=df['red_pill_score'], cmap='RdYlGn', alpha=0.6)
    axes[0, 1].set_title('Accuracy vs Missions Completed')
    axes[0, 1].set_xlabel('Missions Completed')
    axes[0, 1].set_ylabel('Accuracy (%)')
    axes[0, 1].grid(True, alpha=0.3)
    plt.colorbar(scatter, ax=axes[0, 1], label='Red Pill Score')
    
    # Plot 3: Bullets Dodged Distribution
    axes[1, 0].hist(df['bullets_dodged'], bins=25, color='red', alpha=0.7, edgecolor='black')
    axes[1, 0].set_title('Bullets Dodged Distribution')
    axes[1, 0].set_xlabel('Bullets Dodged')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Plot 4: Red Pill Score Distribution
    axes[1, 1].boxplot([df['red_pill_score']], labels=['Red Pill Score'])
    axes[1, 1].set_title('Red Pill Score Distribution')
    axes[1, 1].set_ylabel('Score')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"\nAnalysis complete!")
    print(f"Results saved to: {filename}")
    
    # Don't show the plot in non-interactive mode
    # plt.show()


def compare_package_managers():
    """Display comparison between pip and Poetry."""
    print("\n" + "="*60)
    print("PACKAGE MANAGEMENT COMPARISON")
    print("="*60)
    print("\npip (requirements.txt):")
    print("  ✓ Simple and widely used")
    print("  ✓ Works with virtualenv")
    print("  ✓ Direct dependency specification")
    print("  ✗ No automatic dependency resolution")
    print("  ✗ No lock file (without pip-tools)")
    print("  ✗ Manual virtual environment management")
    
    print("\nPoetry (pyproject.toml):")
    print("  ✓ Automatic dependency resolution")
    print("  ✓ Generates lock file (poetry.lock)")
    print("  ✓ Built-in virtual environment management")
    print("  ✓ Separates dev and production dependencies")
    print("  ✓ Build and publish packages easily")
    print("  ✗ Additional tool to install")
    print("  ✗ Learning curve for configuration")
    
    print("\nCurrent Environment:")
    # Detect if running in Poetry environment
    if sys.prefix != sys.base_prefix:
        print("  Running in virtual environment")
        if 'poetry' in sys.prefix.lower():
            print("  Managed by: Poetry")
        else:
            print("  Managed by: venv/virtualenv")
    else:
        print("  Running in global environment (not recommended!)")


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
    
    # Show package manager comparison
    compare_package_managers()
    
    print("\n" + "="*60)
    print("SUCCESS: All programs loaded successfully!")
    print("="*60)


if __name__ == "__main__":
    main()



import sys
import os
import site

def in_venv():
    """
        deteect wether script is running
        in a virtual environment
    """
    if os.environ.get('VIRTUAL_ENV'):
        return True

    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        return True

    return False

def get_venv_name():
    """
        get the name of the venv
    """
    venv_path = os.environ.get('VIRTUAL_ENV')
    if venv_path:
        return os.path.basename(venv_path)

    if hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix:
        return os.path.basename(sys.prefix)

    return None

def get_package_paths():
    """
        get site-packages dirs
        where packages are installed
    """
    return site.getsitepackages()

def display_outside_venv():
    print("\nMATRIX STATUS: You're still plugged in")

    print(f"\nCurrent Python: {sys.executable}")
    print("Virtual Environment: None detected")
    
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows")

    print("\nThen run this program again.")

def display_in_venv():
    venv_name = get_venv_name()
    venv_path = os.environ.get('VIRTUAL_ENV') or sys.prefix
    package_paths = get_package_paths()

    print("\nMATRIX STATUS: Welcome to the construct")

    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")

    if package_paths:
        print("\nPackage installation path:")
        print(f" {package_paths[0]}")

if __name__ == "__main__":

    if in_venv():
        display_in_venv()
    else:
        display_outside_venv()


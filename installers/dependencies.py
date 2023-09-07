import subprocess

def install_dependency(dependency):
    subprocess.call(["pip", "install", dependency])

def main():
    with open("requirements.txt", "r") as requirements_file:
        dependencies = requirements_file.read().splitlines()

    missing_dependencies = []

    for dependency in dependencies:
        try:
            __import__(dependency)
        except ImportError:
            missing_dependencies.append(dependency)

    if missing_dependencies:
        print("Missing dependencies:")
        for dependency in missing_dependencies:
            print(dependency)
            install_dependency(dependency)
    else:
        print("All dependencies are already installed.")

if __name__ == "__main__":
    main()

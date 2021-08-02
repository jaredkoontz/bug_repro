from bug_repro import __version__


def cli():
    """simply prints the value in __version__ which will match what is in pyproject.toml"""
    print(f"version {__version__}")

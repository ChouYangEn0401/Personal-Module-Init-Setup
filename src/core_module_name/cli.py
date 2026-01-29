"""
讓使用者安裝後可以：
<<<<<my_module_name>>>>> -V
<<<<<my_module_name>>>>> --version
"""
from ._version import __version__

def main():
    import argparse

    parser = argparse.ArgumentParser(description="<<<<<my_module_name>>>>> CLI")
    parser.add_argument("-V", "--version", action="store_true", help="Show version")
    args = parser.parse_args()

    if args.version:
        print(__version__)
        return

    print("<<<<<my_module_name>>>>> CLI running ...")

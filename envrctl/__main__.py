"""
envrctl - manage envrc and psenvrc files in a project
"""
import sys

if __name__ == "__main__":
    from .cli import envrctl

    sys.exit(envrctl())

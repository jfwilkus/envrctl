"""
Envrctl - manage envrc and psenvrc files in a project,
"""
import click

from envrctl.cli.initialize import init_envrctl
from envrctl.console import console
from envrctl.direnv import DirenvConfig
from envrctl.psenvrc import PsenvConfig

from ..__about__ import __version__


@click.group(no_args_is_help=True)
@click.version_option(version=__version__, prog_name="envrctl")
def envrctl():
    # editorconfig-checker-disable
    """
    \b
                              _   _
      ___ _ ____   ___ __ ___| |_| |
     / _ \\ '_ \\ \\ / / '__/ __| __| |
    |  __/ | | \\ V /| | | (__| |_| |
     \\___|_| |_|\\_/ |_|  \\___|\\__|_|
    """
    # editorconfig-checker-enable


def main():
    return envrctl()


@envrctl.command()
def generate():
    """Generate envrc files for direnv and posh-direnv."""
    psenvrc = PsenvConfig()
    direnv = DirenvConfig()
    psenvrc.save()
    console.print(f"Generated {psenvrc.path}")
    direnv.save()
    console.print(f"Generated {direnv.path}")


envrctl.add_command(init_envrctl)

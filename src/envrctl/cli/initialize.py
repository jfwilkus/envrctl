from pathlib import Path

import click

from envrctl.console import console
from envrctl.constants import ENVRCTL_CONFIG
from envrctl.contextmanager import write_file

# editorconfig-checker-disable
TEMPLATE = """
version: 1

vars:
  PYTHON_VERSION: '$(cat .python-version)'
  # RUBY_VERSION: '$(cat .ruby-version)'

# SECRET: gopass/path
secrets: {}

### direnv specific configuration

# Specify layouts for direnv
# https://direnv.net/man/direnv-stdlib.1.html#codelayout-lttypegtcode

layouts:
  - pyenv "${PYTHON_VERSION}"
  # - pipenv
  # - node
  # - go

# Uncomment to define any use statements for direnv
#uses:
#  - rbenv

# Should direnv load .env file
# https://direnv.net/man/direnv-stdlib.1.html#codedotenvifexists-ltdotenvpathgtcode
dotenv_if_exists: true
### TODO
# Manage .python-version file
#use_pyenv: true
#python: 3.10.5

# Manage .ruby-version file
#use_rbenv: true
#ruby: 3.1.2
""".strip()
# editorconfig-checker-enable


@click.command(name="init")
def init_envrctl():
    """Init envrctl for project."""
    rc = Path.cwd() / ENVRCTL_CONFIG
    with write_file(rc) as file:
        file.write(TEMPLATE)
    console.print(f":tada: Created {rc}")
    console.print(
        f":laptop_computer: Edit the ./{ENVRCTL_CONFIG} "
        + "then run [green]envrctl generate"
    )

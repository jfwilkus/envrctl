from pathlib import Path

import yaml
from jinja2 import BaseLoader, Environment

from envrctl.constants import ENVRCTL_CONFIG, SECRET_COMMAND
from envrctl.contextmanager import write_file


class EnvrctlConfig:
    def __init__(self) -> None:
        self.template = ""
        self.path = ""
        self.secret_command = SECRET_COMMAND

        with open(Path.cwd() / ENVRCTL_CONFIG) as f:
            self.__dict__.update(yaml.safe_load(f))

    def render(self):
        """Return a rendered template."""
        rt = Environment(loader=BaseLoader()).from_string(self.template)  # nosec B701
        return rt.render(self.__dict__)

    def save(self):
        with write_file(self.path) as file:
            file.write(self.render())

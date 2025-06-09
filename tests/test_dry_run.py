import os
import shutil
from typing import Callable

from tests.conftest import Dotfiles


def test_dry_run_create(home: str, dotfiles: Dotfiles, run_dotbot: Callable[..., None]) -> None:
    dotfiles.write_config([{"create": ["~/a"]}])
    run_dotbot("--dry-run")
    assert not os.path.isdir(os.path.join(home, "a"))


def test_dry_run_shell(home: str, dotfiles: Dotfiles, run_dotbot: Callable[..., None]) -> None:
    dotfiles.write_config([{"shell": ["touch ~/flag"]}])
    run_dotbot("--dry-run")
    assert not os.path.exists(os.path.join(home, "flag"))


def test_dry_run_third_party_plugin(home: str, dotfiles: Dotfiles, run_dotbot: Callable[..., None]) -> None:
    plugin_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dotbot_plugin_file.py")
    shutil.copy(plugin_file, os.path.join(dotfiles.directory, "file.py"))
    dotfiles.write_config([{"plugin_file": "~"}])
    run_dotbot("--dry-run", "--plugin", os.path.join(dotfiles.directory, "file.py"))
    assert not os.path.exists(os.path.join(home, "flag"))


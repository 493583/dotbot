from typing import Any

from dotbot.context import Context
from dotbot.messenger import Messenger


class Plugin:
    SUPPORTS_DRY_RUN = False
    """
    Abstract base class for commands that process directives.
    """

    def __init__(self, context: Context):
        self._context = context
        self._log = Messenger()
        self._dry_run = getattr(context.options(), "dry_run", False)

    def dry_run(self) -> bool:
        return self._dry_run

    def can_handle(self, directive: str) -> bool:
        """
        Returns true if the Plugin can handle the directive.
        """
        raise NotImplementedError

    def handle(self, directive: str, data: Any) -> bool:
        """
        Executes the directive.

        Returns true if the Plugin successfully handled the directive.
        """
        raise NotImplementedError

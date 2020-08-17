"""The dummy package."""
from .dummy_server import get_dummy_app, run_dummy_app
from .smarty_server import get_smarty_app, run_smarty_app

__all__ = [
    "get_dummy_app",
    "get_smarty_app",
    "run_dummy_app",
    "run_smarty_app",
]

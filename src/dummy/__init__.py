"""Dummy."""
import pkg_resources


def hello():
    """Say hello."""
    print("hello")


def get_message():
    """Load the message from file."""
    message = pkg_resources.resource_string(__name__, "resources/message.txt")
    return message.decode().strip()

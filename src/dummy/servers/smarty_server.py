"""The smarty webapp."""
import argparse
import secrets

from flask import Flask


def get_smarty_app():
    """Create the smarty webapp.

    Returns
    -------
    app : flask.Flask
        The flask app.
    """
    smarty_app = Flask("Smarty app")

    @smarty_app.route("/", methods=["GET", "POST"])
    def send_answer():
        number = secrets.randbelow(100)
        return f"Today's answer is: {number}\n"

    return smarty_app


def run_smarty_app(argv=None):
    """Run the smarty web app in the CLI development mode.

    Parameters
    ----------
    argv : list_like
        The command line arguments

    Returns
    -------
    int
        The exit code.
    """
    parser = argparse.ArgumentParser(usage="%(prog)s [options]")
    parser.add_argument("--debug", action="store_true", default=False)
    args = parser.parse_args(argv)

    if args:  # pragma: no cover
        smarty_app = get_smarty_app()
        smarty_app.run(host="localhost", port=8081, debug=args.debug)

    return 0  # pragma: no cover


if __name__ == "__main__":
    exit(run_smarty_app())

"""The dummy webapp."""
import argparse
import logging
import os
import textwrap

import requests
from flask import Flask


def get_dummy_app():
    """Create the dummy webapp.

    Returns
    -------
    app : flask.Flask
        The flask app.
    """
    app = Flask("My web app")
    logger = logging.getLogger("Dummy app")

    @app.route("/")
    def hello():
        logger.debug("GET /")
        secret = os.getenv("DUMMY_SECRET", "no secret found")
        page = f"""
        <head>
            <title>Dummy Web</title>
        </head>
        <body>
            <h1>Hello!</h1>
            <p>
                The secret was: {secret}
            </p>
            <p>
                Want to ask smarty? Click <a href="/ask_smarty">here!</a>
            </p>
        </body>
        """
        return textwrap.dedent(page)

    @app.route("/ask_smarty")
    def ask_smarty():
        logger.debug("GET /ask_smarty")

        smarty_host = os.getenv("SMARTY_HOST")
        smarty_port = os.getenv("SMARTY_PORT")
        logger.debug(f"SMARTY_HOST = {smarty_host}")
        logger.debug(f"SMARTY_PORT = {smarty_port}")

        if smarty_host is not None and smarty_port is not None:
            smarty_url = f"http://{smarty_host}:{smarty_port}"

            try:
                response = requests.get(smarty_url)
                if response.ok:
                    message = response.text
                else:
                    message = "Smarty sent a bad response"
            except requests.ConnectionError:
                message = f"Couldn't reach smarty at {smarty_url}"
        else:
            message = "Don't know how to contact smarty"

        page = f"""
        <head>
            <title>Dummy Web</title>
        </head>
        <body>
            <h1>Ask Smarty</h1>
            <p>
                Let's try and ask smarty: <br>
                &rarr; {message}
            </p>
            <p>
                To go back click <a href="/">here</a>.
            </p>
        </body>
        """

        return textwrap.dedent(page)

    return app


def run_dummy_app(argv=None):
    """Run the dummy web app in the CLI development mode.

    Parameters
    ----------
    argv : list_like
        The command line arguments

    Returns
    -------
    int
        The exit code.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(usage="%(prog)s [options]")
    parser.add_argument("--secret", type=int, default=42)
    parser.add_argument("--debug", action="store_true", default=False)
    args = parser.parse_args(argv)

    # Logging
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    if args:  # pragma: no cover
        # create_app reads the configuration from environment variables
        os.environ["DUMMY_SECRET"] = str(args.secret)

        app = get_dummy_app()
        app.run(host="localhost", port="8080", debug=args.debug)

    return 0  # pragma: no cover


if __name__ == "__main__":
    exit(run_dummy_app())

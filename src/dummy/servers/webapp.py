"""The dummy webapp."""
import argparse
import os
import textwrap

from flask import Flask


def create_app():
    """Create the dummy webapp.

    Returns
    -------
    app : flask.Flask
        The flask app.
    """
    app = Flask("My web app")

    @app.route("/")
    def hello():
        secret = os.getenv("DUMMY_SECRET", "no secret found")
        message = f"""
        <head>
            <title>Dummy Web</title>
        </head>
        <body>
            <h1>Hello!</h1>
            <p>
                The secret was: {secret}
            </p>
        </body>
        """
        return textwrap.dedent(message)

    return app


def run_my_web_app(argv=None):
    """Run the web app in the CLI development mode.

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

    # create_app reads the configuration from environment variables
    os.environ["DUMMY_SECRET"] = str(args.secret)

    app = create_app()
    app.run(host="localhost", port="8080", debug=args.debug)

    return 0


if __name__ == "__main__":
    exit(run_my_web_app())

import flask
import pytest

from dummy.servers import webapp


@pytest.fixture
def dummyweb_client():
    app = webapp.create_app()
    assert isinstance(app, flask.Flask)

    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_create_app(dummyweb_client):
    response = dummyweb_client.get("/")
    assert response.status_code == 200
    assert b"Hello!" in response.data


def test_help(capsys):
    with pytest.raises(SystemExit) as error:
        webapp.run_my_web_app(["--help"])
    stdout, stderr = capsys.readouterr()

    assert error.value.code == 0
    assert stdout.startswith("usage:")
    assert stderr == ""

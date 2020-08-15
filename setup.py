from setuptools import find_packages, setup

setup(
    name="dummy",
    version="0.0.1",
    package_dir={"": "src"},
    package_data={"dummy": ["resources/img.png", "resources/message.txt"]},
    packages=find_packages("src"),
    install_requires=["Flask", "gunicorn"],
    entry_points={"console_scripts": ["dummyweb=dummy.servers.webapp:run_my_web_app"]},
)

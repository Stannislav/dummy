from setuptools import find_packages, setup

setup(
    name="dummy",
    version="0.0.1",
    package_dir={"": "src"},
    package_data={"dummy": ["resources/img.png", "resources/message.txt"]},
    packages=find_packages("src"),
    install_requires=["Flask", "gunicorn", "requests"],
    extras_require={
        "tests": ["pytest", "pytest-cov"],
        "lint": ["bandit" "black" "flake8" "isort" "pydocstyle"],
    },
    entry_points={
        "console_scripts": [
            "dummyweb=dummy.servers:run_dummy_app",
            "smartyweb=dummy.servers:run_smarty_app",
        ]
    },
)

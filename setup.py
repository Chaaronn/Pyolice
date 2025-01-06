from setuptools import setup, find_packages

setup(
    name="Pyolice",
    version="0.1.0",
    description="A Python wrapper for the UK Police API.",
    author="Matt Voce",
    author_email="@mozmail.com",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    python_requires=">=3.7",
)

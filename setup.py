from setuptools import setup, find_packages

setup(
    name="Pyolice",
    version="0.1.0",
    description="A Python wrapper for the UK Police API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Matt Voce",
    author_email="@mozmail.com",
    url="https://github.com/Chaaronn/Pyolice",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
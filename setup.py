from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="maiker",
    version="0.0.2",
    author="Luis Sobrecueva",
    author_email="luis@sobrecueva.com",
    description="AI-powered code project generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lusob/maiker-cli",
    packages=["maiker"],
    entry_points={
        "console_scripts": [
            "maiker=maiker.cli:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "openai",
        "click",
    ],
)


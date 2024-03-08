import os

import pkg_resources
from setuptools import setup

setup(
    name="whisperx",
    version="3.1.1",
    description="Time-Accurate Automatic Speech Recognition using Whisper.",
    readme="README.md",
    python_requires=">=3.8",
    author="Max Bain",
    url="https://github.com/m-bain/whisperx",
    license="MIT",
    packages=["whisperx"],
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ]
    + [f"pyannote.audio==3.1.1"],
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)

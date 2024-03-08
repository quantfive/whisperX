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
        "torch>=2",
        "torchaudio>=2",
        "faster-whisper==1.0.0",
        "transformers",
        "pandas",
        "setuptools>=65",
        "nltk",
        "pyannote.audio==3.1.1"
    ],
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)

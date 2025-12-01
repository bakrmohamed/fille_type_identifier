from setuptools import setup, find_packages

setup(
    name="file-identifier",
    version="1.0.0",
    description="A simple file identification and analysis tool.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "python-magic",
    ],
    entry_points={
        "console_scripts": [
            "file-identifier=file_identifier:main",
        ]
    },
)

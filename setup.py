from setuptools import setup

setup(
    name="file-identifier",
    version="1.0.1",
    description="File signature inspection with an optional libmagic backend",
    py_modules=["fille_type_identifier"],
    extras_require={"magic": ["python-magic>=0.4.27,<0.5"]},
    entry_points={"console_scripts": ["file-identifier=fille_type_identifier:main"]},
)

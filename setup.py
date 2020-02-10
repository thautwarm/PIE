from setuptools import setup, find_packages
from datetime import datetime
from pathlib import Path

with Path('README.md').open() as readme:
    readme = readme.read()

version = 0.1

setup(
    name='painless-import-extension',
    version=version if isinstance(version, str) else str(version),
    keywords="",
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    license='mit',
    python_requires='>=3',
    url='https://github.com/thautawarm/PIE',
    author='thautawarm',
    author_email='twshere@outlook.com',
    packages=find_packages(),
    entry_points={"console_scripts": []},
    install_requires=["devpackage"],
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)

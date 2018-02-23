
from setuptools import setup, find_packages
setup(
    name="helloworld",
    version="0.1",
    packages=find_packages(),
    author="Cecilia Sena",
    license="GPLv3",
    description="A package for saying hello and making some major life choices",
    entry_points={
        'console_scripts': ['helloworld = helloworld.__main__:main'],
        },
    classifiers=["Programming Language :: Python :: 3"],
)
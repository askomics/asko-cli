from setuptools import setup, find_packages

from os import listdir

setup(
    name="askocli",
    version='0.2',
    description="Command line interface for a distant AskOmics",
    author="Xavier Garnier",
    author_email="xavier.garnier@irisa.fr",
    url="https://github.com/xgaia/asko-cli",
    install_requires=['requests>=2.4.3'],
    packages=find_packages(),
    license='AGPL',
    platforms="Posix; MacOS X; Windows",
    scripts=['bin/' + f for f in listdir('bin')],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: AGPL License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3"
    ])

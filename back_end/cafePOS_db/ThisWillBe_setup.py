# ==========================================
#     DEVELOPER:  J.A. Runnells
#          FILE:  setup.py
#        BRANCH: main
# ==========================================
from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
    name=None,
    version=None,
    description=None,
    license="MIT",
    long_description=long_description,
    author="J.A. Runnells",
    author_email="jason@mztechsolutions.com",
    url="https://mzTechSolutions.com/",
    packages=[None],  # same as name
    install_requires=[None, None],  # external packages as dependencies
    scripts=[
        None,
        None,
    ]
)

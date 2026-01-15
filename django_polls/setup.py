
import os
from setuptools import find_packages, setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="django_polls",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    description="A simple Django app to conduct web-based polls.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/bdeery002/Code",  # Update if needed
    author="Your Name",
    author_email="your.email@example.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)

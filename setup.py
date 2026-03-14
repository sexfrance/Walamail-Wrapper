from setuptools import setup, find_packages

setup(
    name="walamail",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    author="WalaMail",
    description="Python API Wrapper for WalaMail",
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/walamail/wrapper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

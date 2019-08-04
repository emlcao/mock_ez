import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mock_ez",
    version="0.0.1",
    author="Linh Cao",
    author_email="linhctd8@gmail.com",
    description="A small example package for testing mock",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emlcao/mock_ez",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

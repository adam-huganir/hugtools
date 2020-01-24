import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hugtools", # Replace with your own username
    version="0.0.1",
    author="Adam Huganir",
    author_email="adam@huganir.com",
    description="fun tools from a fun guy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://hugtools.huganir.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geokrety-jsonapi-client-proto",
    version="0.0.1",
    author="Mathieu Alorent",
    author_email="kumy@geokrety.org",
    description="GeoKrety JSONAPI prototype",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geokrety/geokrety-jsonapi-client-proto",
    packages=setuptools.find_packages(),
    install_requires=[
        "jsonapi-requests==0.6.0",
        "Flask==1.0.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

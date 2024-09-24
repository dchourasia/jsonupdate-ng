import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsonupdate-ng",
    version="1.0.2",
    author="Deepak Chourasia",
    author_email="deepak.chourasia@gmail.com",
    description="A Next Generation Library to update any json document",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.sas.com/sindec/rf-rest",
    project_urls={
        "Bug Tracker": "https://gitlab.sas.com/sindec/jsonupdate-ng",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Software Development :: Testing",
        "Development Status :: 5 - Production/Stable"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.5.2",
)
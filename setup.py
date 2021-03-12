import setuptools

with open("./README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="decomp-framework",
    version="0.0.2",
    author="M4xw",
    author_email="m4x@m4xw.net",
    description="N64 Reverse Engineering Toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/N64RET/decomp-framework",
    project_urls={
        "Bug Tracker": "https://github.com/N64RET/decomp-framework/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
    ],
    install_requires=["cstruct", "Mako", "MarkupSafe"],
    packages=setuptools.find_packages(),
    python_requires=">=3.0",
)

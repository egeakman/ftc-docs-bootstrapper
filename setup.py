from setuptools import find_packages, setup

version = "0.1.0"

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ftc-docs-bootstrapper",
    author="egeakman",
    author_email="me@egeakman.dev",
    url="https://github.com/egeakman/ftc-docs-bootstrapper",
    description="Bootstrapper for FTC documentation translations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=version,
    license="MIT",
    download_url=f"https://github.com/egeakman/ftc-docs-bootstrapper/archive/{version}.tar.gz",
    packages=find_packages(where="."),
    install_requires=["sphinx==4.4.0"],
    include_package_data=True,
    package_data={
        "bootstrapper": ["data/.gitignore", "data/Makefile", "data/README.md"]
    },
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "bootstrapper=bootstrapper.bootstrapper:main",
        ]
    },
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
    ],
    keywords=[
        "documentation",
        "translation",
        "sphinx",
        "i18n",
        "ftc-docs",
        "CLI",
        "automation",
        "utilities",
    ],
    project_urls={
        "Homepage": "https://github.com/egeakman/ftc-docs-bootstrapper",
        "Issues": "https://github.com/egeakman/ftc-docs-bootstrapper/issues",
    },
)
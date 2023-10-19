# ftc-docs-bootstrapper

This repository contains the scripts and data used to bootstrap a new translation of the FIRST Tech Challenge documentation.

## Installation

```bash
$ pip install ftc-docs-bootstrapper
```

## Usage

```bash
$ bootstrapper --help
usage: bootstrapper [-h] [-b BRANCH] language

positional arguments:
  language              IETF language tag (e.g. tr, pt-br)

options:
  -h, --help            show this help message and exit
  -b BRANCH, --branch BRANCH
                        ftcdocs branch (e.g. main)
```

## Example

```bash
$ bootstrapper tr --branch main
```

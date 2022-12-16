# envrctl

This tool is only helpful if you need to keep `direnv` and `posh-direnv`
configuration files in sync.

## Table of Contents

- [Installation](#installation)

## Features

- Single configuration file to manage both `direnv` and `posh-direnv`

## Installation

```console
pip install git+https://github.com/jfwilkus/envrctl.git@main
```

Or add it to your `requirements.txt`:

```text
envrctl @ git+https://github.com/jfwilkus/envrctl.git@main

```

## Usage

### Initialize project for envrctl

```console
envrctl init
```

### Edit Configuration

Edit the `.envrctl.yml` file.

```yaml
version: 1
secrets:
  SUPERSECRET: batcave/pin
vars:
  PYTHON_VERSION: 3.10.5
```

### Generate envrc and psenvc files

```console
envrctl generate
```

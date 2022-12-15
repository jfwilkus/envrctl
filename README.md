# envrctl

## Table of Contents

- [Installation](#installation)

## Installation

```console
pip install github.com:jfwilkus/envrctl.git
```

## Usage

### Generate envrc and psenvc files

```console
envrctl generate
```

### Edit Configuration

```yaml
version: 1
secrets:
  SUPERSECRET: batcave/pin
vars:
  PYTHON_VERSION: 3.10.5
```

### Create envrc files

```console
envrctl create
```

<!-- vale off -->

# envrctl

<!-- vale on -->

This tool is helpful if you need to keep `direnv` and `posh-direnv`
configuration files in sync.

## Table of contents

<!-- toc -->

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Initialize project](#initialize-project)
  - [Edit configuration](#edit-configuration)
  - [Generate configuration files](#generate-configuration-files)

<!-- tocstop -->

## Features

- Single configuration file to manage both `direnv` and `posh-direnv`

## Requirements

- `gopass>=1.15`

## Installation

```console
pip install git+https://github.com/jfwilkus/envrctl.git@main
```

Or add it to your `requirements.txt`:

```text
envrctl @ git+https://github.com/jfwilkus/envrctl.git@main
```

## Usage

### Initialize project

```console
envrctl init
```

### Edit configuration

Edit the `.envrctl.yml` file.

```yaml
version: 1
secrets:
  SUPERSECRET: batcave/pin
vars:
  PYTHON_VERSION: 3.10.5
```

### Generate configuration files

```console
envrctl generate
```

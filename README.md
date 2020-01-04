# Fedora Sample JSON Schema Plugin

## Overview

This is designed to work with the Fedora publisher and listener I made earlier (https://github.com/ethanparab/fedora-publisher-listener). It is a JSON schema package for the messaging system.

## Installation

Follow the instructions to install the Fedora publisher and listener in another repository (https://github.com/ethanparab/fedora-publisher-listener/blob/master/README.md). Once that is done, return here.

Enter the directory you would like this repository to be cloned to. Replace "/this/is/a/path" with the path to the desired directory. Continue to clone to repository.
```sh
    cd /this/is/a/path
    git clone https://github.com/ethanparab/fedora-sample-scheme-plugin.git
```

Enter the directory.
```sh
    cd fedora-sample-schema-plugin
```

Set up the schema.
```sh
  $ python3 schema_package/setup.py develop
```
## Usage

Start the listener from the previous repository. Refer to (https://github.com/ethanparab/fedora-publisher-listener/blob/master/README.md) for instructions.

Start the new publisher prepped to use the new schema in another terminal. The old publisher can, if edited, use the new schema, if that is desired, but instructions are only given for the one provided.
```sh
    cd /this/is/a/path/fedora-sample-schema-plugin
    python3 publish.py
```

A sample message should appear in the listener. If not, ensure the RabbitMQ server is online and the schema was installed correctly.

## Credits

This schema was made using code and documentation from Fedora.

## License

This repository is licensed under GNU Affero General Public License v3. This is included in the file named LICENSE.

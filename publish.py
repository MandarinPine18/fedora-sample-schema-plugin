#!/usr/bin/env python3

from fedora_messaging.api import publish
from fedora_messaging.config import conf
from mailman_schema.schema import MessageV3 as Message

conf.setup_logging()
message= Message(
    topic="tutorial.topic",
    body={
        "owner": "demonstration user",
        "package": {
            "name": "package to demo sample message schema",
            "version": "3.0",
        }
    }
)
publish(message)

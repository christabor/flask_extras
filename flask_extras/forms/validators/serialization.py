"""Validators for various serialization formats."""

import json


def valid_json(formcls, field):
    """Validate field data as a json.

    :param formcls (object): The form class.
    :param field (str): The list of ips.
    """
    json.loads(field.data)

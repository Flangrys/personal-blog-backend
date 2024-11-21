import re

from django.core import exceptions, validators

NICKNAME_PATTERN = re.compile(r"^@([a-zA-Z0-9])+(.?[a-zA-Z0-9])*(.blog)$")


def nickname_validation(text) -> bool:

    if not isinstance(text, str):
        raise exceptions.ValidationError("invalid nickname input")

    if not NICKNAME_PATTERN.findall(text):
        raise exceptions.ValidationError("invalid nickname format")

    return True

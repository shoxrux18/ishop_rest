from django.utils.translation import get_language
from django.conf import settings
from django.db import models


def i18n(cls):
    if not issubclass(cls, models.Model):
        return cls

    codes = set(row[0] for row in settings.LANGUAGES)

    for field in cls._meta.fields:
        suffix = field.name[-3:]
        if not suffix.startswith("_") or suffix[1:] not in codes:
            continue

        property_name = field.name[:-3]
        setattr(cls, property_name, property(lambda self: getattr(self, f"{property_name}_{get_language()}")))

    return cls
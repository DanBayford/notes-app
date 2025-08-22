from enum import Enum


class AppThemeEnum(Enum):
    LIGHT = "Light"
    DARK = "Dark"
    SYSTEM = "System"

    @classmethod
    def choices(cls):
        return [(cs.name, cs.value) for cs in cls]


class AppFontEnum(Enum):
    SANS = "Sans"
    SERIF = "Serif"
    MONO = "Mono"

    @classmethod
    def choices(cls):
        return [(cs.name, cs.value) for cs in cls]

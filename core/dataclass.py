from dataclasses import dataclass, field

from core.enums import Countries, LanguageLevels

@dataclass
class User:
    name: str = field(default="Janez Novak")
    age: int = field(default=45)
    country: Countries = field(default=Countries.SLO)
    language_1: bool = field(default=True)
    language_1_level: LanguageLevels = field(default=LanguageLevels.MIGHTLY_FIELDS)
    language_2: bool = field(default=True)
    language_2_level: LanguageLevels = field(default=LanguageLevels.MIGHTLY_FIELDS)
from enum import Enum

class Countries(Enum):
    """ For all countries available in the form. """

    SLO = 'Slovenija'
    ITA = 'Italija'
    AVS = 'Austrija'
    HRV = 'Hrvaška'
    MAD = 'Madžarska'


class LanguageLevels(Enum):
    """ For all languages levels available in the form. """
    
    B1 = 'B1'
    A1 = 'A1'
    MIGHTLY_FIELDS = 'UltraMega'
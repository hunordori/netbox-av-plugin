"""
Defines the various choices to be used by the models, forms, and other plugin specifics.
"""

from utilities.choices import ChoiceSet

__all__ = (
    "MediumChoices",
    "VideoSignalRateChoices",
    "SignalTypeChoices",
    "SignalDirectionChoices",
)

class MediumChoices(ChoiceSet):
    CHOICES = [
        ('SDI', 'SDI'),
        ('HDMI', 'HDMI'),
        ('VGA', 'VGA'),
        ('DVI', 'DVI'),
        ('DP', 'Display Port'),
        ('XLR3', 'XLR 3-pin'),
        ('XLR4', 'XLR 4-pin'),
        ('BNC', 'BNC'),
    ]
class VideoSignalRateChoices(ChoiceSet):
    CHOICES = [
        ('SDI15GLVLA', 'SDI 1.5G Level A'),
        ('SDI3GLVLA', 'SDI 3G Level A'),
        ('SDI6GLVLA', 'SDI 6G Level A'),
        ('SDI12GLVLA', 'SDI 12G Level A'),
        ('SDI15GLVLB', 'SDI 1.5G Level B'),
        ('SDI3GLVLB', 'SDI 3G Level B'),
        ('SDI6GLVLB', 'SDI 6G Level B'),
        ('SDI12GLVLB', 'SDI 12G Level B'),
        ('HDMI12', 'HDMI 1.2'),
        ('HDMI14', 'HDMI 1.4'),
        ('HDMI20', 'HDMI 2.0'),
        ('DP12', 'Display Port 1.2'),
        ('DP14', 'Display Port 1.4'),
        ('DP2', 'Display Port 2.0'),
        ('RCA', 'RCA'),
        ('COAX', 'Coax'),
    ]

class SignalTypeChoices(ChoiceSet):
    CHOICES = [
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('video_audio', 'Video and Audio'),
        ('genlock', 'Genlock'),
        ('timecode', 'Timecode'),
        ('data', 'Data'),
    ]

class SignalDirectionChoices(ChoiceSet):
    CHOICES = [
        ('input', 'Input'),
        ('output', 'Output'),
        ('configurable', 'Configurable'),
    ]


import _settings
from abjad import *
from calliope.bubbles import *
from base import Neon
from intro import *

class Intro(GridSequence, Neon):
    grid_sequence = (Intro1, Intro2, Intro3)

class NeonMusic(GridSequence, Neon):
    grid_sequence = (Intro, )
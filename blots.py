import _settings
from abjad import *
from calliope.bubbles import *


# These blots are little fragments of lines that are combined and re-configured throughout 
# ... they generally "add up" vertially to a cluster of 5 notes

class BlotDrill1(MultiLine):
    voice1 = Line("d'4")
    voice2 = Line("b8([ a)]")

# TO DO... can we make this reverse automatically???
class BlotDrill2(BlotDrill1):
    voice2 = Line("a8([ b)]")

class Blot1(Line):
    music = BubbleMaterial("neon.blots.1")

class Blot2(MultiLine):
    a = Line("s4 d'4")
    b = BubbleMaterial("neon.blots.2")

class Blot3(MultiLine):
    a = Line("d'4 s4")
    b = BubbleMaterial("neon.blots.3")

class Blot4(Line):
    music = BubbleMaterial("neon.blots.4")
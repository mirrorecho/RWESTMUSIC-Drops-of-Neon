import settings
from abjad import *
from calliope.bubbles import *


# These blots are little fragments of lines that are combined and re-configured throughout 
# ... they generally "add up" vertially to a cluster of 5 notes

# TO DO... multiple voices for these blots doesn't work right...
class Blot1(Line):
    music = """e'8( c' e' b) <<
    {
        \\voiceOne
        d'4
      }
      \\new Voice {
        \\voiceTwo
        \\stemDown
        a8([ b)]
      }
    >>
    \\oneVoice
    r4"""

class Blot2(Line):
    music = "c'8( a4 c'8)"

class Blot3(Line):
    music = "c'8( a4 c'8)"

class Blot4(Line):
    music = "c'8( a4 c'8)"
import settings
from abjad import *
from calliope.bubbles import *
from blots import *

class NeonScore(BubbleScore):
    violin1 = BubbleStaff(instrument=instrumenttools.Violin(instrument_name="Violin 1", short_instrument_name="vln.1"))
    violin2 = BubbleStaff(instrument=instrumenttools.Violin(instrument_name="Violin 2", short_instrument_name="vln.2"))
    viola = BubbleStaff(instrument=instrumenttools.Viola(instrument_name="Viola", short_instrument_name="vla."), clef="alto")
    cello = BubbleStaff(instrument=instrumenttools.Cello(instrument_name="Cello", short_instrument_name="vc."), clef="bass") 
    sequence = ("violin1", "violin2", "viola", "cello")

class Neon(Bubble):
    violin1 = Placeholder()
    violin2 = Placeholder()
    viola = Placeholder()
    cello = Placeholder()

class Intro1(Neon):
    violin1 = Line("r1\\fermata")
    violin2 = violin1
    viola = violin1
    cello = Line('a1\\fermata ^"sul tasto"')

class Intro2(Intro1):
    cello = Line("a1\\fermata")

class Intro3(Neon):
    violin1 = Line("r2 r4 r4\\fermata | R1 | R1 |")
    violin2 = violin1
    viola = Line("a8( b) r4 r4 r4\\fermata | r8( b c'[ a]) r2 | R1")
    cello = Line('b8(^"lightly" a) a2 r4\\fermata | b8( a4 b8) a2~ | a2 r2 ')


class Intro4(Neon):
    violin1 = Blot1()
    cello = Blot1() + Blot1()

class Intro(GridSequence, Neon):
    grid_sequence = (Intro1, Intro2, Intro3, Intro4)

class NeonMusic(GridSequence, Neon):
    grid_sequence = (Intro, )


score = NeonScore( NeonMusic() )
score.make_pdf()
print(score)



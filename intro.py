import _settings
from abjad import *
from calliope.bubbles import *
from blots import *
from base import Neon

class CelloIntroCresc(SimulLine):
    commands=(
        ("once \\override Script.outside-staff-priority = #50", "before"),
        ("override Hairpin.minimum-length = #12", "before"),
        ("override Hairpin.minimum-length = #4", "after"),
        )
    line = Line("a1\\fermata a1\\fermata", instruction="sul tasto")
    dynamics = Line("s2\\ppp  s4..\\mp   s16  |  s2...\\ppp  s16")
    sequence = ("line", "dynamics")
    def after_music(self, music, **kwargs):
        cresc = spannertools.Crescendo(include_rests=True)
        attach(cresc, music[1].select_leaves()[0:2] )
        decresc = spannertools.Decrescendo(include_rests=True)
        attach(decresc, music[1].select_leaves()[1:3] )
        cresc = spannertools.Crescendo(include_rests=True)
        attach(cresc, music[1].select_leaves()[3:] )

class Intro1(Neon):
    violin1 = BubbleMaterial("intro.violins")
    violin2 = violin1
    viola = BubbleMaterial("intro.viola")
    cello = CelloIntroCresc() + Line("b8( a) a2 r4\\fermata", instruction="lightly", dynamic="pp")

class Intro2(Neon):
    violin1 = Line("R1*5")
    violin2 = Line("R1*2") + Blot1(instruction="sul tasto, lightly", dynamic="pp") + Line("r2 | R1")
    viola = Line("R1*2") + Blot2() + Line("b2 ~ | b2 r2")
    cello = Line("b8( a4 b8) a2 ~ | a2 r2") + Blot3() + Line("a2 ~ | a2 r2")

class Intro3(Neon):
    violin1 = Line("r4 e' \\pp r") + BlotDrill1() + Line("e'8( c') r4 r2") + Blot1() + BlotDrill2() + Line("r4")
    violin2 = BlotDrill1() + Line("r4 r2") + BlotDrill1() + BlotDrill1() + Line("r4 e'4") + Blot2() + Line("r2") + Blot2() + Line("c'8( a) r4")
    viola = Line("a8( c') b2 r4 | a8([ c')] a([ c')] r4 a8( b)") + Blot3() + Line("r2") + Blot3() + Line("b8( e') r4")
    cello = Line("c'8( b) r2 r4 | c'8([ b)] c'([ b)] a4 c'") + Blot4() + Line("a4-- r4") + Blot4() + Line("e'8( c') r4")

# class Intro1(Neon):
#     pass
    # violin1 = Blot1() + Line("r2") + Line("R1")
    # violin2 = Blot2() + Line("r2")
    # viola = Blot3() + Line("r2")
    # cello = Blot4() + Line("r2")
    # cello = Blot1() + Blot1()

# class Intro2(Neon):

#     violin1 = Blot1() + Line("r2") + Line("R1")
#     violin2 = Blot2() + Line("r2")
#     viola = Blot3() + Line("r2")
#     cello = Blot4() + Line("r2")
#     # cello = Blot1() + Blot1()

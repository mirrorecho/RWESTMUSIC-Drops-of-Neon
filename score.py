import _settings
from abjad import *
from calliope.bubbles import *
from form import NeonMusic

class NeonScore(BubbleScore):
    violin1 = BubbleStaff(instrument=instrumenttools.Violin(instrument_name="Violin 1", short_instrument_name="vln.1"))
    violin2 = BubbleStaff(instrument=instrumenttools.Violin(instrument_name="Violin 2", short_instrument_name="vln.2"))
    viola = BubbleStaff(instrument=instrumenttools.Viola(instrument_name="Viola", short_instrument_name="vla."), clef="alto")
    cello = BubbleStaff(instrument=instrumenttools.Cello(instrument_name="Cello", short_instrument_name="vc."), clef="bass") 
    sequence = ("violin1", "violin2", "viola", "cello")

music = NeonMusic()
score = NeonScore( music )

score.make_pdf()
# print(score)
# print( format(music.blow_bubble("violin1")) )
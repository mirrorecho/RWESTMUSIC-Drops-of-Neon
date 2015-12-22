from abjad import *


# c = Container()
# c.is_simultaneous = True

# c1 = Container("r4 r4 r4 r4")
# c2 = Container("b4 b4 b4 b4")

# c.append(c1)
# c.append(c2)

# print(c.select_leaves(allow_discontiguous_leaves=True))

c = Container("b4 << {b2} \\\\  {\\voiceTwo a8([ c8]) r4} >> r4")

s = Staff()
s.append(c)

show(s)
print(format(s))

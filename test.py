from abjad import *
import ly.document

ly_string = ""

with open ("test.ly", "r") as ly_file:
    ly_string = ly_file.read()

d = ly.document.Document(ly_string)

print(d.block("ya").text())

# l = ly_string.split("=")

# for i, x in enumerate(l):
#     if i % 2 == 0:
#         print(i)
#         print(x)


# print(l)


# c = Container()
# c.is_simultaneous = True

# c1 = Container("r4 r4 r4 r4")
# c2 = Container("b4 b4 b4 b4")

# c.append(c1)
# c.append(c2)

# print(c.select_leaves(allow_discontiguous_leaves=True))

# c = Container("b4 << {b2} \\\\  {\\voiceTwo a8([ c8]) r4} >> r4")

# s = Staff()
# s.append(c)

# show(s)
# print(format(s))

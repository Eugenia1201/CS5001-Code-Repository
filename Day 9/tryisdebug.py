"""try detecting debuggin"""


import sys
gettrace = getattr(sys, "gettrace")
print(gettrace() is not None)
print(gettrace is not None)

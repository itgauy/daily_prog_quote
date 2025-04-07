# Author: Lian T. (itgauy)
# Date: 2025-04-05

# Quote: I can fix the world, but they won't give me the source code.

x = "I can fix the world"
y = "but they won't give me the source code"
z = "\n"


def fix_the_world():
  return x + ",\n" + y + "."

def style():
  i = 0
  while i < 5:
    print(z)
    i += 1

style()
print(fix_the_world())
style()
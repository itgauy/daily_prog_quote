# Author: Lian T. (itgauy)
# Date: 2025-04-06

# Quote: A strange game. The only winning move is not to play.

a = "The only winning move is"
s = "not to play"
c = "."
ii = "\n"

def void():
  i = 0
  while i < 5:
    print(ii)
    i += 1

secret = [115, 116, 114, 97, 110, 103, 101, 32, 103, 97, 109, 101]
o = ''.join(chr(num) for num in secret)

void()
print('A ' + o + c + ii + ii + a + ii + s + c)
void()
from ebook_to_string import *
import math
livros = epub2text('1984.epub')
#98 caracteres/linha
out =livros[1].splitlines()
print(out[14])

lines = math.floor((len(out[14])/98))
print(lines)
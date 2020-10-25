from ebook_to_string import *

livros = epub2text('1984.epub')
print(repr(livros[1][0:200]))
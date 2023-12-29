from package.all_words import all_words
from package.possible_words import all_possible
from package.wordle_functions_copy2 import *

import random, sys


#colors
from rich import print as rprint #source https://github.com/Textualize/rich
from rich.console import Console
console = Console()
from rich.color import Color
from rich.style import Style
right_style = Style(color="green", bold=True)
mid_style = Style(color="yellow", bold=True)
wrong_style = Style(bold=True)
from rich.text import Text, TextType

#source for ascii words https://ascii-generator.site/t/ bubble font
#source for ascii boxes https://textik.com/


print("""
      / \  / \  / \  / \  / \  / \ 
     ( w )( o )( r )( d )( l )( e )
      \_/  \_/  \_/  \_/  \_/  \_/

    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+

I'm thinking of a word. Can you guess it?
If your letter is correct and in the right spot,
it will show up green!
If your letter is in the word but not in the 
right location,
it will show up yellow!
If your letter is not in my word, 
it will stay neutral.
 """)
answer = choose_answer(all_possible)

# rprint(answer)
#I have to leave this in because the colors aren't working

guess(all_words, answer)
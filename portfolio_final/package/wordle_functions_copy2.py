import random, sys
from rich import print as rprint
from rich import inspect
from rich.console import Console

from rich.color import Color
from rich.style import Style
# from rich.theme import Theme
# wordle_theme = Theme({
#     "right": "bold green",
#     "mid": "bold yellow",
#     "default": "bold"
# })
console = Console()
right_style = Style(color="green", bold=True)
mid_style = Style(color="yellow", bold=True)
default_style = Style(bold=True)
wrong_style = Style(strike=True)
from rich.text import Text
from rich.markup import escape

alphabet = Text("ABCDEFGHIJKLMNOPQRSTUV", style=default_style)

def choose_answer(list):
    answer = random.choice(list)
    # answer = Text(answer, style=right_style)
    return answer

def guess(word_list, answer):
    global alphabet
    #each potential character gets its own empty var
    a1 = Text(" ")
    a2 = Text(" ")
    a3 = Text(" ")
    a4 = Text(" ")
    a5 = Text(" ")
    b1 = Text(" ")
    b2 = Text(" ")
    b3 = Text(" ")
    b4 = Text(" ")
    b5 = Text(" ")
    c1 = Text(" ")
    c2 = Text(" ")
    c3 = Text(" ")
    c4 = Text(" ")
    c5 = Text(" ")
    d1 = Text(" ")
    d2 = Text(" ")
    d3 = Text(" ")
    d4 = Text(" ")
    d5 = Text(" ")
    e1 = Text(" ")
    e2 = Text(" ")
    e3 = Text(" ")
    e4 = Text(" ")
    e5 = Text(" ")
    f1 = Text(" ")
    f2 = Text(" ")
    f3 = Text(" ")
    f4 = Text(" ")
    f5 = Text(" ")
    #split those vars into turns
    turn_1 = [a1, a2, a3, a4, a5]
    turn_2 = [b1, b2, b3, b4, b5]
    turn_3 = [c1, c2, c3, c4, c5]
    turn_4 = [d1, d2, d3, d4, d5]
    turn_5 = [e1, e2, e3, e4, e5]
    turn_6 = [f1, f2, f3, f4, f5]
    #master list of turns to iterate through
    turn_list = [turn_1, turn_2, turn_3, turn_4, turn_5, turn_6]

    for i in range(len(turn_list)): #max num of turns
        turn = turn_list[i]
        
        guess = input("\nType a 5-letter word and hit enter!\n\n")

        if guess not in word_list:
            rprint("Sorry, I don't know that word. This guess did not count.\n")
            guess = input("\nType a 5-letter word and hit enter!\n\n")
        
        #i copied this from a youtube video to make it prettier
        #link https://youtu.be/NCgN4qtbh2Q 18:23
        sys.stdout.write("\x1b[1A")
        sys.stdout.write("\x1b[2K")
        
        
        for x in range(len(answer)):
            if guess[x] == answer[x]:
                turn[x] = Text(guess[x], style=right_style)
                
                
                
            elif guess[x] in answer:
                turn[x] = Text(guess[x], style=mid_style) #what about doubles?

            else:
                turn[x] = Text(guess[x], style=default_style)
            
        
        #turns out the rich print function renders Text() objects as plain old strings so my friend Mike helped me make this other list of lists.

        printed_rows = [

# Opening lines
[
"""
  / \  / \  / \  / \  / \  / \ 
 ( w )( o )( r )( d )( l )( e )
  \_/  \_/  \_/  \_/  \_/  \_/

"""
], 

# BEGIN CYCLE

# 1st row of cycle
[
"""
+-----+-----+-----+-----+-----+
|     |     |     |     |     |
"""
],

# 2nd row of cycle (is a whole list instead of a single big string)
[
"""| """, turn_1[0],""" | """, turn_1[1],""" | """, turn_1[2],""" | """, turn_1[3],""" | """, turn_1[4], """ |
"""
],

# 3rd row of cycle
[
"""|     |     |     |     |     |
"""
],
[
"""+-----+-----+-----+-----+-----+
|     |     |     |     |     |
"""
],
[
"""| """, turn_2[0],""" | """, turn_2[1],""" | """, turn_2[2],""" | """, turn_2[3],""" | """, turn_2[4], """ |
"""
],
[
"""|     |     |     |     |     |
"""
],
[
"""+-----+-----+-----+-----+-----+
|     |     |     |     |     |
"""
],
[
"""| """, turn_3[0],""" | """, turn_3[1],""" | """, turn_3[2],""" | """, turn_3[3],""" | """, turn_3[4], """ |
"""
],
[
"""|     |     |     |     |     |
"""
],
[
"""+-----+-----+-----+-----+-----+
|     |     |     |     |     |
"""
],
[
"""| """, turn_4[0],""" | """, turn_4[1],""" | """, turn_4[2],""" | """, turn_4[3],""" | """, turn_4[4], """ |
"""
],
[
"""|     |     |     |     |     |
"""
],
[
"""+-----+-----+-----+-----+-----+
|     |     |     |     |     |
"""
],
[
"""| """, turn_5[0],""" | """, turn_5[1],""" | """, turn_5[2],""" | """, turn_5[3],""" | """, turn_5[4], """ |
"""
],
[
"""|     |     |     |     |     |
"""
],
[
"""+-----+-----+-----+-----+-----+
|     |     |     |     |     |
"""
],
[
"""| """, turn_6[0],""" | """, turn_6[1],""" | """, turn_6[2],""" | """, turn_6[3],""" | """, turn_6[4], """ |
"""
],
[
"""|     |     |     |     |     |
"""
],
[
"""+-----+-----+-----+-----+-----+
"""
]
]
        for row in printed_rows:
            rprint(*row, end="")

        if guess == answer:
            rprint(f"YOU WIN!!! The word was: {answer.upper()}!\n\n")
            return
    rprint(f"YOU LOSE. The word was: {answer.upper()}")
    return

#oh god i minimized this and idek what it is anymore
    print(f"""
      / \  / \  / \  / \  / \  / \ 
     ( w )( o )( r )( d )( l )( e )
      \_/  \_/  \_/  \_/  \_/  \_/

    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |  {a1}  |  {a2}  |  {a3}  |  {a4}  |  {a5}  |
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |  {b1}  |  {b2}  |  {b3}  |  {b4}  |  {b5}  |
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |  {c1}  |  {c2}  |  {c3}  |  {c4}  |  {c5}  |
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |  {d1}  |  {d2}  |  {d3}  |  {d4}  |  {d5}  |
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |  {e1}  |  {e2}  |  {e3}  |  {e4}  |  {e5}  |
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |  {f1}  |  {f2}  |  {f3}  |  {f4}  |  {f5}  |
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

ABCDEFGHIJKLMNOPQRSTUV
 """)
    
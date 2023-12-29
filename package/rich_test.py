from rich import print as rprint
from rich.panel import Panel
from rich.console import Console
from rich.layout import Layout
console = Console()
from rich.color import Color
from rich.style import Style
right_style = Style(color="green", bold=True)
mid_style = Style(color="yellow", bold=True)
wrong_style = Style(bold=True)
from rich.text import Text
from rich.markup import escape

# rprint(Panel("Hello, [red]World!"))

wordle = Panel(renderable="panel", border_style="bold", title="WORDLE", subtitle="a knockoff by MK Bishop")

rprint(wordle)

_wordle = Layout(renderable="layout", name="WORDLE")
_wordle.split_column(
    Layout(name="WORDLE"),
    Layout(name="a").split_row(
        Layout(name="0"),
        Layout(name="1"),
        Layout(name="2"),
        Layout(name="3"),
        Layout(name="4"),
    ), #turn 1
    Layout(name="b").split_row(
        Layout(name="0"),
        Layout(name="1"),
        Layout(name="2"),
        Layout(name="3"),
        Layout(name="4"),
    ), #turn 2
    Layout(name="c").split_row(
        Layout(name="0"),
        Layout(name="1"),
        Layout(name="2"),
        Layout(name="3"),
        Layout(name="4"),
    ), #turn 3
    Layout(name="d").split_row(
        Layout(name="0"),
        Layout(name="1"),
        Layout(name="2"),
        Layout(name="3"),
        Layout(name="4"),
    ), #turn 4
    Layout(name="e").split_row(
        Layout(name="0"),
        Layout(name="1"),
        Layout(name="2"),
        Layout(name="3"),
        Layout(name="4"),
    ), #turn 5
    Layout(name="f").split_row(
        Layout(name="0"),
        Layout(name="1"),
        Layout(name="2"),
        Layout(name="3"),
        Layout(name="4"),
    ), #turn 6
)
rprint(_wordle)
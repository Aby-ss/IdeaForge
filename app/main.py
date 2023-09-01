from datetime import datetime
import csv
import time
import requests
from time import sleep
import math
import keyboard
import numpy as np
import asciichartpy

from rich import print
from rich import box
from rich.tree import Tree
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.layout import Layout 
from rich.table import Table

from rich.live import Live
from rich.prompt import Prompt
from rich.progress import track
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn

from rich.traceback import install
install(show_locals=True)

layout = Layout()

layout.split_column(
    Layout(name = "Header", size=3),
    Layout(name = "Body"),
    Layout(name = "Footer", size=3)
)

layout["Body"].split_row(
    Layout(name="Left"),
    Layout(name="Right")
)


layout["Left"].split_column(
    Layout(name="Trends Analysis"),
    Layout(name="Resource Allocator"),
    Layout(name="Related Sales Data")
)

layout["Right"].split_column(
    Layout(name="Competitor Analysis"),
    Layout(name="Feasibility Evaluator")
)


class Header:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "🗃", "[b]IdeaForge: Innovation Catalyst Suite[/]", datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="bold white", box=box.SQUARE)
    
class Footer:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_row("[b]Empower innovation with IdeaForge[/]")
        return Panel(grid, style="white on black", box=box.SQUARE)

def Serpwow_trends():
    # set up the request parameters
    params = {
    'api_key': '098DE11908BF480FBE85735565EEB280',
      'engine': 'google',
      'search_type': 'trends',
      'q': 'Abdulrehman'
    }
    
    # make the http GET request to SerpWow
    api_result = requests.get('https://api.serpwow.com/search', params)
    
    # print the JSON response from SerpWow
    print(json.dumps(api_result.json()))
    
def get_trends(keywords, timeframe='today 5-y', geo='US'):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo=geo)
    interest_over_time_df = pytrends.interest_over_time()
    return interest_over_time_df

def plot_trends(data, title):
    plt.figure(figsize=(10, 6))
    for keyword in data.columns:
        plt.plot(data.index, data[keyword], label=keyword)
    plt.xlabel('Date')
    plt.ylabel('Interest Over Time')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

def plot_ascii_trends(data, title):
    for keyword in data.columns:
        chart = asciichartpy.plot(data[keyword], {'width': 5,'height': 10, 'colors': [asciichartpy.blue]})
        print(f"Keyword: {keyword}\n")
        print(chart)
        print("\n")

layout["Header"].update(Header())
layout["Footer"].update(Footer())

print(layout)
from adventure.utils import read_events_from_file
import random
from rich import print
from rich.prompt import Prompt

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[yellow]You stand still, unsure what to do. The forest swallows you.[/yellow]"

def left_path(event):
    return "[blue]You walk left. [/blue]" + event

def right_path(event):
    return "[red]You walk right. [/red]" + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("[bold cyan]You wake up in a dark forest. You can go[/bold cyan] [bold yellow]left[/bold yellow] or [bold yellow]right[/bold yellow] or [bold red]exit[/bold red] to leave the game.")
    while True:
        choice = Prompt.ask("[bold cyan]Which direction do you choose?[/bold cyan] [bold yellow]left[/bold yellow] or [bold yellow]right[/bold yellow] or [bold red]exit[/bold red] to leave the game.")
        choice = choice.strip().lower()
        if choice == 'exit':
            print("[bold green]Goodbye, play again another time![/bold green]")
            break
        
        print(step(choice, events))

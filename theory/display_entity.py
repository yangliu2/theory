import pandas as pd
from typing import List
import argparse
from rich.console import Console
from rich.table import Table


def display_table(entity: str,
                  rows: List):
    """Display rows of entity using 'rich' package for cli

    Args:
        entity (str): entity name
        rows (List): all the rows related to that entity
    """
    table = Table(title=entity.capitalize())

    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("Theory", justify="left", style="magenta")
    table.add_column("Entities", justify="left", style="green")
    table.add_column("Description", justify="left", style="yellow")

    for row in rows:
        # uppack the list of strings as args for the add_row function
        table.add_row(*row)

    console = Console()
    console.print(table)


def display_entity(entity: str,
                   theory_path: str = "data/theories.csv"):
    """Display all rows related to the entity

    Args:
        entity (str): entity to filter with
        theory_path (str, optional): file path for the theory data. 
        Defaults to "data/theories.csv".
    """
    data_df = pd.read_csv(theory_path)

    # since the entities may contain more than one entity, separated by `:`
    # need to look for if the string have any of the entities
    target_df = data_df[data_df['entities'].str.contains(entity)]

    rows = target_df.values.tolist()
    display_table(entity=entity,
                  rows=rows)


def main():
    parser = argparse.ArgumentParser(description='Displaying entities.')
    parser.add_argument('-e',
                        '--entity',
                        help="entity of the theory")
    args = parser.parse_args()

    display_entity(entity=args.entity)


if __name__ == "__main__":
    main()

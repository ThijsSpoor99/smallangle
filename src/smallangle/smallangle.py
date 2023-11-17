import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def smallangle():
    pass

@smallangle.command()
@click.option(
    '-n',
    '--number',
    default=10,
    help='number of steps between 0 and 2pi'
)
def sin(number):
    """shows sin(x) from 0 to 2pi

    Args:
        number (number): number of steps between 0 and 2pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@smallangle.command()
@click.option(
    '-n',
    '--number',
    default=10,
    help='number of steps between 0 and 2pi'
)
def tan(number):
    """shows tan(x) from 0 to 2pi

    Args:
        number (int): number of steps between 0 and 2pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

if __name__ == "__main__":
    smallangle()
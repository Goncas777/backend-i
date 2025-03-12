import typer

app = typer.Typer()


@app.command()
def calc(number: int, number2: int=0, sum: bool = False, multiplication: bool = False, division: bool = False, subtraction: bool = False, square: bool = False):
    """
    calculadora.
    """

    if number2 == 0:
        typer.echo("If you didnt insert a second number, it means that by defalut we consider is as 1")

    if sum:
        typer.echo(f"Result of sum is {number+number2}")
    if subtraction:
        typer.echo(f"Result of subtraction is {number-number2}")
    if multiplication:
        typer.echo(f"Result of multiplication is {number*number2}")
    if division:
        if number2 == 0:
            typer.echo("Error: Cannot divide by zero.")
        else:
            typer.echo(f"Result of division is {number/number2}")
    if square:
        typer.echo(f"Result of square is {number**2}")


if __name__ == "__main__":
    app()

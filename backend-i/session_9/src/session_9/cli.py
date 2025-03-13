import typer
from session_9.bot import run, welcome
import os
from dotenv import load_dotenv


app = typer.Typer()

load_dotenv()

@app.command()
def start():
    """
    Start the Discord bot using the provided token.
    """
    run(os.getenv('DOCKER_TOKEN', None))
    
@app.command()
def welcome(word: str):
    if(word == 'welcome'):
        welcome()

if __name__ == "__main__":
    app()
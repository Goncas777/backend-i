# Backend I

## Session 1: Python Basics, Dev Container & Poetry

**Goal**: Introduce Python’s core syntax and programming concepts while setting up the development environment using a Dev Container and Poetry.

**Definition**:
- Use a VS Code Dev Container instead of local installations for a consistent environment.
- Manage dependencies with Poetry.
- Learn basic constructs: variables, data types, operators, and control flow.

**Documentation References:**
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [Visual Studio Code Dev Containers](https://code.visualstudio.com/docs/remote/containers)
- [Poetry Documentation](https://python-poetry.org/docs)

### Tutorial

#### Step 1: Dev Container Setup:
- Create a .devcontainer folder in your project with a basic configuration (see the [official docs](https://code.visualstudio.com/docs/remote/containers) for details).

#### Step 2: Poetry Project Initialization:

- Inside the Dev Container, open a terminal and run:

```bash
    poetry config virtualenvs.in-project true # configures poetry to create virtual environment in the projects root
    poetry new backend-i
    cd backend-i
```

- This creates a new project with a `pyproject.toml` file to manage dependencies.

#### Step 3: Basic Python Script:

- Create a file hello.py in your project’s root:

```python
# hello.py
print("Hello, World!")
a = 5
b = 10
print("The sum of", a, "and", b, "is", a + b)
```
- Run your script using Poetry:

```bash
poetry run python hello.py
```

### Exercise

- Use Poetry to add a dependency (e.g. requests) and write a simple script that fetches data from a public API.

### Challenge

- Extend the basic calculator from a previous example to use Poetry for dependency management. Add built-in logging as a dependency (e.g. using the built-in logging module) to record each operation.

## Session 2: Data Structures, Comprehensions, Functions, args & kwargs

**Goal**: Deepen your understanding of Python’s core data structures, comprehensions, and function parameters, including `*args` and `**kwargs`.

**Definition**:
- Master lists, dictionaries, tuples, and sets.
- Learn `list`, `dict`, and `tuple` comprehensions.
- Understand how to define functions with variable-length arguments (`*args`) and keyword arguments (`**kwargs`).

**Documentation References**:
- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

### Tutorial

#### Comprehensions:

- Create a file comprehensions.py:
```python
# List comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x * x for x in numbers]
print("Squared:", squared)

# Dictionary comprehension
squared_dict = {x: x * x for x in numbers}
print("Squared Dict:", squared_dict)

# Tuple comprehension (using a generator expression converted to a tuple)
squared_tuple = tuple(x * x for x in numbers)
print("Squared Tuple:", squared_tuple)
```
#### Functions with `*args` and `**kwargs`:

- Create a file functions.py:
```python
def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_args(1, 2, 3, a="apple", b="banana")
```

#### Poetry Integration:

- Ensure you run these scripts using Poetry:
```bash
poetry run python comprehensions.py
poetry run python functions.py
```
### Exercise

- Write a function that accepts any number of numeric arguments (using `*args`) and returns their sum. Then, write another function using `**kwargs` to filter a dictionary for values above a specified threshold.

### Challenge

- Develop a mini user registration system that:
  - Uses comprehensions to manage users.
  - Accepts dynamic user details via *args and **kwargs.


## Session 3: Object-Oriented Programming, Dunder Methods, and Inheritance

**Goal**: Introduce OOP concepts including `classes`, `objects`, `dunder (magic) methods`, `self`, and inheritance. Learn how to organise your code into modules for a scalable backend.

**Definition**:
- Understand class creation, instance variables, and methods.
- Learn about special dunder methods like `__init__`, `__str__`, and `__repr__` to control object behaviour.
- Implement inheritance to extend classes.

**Documentation References**:
- [Classes](https://docs.python.org/3/tutorial/classes.html)
- [Modules](https://docs.python.org/3/tutorial/modules.html)

### Tutorial

#### Basic Class & Dunder Methods:
- Create a file store.py:
```python
class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def __str__(self):
    return f"Product: {self.name} costs ${self.price:.2f}"

  def __repr__(self):
    return f"Product({self.name!r}, {self.price!r})"

class User:
  def __init__(self, username, email):
    self.username = username
    self.email = email

  def __str__(self):
    return f"User: {self.username}, Email: {self.email}"
```
#### Inheritance & Magic Methods:

- Extend the product class:
```python
class DiscountedProduct(Product):
  def __init__(self, name, price, discount):
    super().__init__(name, price)
    self.discount = discount  # discount in percentage

  def discounted_price(self):
    return self.price * (1 - self.discount / 100)

  def __str__(self):
    return (f"{self.name} - Original: ${self.price:.2f}, "
          f"Discount: {self.discount}%, Now: ${self.discounted_price():.2f}")
```
#### Poetry Integration:

- Ensure all modules are managed under your Poetry project. Run with:
```bash
poetry run python store.py
```

### Exercise

- Develop a mini online store simulation by creating classes for Product and User.
  - Create functions to add a product and register a user.
  - Use dunder methods for string representation.

### Challenge

- Extend the online store by implementing inheritance with a subclass `DiscountedProduct` (as shown above) and display both the original and discounted prices.


## Session 4: Iterators, Generators, Enumerate & Advanced Yield

**Goal**: Learn efficient data traversal using iterators and generators, and enhance your understanding of yield alongside built-in functions like enumerate for practical backend tasks.

**Definition:**
- Implement custom iterators with __iter__ and __next__.
- Create generator functions that use yield to produce sequences lazily.
- Use enumerate to iterate over collections with index-value pairs.

**Documentation References:**
- [Iterators](https://docs.python.org/3/tutorial/classes.html#iterators)
- [Generators](https://docs.python.org/3/tutorial/classes.html#generators)

### Tutorial

#### Custom Iterator with Enumerate:
- Create a file iterators.py:
```python
class EvenIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Use enumerate-like behaviour to track index and value
        while self.index < len(self.numbers):
            num = self.numbers[self.index]
            self.index += 1
            if num % 2 == 0:
                return num
        raise StopIteration

# Using enumerate to show index-value pairs
items = ['apple', 'banana', 'cherry']
for index, item in enumerate(items):
    print(f"Index {index}: {item}")
```

- Generator with Detailed Yield Explanation:

In the same file, add:
```python
def fibonacci(n):
    """Yield the Fibonacci sequence up to n terms.
    
    'yield' pauses the function saving its state, and produces a value
    on each iteration. This is memory efficient for large sequences.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Tutorial snippet: Generate and print first 10 Fibonacci numbers
for num in fibonacci(10):
    print("Fibonacci number:", num)
```

```bash 
poetry run python iterators.py
```

### Exercise

- Implement the custom EvenIterator to filter even numbers from a list.
Write a generator function that yields the Fibonacci sequence.


### Challenge

- Create a generator that reads lines from a large text file (simulate with a list of strings), uses enumerate to show line numbers, strips whitespace, and filters out empty lines.


## Session 5: Decorators

**Goal:** Learn how to enhance functions using decorators to modify or extend their behaviour without altering their code.

**Definition:**
Understand the concept of decorators in Python.
Create simple decorators for logging, execution timing, authentication, and caching.

**Documentation Reference:**
- [Decorators](https://book.pythontips.com/en/latest/decorators.html)

### Tutorial

- Simple Logging Decorator:
Create a file named decorators.py:
```python
def log_calls(func):
    """A decorator that logs function call details."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

print("Result of add:", add(3, 4))
```

### Exercise

- Write a decorator that logs the execution time of a function.
**Hint**: use `time` built-in module

### Challenge

- Create two decorators: one for simulating authentication (verifying a username) and another for caching results of an expensive function (e.g. computing factorial). Demonstrate their usage by decorating a function.

**Hint**: use `functools` built-in module

## Session 6: Unit Testing with pytest

**Goal:** Introduce unit testing in Python using pytest to ensure code quality and reliability.  
**Definition:**  
- Understand the importance of testing in software development.  
- Learn how to write and run unit tests using pytest.  
- Integrate tests in your Poetry-managed project.  

**Documentation References:**  
- [pytest Documentation](https://docs.pytest.org/en/stable/)

### Tutorial

1. **Install pytest as a Development Dependency:**  
```bash
poetry add --dev pytest
```
- Create a Simple Function and Its Test:
```py
def add(a, b):
    return a + b
```
- Then create a test file test_sample.py:
```py
from sample import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```
- Run the Tests:
```bash
poetry run pytest
```

### Exercise

- Write a function that multiplies two numbers and create a pytest unit test for it.

### Challenge

- Implement a function to calculate the factorial of a number recursively (handling negative inputs with an exception) and write unit tests covering normal and edge cases.

## Session 7: Command Line Interfaces using Typer

**Goal:** Learn how to build command line interface (CLI) applications in Python using Typer.  
**Definition:**  
- Understand how to create commands, arguments, and options using Typer.  
- Integrate CLI functionality into your Poetry-managed project for easy command execution.

**Documentation References:**  
- [Typer Documentation](https://typer.tiangolo.com/)

### Tutorial

#### Create a Basic Typer CLI Application:**  
Create a file `main.py`:
```python
import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    """
    Greet the user with their name.
    """
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    app()
```

Run the CLI Application:
Execute the application using Poetry:
```bash
poetry run python main.py hello --name "World"
```

### Exercise

- Develop a Typer CLI command that accepts an integer as input and prints its square.


### Challenge

- Extend your CLI to support multiple commands (e.g. addition and subtraction) with proper error handling.

## Session 8: Building a Discord Bot with Typer CLI

**Goal:** Create a hands-on project to build a Discord bot that runs under a Typer-based command line interface.  
**Definition:**  
- Learn how to use the Discord API via discord.py to create a bot.  
- Integrate the bot with a Typer CLI for command-based execution and control.  
- Manage your project and dependencies with Poetry.

**Documentation References:**  
- [discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)
- [Typer Documentation](https://typer.tiangolo.com/)

### Tutorial

1. **Create the Discord Bot Module:**  
Create a file `bot.py`:
```python
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

def run_bot(token: str):
    bot.run(token)
```

2. Integrate the Bot with Typer CLI:
Create a file cli.py:
```py
import typer
from bot import run_bot

app = typer.Typer()

@app.command()
def start(token: str):
    """
    Start the Discord bot using the provided token.
    """
    run_bot(token)

if __name__ == "__main__":
    app()
```

Run the Bot via CLI:
Execute the bot using Poetry (replace <YOUR_DISCORD_TOKEN> with your actual token):
```bash 
poetry run python cli.py start --token "<YOUR_DISCORD_TOKEN>"
```

### Exercise

- Add a simple function to your bot that returns a welcome message for a user and expose it via a Typer command.

### Challenge

- Extend your project by adding a Typer command that sends a test message to a specific Discord channel. (Hint: Use asynchronous functions in your bot module.)


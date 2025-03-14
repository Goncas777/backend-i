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

## Session 7: Context Managers

**Goal:** Learn to manage resources effectively by implementing context managers and utilising the with statement to ensure clean, safe handling of resources in your code.
**Definition:**
- Understand what context managers are and how they facilitate resource management (e.g. file handling, network connections, locks).
- Learn how to implement context managers using both a class (defining `__enter__` and `__exit__`) and the `@contextmanager` decorator from the `contextlib` module.
- Integrate these techniques into your Poetry-managed project for consistency.
**Documentation References:**
- [Context Managers](https://docs.python.org/3/reference/datamodel.html#context-managers)
- [contextlib — Utilities for with-statement contexts](https://docs.python.org/3/library/contextlib.html)

### Tutorial
- Custom Context Manager using a Class:
- Create a file named context_manager.py with the following code:
```py
class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file {self.filename}")
        if self.file:
            self.file.close()
        # Do not suppress exceptions
        return False

# Usage example:
if __name__ == "__main__":
    with FileOpener("example.txt", "w") as f:
        f.write("Hello, Context Managers!")
```
- Context Manager using the @contextmanager Decorator:
- Extend the same file or create a new one, and add:
```py
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    print(f"Opening file {filename}")
    f = open(filename, mode)
    try:
        yield f
    finally:
        print(f"Closing file {filename}")
        f.close()

# Usage example:
if __name__ == "__main__":
    with open_file("example.txt", "a") as f:
        f.write("\nAppending with context manager using @contextmanager.")
```

### Exercise

- Write a context manager that measures and prints the execution time of the code block it wraps.

### Challenge

- Create a context manager using the @contextmanager decorator that handles exceptions within its block, logs the exception details, and suppresses the exception so that the program continues running.

## Session 8: Command Line Interfaces using Typer

**Goal:** Learn how to build command line interface (CLI) applications in Python using Typer.  
**Definition:**  
- Understand how to create commands, arguments, and options using Typer.  
- Integrate CLI functionality into your Poetry-managed project for easy command execution.

**Documentation References:**  
- [Typer Documentation](https://typer.tiangolo.com/)
- [Typer Testing](https://typer.tiangolo.com/tutorial/testing)

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
poetry run python main.py hello "World"
```

### Exercise

- Develop a Typer CLI command that accepts an integer as input and prints its square.

### Challenge

- Extend your CLI to support multiple commands (e.g. addition and subtraction) with proper error handling.

## Session 9: Building a Discord Bot with Typer CLI

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

## Session 10: HTTP Protocol
**Goal:** Gain a deep understanding of the HTTP protocol and learn how to implement a basic HTTP server from scratch using Python’s built-in libraries (without any external frameworks).
**Definition:**
- Understand the fundamentals of the HTTP protocol including requests, responses, headers, and methods (e.g. GET, POST).
- Learn how to create a low-level TCP socket server that manually handles HTTP request parsing and response generation.
- Discover how HTTP messages are structured and how to construct valid HTTP responses.
**Documentation References:**
- [Socket Module – Python Documentation](https://docs.python.org/3/library/socket.html)
- [HTTP/1.1 Overview – MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
### Tutorial
- Understanding the Basics:
  - HTTP is a request–response protocol that runs over TCP/IP. A client (typically a web browser) sends an HTTP request to a server, which then returns an HTTP response. An HTTP request contains:
    - A request line (e.g. GET / HTTP/1.1)
    - Headers (e.g. Host: localhost)
    - An optional body (for POST or PUT requests)

  - An HTTP response typically contains:
    - A status line (e.g. HTTP/1.1 200 OK)
    - Headers (e.g. Content-Type: text/html)
    - An optional body (e.g. HTML content)

- Creating a Basic HTTP Server Using Sockets:
- Create a file called http_server.py with the following code:
```py
import socket

# Define the host and port to listen on
HOST, PORT = '127.0.0.1', 8080

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Allow immediate reuse of address after program exit
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Serving HTTP on {HOST} port {PORT} ...")

    while True:
        # Accept a new client connection
        client_connection, client_address = server_socket.accept()
        with client_connection:
            # Receive the request data (limit to 1024 bytes for simplicity)
            request_data = client_connection.recv(1024).decode('utf-8')
            print("Received request:")
            print(request_data)

            # Construct a simple HTTP response
            http_response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                "Content-Length: 46\r\n"
                "\r\n"
                "<html><body><h1>Hello, HTTP!</h1></body></html>"
            )

            # Send the HTTP response back to the client
            client_connection.sendall(http_response.encode('utf-8'))
```
- Explanation of the Code:

  - We create a TCP socket using socket.socket(socket.AF_INET, socket.SOCK_STREAM).
  - The setsockopt call with SO_REUSEADDR ensures that the socket can be reused quickly after the program stops.
  - The server listens on IP 127.0.0.1 (localhost) and port 8080.
  - For each incoming connection, the server reads the request, prints it, and then sends a hard-coded HTTP response.
  - Notice the HTTP response is manually constructed. The headers and body are separated by a blank line (\r\n\r\n).

- Running the Server:

- To run the server (ensuring your project is managed with Poetry), use:
```bash
poetry run python http_server.py
```
- Open your browser and navigate to http://127.0.0.1:8080 to see the response.

### Exercise
- Modify the server to parse the first line of the HTTP request (the request line) and print out the HTTP method and the requested path.

### Challenge
- Extend your HTTP server to support multiple endpoints. For example, respond with a different message when the requested path is /about versus / (the root). Also, include basic error handling for unsupported paths by returning a 404 response.


## Session 11: Developing and Using an API with FastAPI

**Goal:** Learn how to create a RESTful API using FastAPI, integrate logging, and test your endpoints to ensure reliable functionality.
**Definition:**
- Understand how FastAPI leverages Python type hints to build efficient APIs quickly.
- Learn to create various endpoints (GET, POST, etc.) and integrate the built-in Python logging module to monitor API behaviour.
- Gain knowledge on testing API endpoints using tools such as pytest and HTTP client libraries (e.g. httpx).

**Documentation References:**
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)

### Tutorial
- Setting Up the FastAPI Application:
- Create a file named main.py with the following content:
> Install `poetry add uvicorn` to your dependencies
```py
from fastapi import FastAPI, HTTPException
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def read_root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to the FastAPI API!"}

@app.post("/items/")
async def create_item(item: dict):
    logger.info(f"Item received: {item}")
    # A simple validation example
    if "name" not in item:
        logger.error("Item does not contain 'name'")
        raise HTTPException(status_code=400, detail="Item must have a name")
    return {"item": item}

# Run the application using Uvicorn with:
# poetry run uvicorn main:app --reload
```
- Open your browser or use an HTTP client to access http://127.0.0.1:8000 and http://127.0.0.1:8000/docs for interactive API docs.
- Testing the API:
```py
#Create a test file named test_main.py:

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI API!"}

def test_create_item_success():
    response = client.post("/items/", json={"name": "Test Item"})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Test Item"}}

def test_create_item_failure():
    response = client.post("/items/", json={"description": "No name provided"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Item must have a name"
```

### Exercise
- Add a new endpoint to update an item using the PUT method. The endpoint should log the update operation and return the updated item.

### Challenge
- Extend the API by adding a DELETE endpoint to remove an item. The endpoint should:
    - Log the deletion.
    - Return a message confirming the deletion.
    - Include a test case that checks for the correct status code and response.

## Session 12: Deploying FastAPI API with Docker and Logging

**Goal:** Learn how to containerise your FastAPI application using Docker, configure logging within the container, and ensure the API runs reliably in a production-like environment.
**Definition:**
- Understand the basics of Docker and how to create a Dockerfile for your FastAPI application.
- Learn to configure logging so that container logs can be monitored easily.
- Gain skills to build and run the containerised API, and optionally extend to using Docker Compose for multi-container setups.

**Documentation References:**
- [Docker Documentation](https://docs.docker.com/reference/)
- [FastAPI Docker Deployment](https://fastapi.tiangolo.com/deployment/docker/?h=docker)

### Tutorial
- Creating a Dockerfile:
- Create a file named Dockerfile in your project directory:
```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files to install dependencies
COPY pyproject.toml poetry.lock* /app/

# Install Poetry
RUN pip install poetry

# Install dependencies without dev dependencies for production
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copy the rest of the application code
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
- Building and Running the Docker Container:
- Build the Docker image:

`docker build -t fastapi-app .`

- Run the container:

`docker run -d -p 8000:8000 fastapi-app`

- Your FastAPI app will now be accessible at http://localhost:8000.

### Exercise
- Create a Docker Compose file to run your FastAPI application along with a reverse proxy (for example, using Nginx) for routing. Ensure that logs are forwarded appropriately.

### Challenge
- Enhance your Docker setup by adding a volume mount for persistent logging. Modify your Dockerfile and/or Docker Compose configuration so that application logs are saved to a host directory. Provide instructions to view the logs from the host.

## Session 13: Integrating Docker, FastAPI, SQLModel, and Postgres with Logic Layers

**Goal:**
- Build a robust RESTful API using FastAPI, SQLModel (an ORM with Pydantic support), and a Postgres database.
- Leverage Docker Compose to orchestrate containers for the application and database, allowing developers to quickly start using new tools without manual installations.
- Introduce a logic (business) layer to separate core business rules from API endpoints, enhancing modularity and maintainability.

**Definition:**
- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python type hints.
- SQLModel: An ORM library (built on SQLAlchemy) that integrates with Pydantic for data validation and settings management.
- Postgres: A powerful, open-source object-relational database system.
- Docker Compose: A tool for defining and running multi-container Docker applications, which accelerates development by allowing you to run a complete stack (FastAPI, Postgres, etc.) without installing them locally.
- Logic Layers: By decoupling business logic from the API routes, you create reusable and testable components that simplify future development and maintenance.

**Documentation References:**
-[FastAPI Documentation](https://fastapi.tiangolo.com/)
-[SQLModel Documentation](https://sqlmodel.tiangolo.com/)
-[PostgreSQL Documentation](https://www.postgresql.org/docs/)
-[Docker Compose Documentation](https://docs.docker.com/reference/compose-file/)

### Tutorial
1. Application Setup with FastAPI and SQLModel

Create a file called main.py:
```py
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Field, create_engine, Session, select
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

# Define a sample model for an item
class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str = None

# Database connection string using Postgres container (host 'db' will be defined in docker-compose)
DATABASE_URL = "postgresql://postgres:password@db:5432/postgres"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

# ----- Logic Layer (Business Logic) -----

def create_item_logic(session: Session, item: Item) -> Item:
    logger.info("Creating a new item in the database")
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

def update_item_logic(session: Session, item_id: int, new_item: Item) -> Item:
    logger.info(f"Updating item with id {item_id}")
    statement = select(Item).where(Item.id == item_id)
    existing_item = session.exec(statement).one_or_none()
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")
    existing_item.name = new_item.name
    existing_item.description = new_item.description
    session.add(existing_item)
    session.commit()
    session.refresh(existing_item)
    return existing_item

def delete_item_logic(session: Session, item_id: int) -> dict:
    logger.info(f"Deleting item with id {item_id}")
    statement = select(Item).where(Item.id == item_id)
    item = session.exec(statement).one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    session.commit()
    return {"message": f"Item {item_id} deleted successfully"}

# ----- API Endpoints -----

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
    logger.info("Database tables created")

@app.post("/items/", response_model=Item)
def create_item(item: Item, session: Session = Depends(get_session)):
    return create_item_logic(session, item)

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, session: Session = Depends(get_session)):
    statement = select(Item).where(Item.id == item_id)
    result = session.exec(statement)
    item = result.one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item, session: Session = Depends(get_session)):
    return update_item_logic(session, item_id, item)

@app.delete("/items/{item_id}")
def delete_item(item_id: int, session: Session = Depends(get_session)):
    return delete_item_logic(session, item_id)
```
2. Docker Setup with Docker Compose

Create a Dockerfile:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy Poetry configuration files
COPY pyproject.toml poetry.lock* /app/

# Install Poetry and dependencies
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

# Copy application code
COPY . /app/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
Create a docker-compose.yml file:
```yaml
services:
  db:
    image: postgres:17
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DB: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  web:
    build: .
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db

volumes:
  postgres_data:
```
**Explanation:**
- Docker Compose: This file defines two services: a Postgres database (db) and the FastAPI application (web). Using Docker Compose, developers can start the entire stack with a single command without installing Postgres locally.
- Logic Layer: In the code, functions like create_item_logic, update_item_logic, and delete_item_logic encapsulate business rules, allowing API endpoints to remain thin and focused on request/response handling. This separation simplifies testing and maintenance.

3. Running the Application
Build and run the containers using Docker Compose:

`docker-compose up --build`

### Exercise
- Add a new endpoint to search for items by name. Create a corresponding logic function in the logic layer that queries the database for items matching a provided name substring.

### Challenge
- Create an endpoint to delete all items that have a specific keyword in their description. Implement the logic in a separate function in the logic layer, include logging for each deletion, and ensure the endpoint returns the number of items deleted.

## Session 14: Django Overview, Setup, and Models/ORM

**Goal:**
- Introduce Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- Set up a new Django project and app using Django’s built-in tools.
- Understand Django’s architecture with a focus on models and the Django ORM for database operations.

**Definition:**
- Django Overview: Django follows the Model-View-Template (MVT) architectural pattern. It includes a powerful ORM, an easy-to-use admin interface, and a robust set of tools for building web applications quickly.
- Models and ORM: Models represent the data structure and business logic. The Django ORM allows you to interact with the database using Python code rather than SQL.

**Documentation References:**
- [Django Documentation](https://docs.djangoproject.com/en/5.1/)
- [Django Models](https://docs.djangoproject.com/en/5.1/topics/db/models/)

### Tutorial
- Project Setup:
    - Create a new Django project and an app:
```bash
django-admin startproject mysite
cd mysite
python manage.py startapp core
```
Configure the App:
Add the app to INSTALLED_APPS in mysite/settings.py:
```py
INSTALLED_APPS = [
    # ...
    'core',
]
```

Creating a Model:
In core/models.py, create a simple model:

```py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
```
Run migrations to create the database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Exercise
- Create a model for a Category with fields for name and slug. Then, create a relationship from Product to Category.

### Challenge
- Implement a custom model method in the Product model that applies a discount to the product price. Also, write a Django shell snippet to test the method.

## Session 15: Django Views and URL Routing

**Goal:**
- Learn how to create Django views to handle HTTP requests and responses.
- Understand URL routing and how to map URLs to views.
- Create function-based and class-based views for various endpoints.

**Definition:**
- Views: In Django, views are Python functions or classes that receive web requests and return web responses.
- URL Routing: Django uses URLconf to map URLs to their corresponding view functions, enabling clean URL designs.

**Documentation References:**
- [Django Views](https://docs.djangoproject.com/en/5.1/topics/http/views/)
- [Django URL Dispatcher](https://docs.djangoproject.com/en/5.1/topics/http/urls/)

### Tutorial

- Function-Based View:
    - In core/views.py, add a simple view:
```py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Django API!")

# URL Routing:
# Create core/urls.py and configure URL patterns:

from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]

# Then include core/urls.py in the main mysite/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# Class-Based View:
# Add a class-based view in core/views.py:

from django.views import View
from django.http import JsonResponse

class ProductList(View):
    def get(self, request):
        # In a real app, retrieve products from the database
        data = {"products": ["Product 1", "Product 2", "Product 3"]}
        return JsonResponse(data)

# Update core/urls.py:

    from django.urls import path
    from .views import home, ProductList

    urlpatterns = [
        path('', home, name='home'),
        path('products/', ProductList.as_view(), name='product-list'),
    ]
```

### Exercise
- Create a view that returns a JSON response with details of all categories from the database.

### Challenge
- Implement a view to update a product using a class-based view. Include error handling for cases when the product is not found.

## Session 16: Django Templates and Forms

**Goal:**
- Learn how to render dynamic HTML content using Django templates.
- Understand how to create and process forms in Django to handle user input.
- Gain insight into form validation and error handling within Django.

**Definition:**
- Templates: Django’s templating engine allows you to define HTML pages with dynamic content.
- Forms: Django provides tools for generating HTML forms, validating input, and processing data.

**Documentation References:**
- [Django Templates](https://docs.djangoproject.com/en/5.1/topics/templates/)
- [Django Forms](https://docs.djangoproject.com/en/5.1/topics/forms/)

### Tutorial
- Setting Up a Template:
- Create a directory core/templates/core/ and add a file home.html:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django Home</title>
</head>
<body>
    <h1>Welcome to Django!</h1>
    <p>This is a dynamic page rendered with a template.</p>
</body>
</html>
```

- View to Render Template:
- In core/views.py, add a view:
```py
from django.shortcuts import render

def home_template(request):
    return render(request, 'core/home.html')

# Update core/urls.py to include:

from django.urls import path
from .views import home, ProductList, CategoryList, ProductUpdate, home_template

urlpatterns = [
    path('', home_template, name='home-template'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/update/<int:product_id>/', ProductUpdate.as_view(), name='product-update'),
    path('categories/', CategoryList.as_view(), name='category-list'),
]

#Creating and Processing a Form:
#Create a simple form in core/forms.py:

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

# Then create a view in core/views.py:

from .forms import ContactForm
from django.shortcuts import render, redirect

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data (e.g., send an email)
            return redirect('home-template')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})
```
- Create a template core/templates/core/contact.html:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contact</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Send</button>
    </form>
</body>
</html>
```
- Finally, add a URL for the contact view in core/urls.py:
```py
    urlpatterns = [
        path('', home_template, name='home-template'),
        path('contact/', contact_view, name='contact'),
        path('products/', ProductList.as_view(), name='product-list'),
        path('products/update/<int:product_id>/', ProductUpdate.as_view(), name='product-update'),
        path('categories/', CategoryList.as_view(), name='category-list'),
    ]
```

### Exercise
- Create a template to display a list of products. Use a view that queries all products from the database and passes them to the template for rendering.

### Challenge
- Enhance the contact form to include server-side validation that ensures the message field has at least 10 characters. Update the form and display appropriate error messages in the template.

## Session 17: Django Admin and Advanced Features

**Goal:**
- Learn how to customise the Django admin interface to manage your models efficiently.
- Explore advanced Django features such as custom admin actions and model methods.
- Understand how to integrate logging into the admin for monitoring administrative actions.

**Definition:**
- Django Admin: A built-in interface that allows for quick data management, built automatically from your model definitions.
- Advanced Features: Customising admin forms, list displays, filters, and adding custom actions to enhance data management capabilities.

**Documentation References:**
- [Django Admin Site](https://docs.djangoproject.com/en/5.1/ref/contrib/admin/)
- [Customising the Admin Interface](https://docs.djangoproject.com/en/5.1/ref/contrib/admin/actions/)

### Tutorial
- Registering Models in Admin:
- In core/admin.py, register your models:
```py
from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
```

- Custom Admin Action:
- Add a custom action to mark selected products as "discounted" (for demonstration, just log the action):
```py
def mark_discounted(modeladmin, request, queryset):
    for product in queryset:
        product.price = product.price * 0.9  # apply a 10% discount
        product.save()
    modeladmin.message_user(request, "Selected products marked as discounted.")
mark_discounted.short_description = "Apply 10% discount"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name',)
    actions = [mark_discounted]

# Integrating Logging in Admin:
# In your settings, ensure logging is configured. For example, in mysite/settings.py add:

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
```
- Accessing the Admin:
- Create a superuser:

`python manage.py createsuperuser`

### Exercise
- Customize the Django admin for the Product model to display a computed field (e.g., discounted price) and filter products by category.

### Challenge
- Implement a custom admin form for the Category model that validates the uniqueness of the slug (beyond the built-in model constraint) and logs an info message when a new category is created via the admin.
 
## Project Module Briefing 

- This final project spans four sessions and challenges you to develop a real-world application using one or more of the following Python solutions: a Command Line Interface (CLI) with Typer, an API with FastAPI, or a SaaS web application with Django. You may even combine frameworks (for instance, using FastAPI for REST endpoints and Typer for background job commands) to solve the problem more effectively. Below are the detailed requirements and evaluation criteria.
### Project Objectives and Requirements

- Real-World Problem Solving:
- Your project must address a practical problem. For example:
    - Personal Finance Manager: Manage income and expenses via a CLI or web interface.
    - Task Manager: Organise, update, and track tasks using REST APIs and a web dashboard.
    - Inventory System: Manage products and categories in a business context with full administrative features.
        
Choose an idea that is relevant and adds real value to users.

### Framework Implementation Requirements:
- CLI using Typer:
    - Commands: Implement at least 5 different commands (e.g. add, list, update, delete, summary).
        - Options & Arguments: Each command must use options and arguments to handle user input effectively.
          
Example: A command to add an expense might require an amount, category, and optional notes.

- API using FastAPI:
    - Endpoints: Create one endpoint per major HTTP verb—GET, POST, PUT, PATCH, DELETE.
    - OpenAPI Documentation: Each endpoint must be automatically documented on the OpenAPI (Swagger) page provided by FastAPI.
            
Example: A GET endpoint to retrieve tasks, a POST endpoint to create a new task, etc.
        
- SaaS using Django:
    - Models: Create at least 2 models (e.g. Product and Category, or Task and User).
    - Form: Implement at least 1 form for user input (e.g. a contact or registration form).
    - Views: Develop at least 4 views (function-based or class-based) to cover listing, detail, creation, and update operations.
    - Admin: Set up the corresponding admin views to manage your models.

Example: A Django app for inventory could have ListView for products, DetailView for product details, CreateView for adding a new product, and UpdateView for editing existing products.

### Testing:
- Implement tests using either pytest or unittest. Ensure that critical functionality (e.g. API endpoints, CLI commands, form validations) is covered.

### Logging:
- Integrate logging into your project to track operations and errors. Ensure that logs capture key actions and any exceptions that occur.

### Database Integration:
- The project must interact with a database (Postgres is recommended). Ensure that CRUD operations or data queries are performed via your chosen framework’s ORM or database connectivity tool.

### Documentation:
- Create a comprehensive README.md that describes the project, installation steps, and usage instructions.
- The documentation should be clear enough so that another developer can set up and run your project without additional guidance.

### Poetry:
- Use Poetry to manage your dependencies and project configuration consistently.

### Bonus – Docker and Docker Compose:
- Although not mandatory, using Docker and Docker Compose is a plus. This will allow you to set up your development environment (including Postgres) in a containerised manner without needing to install these tools locally.
- Include a Dockerfile and a docker-compose.yml file that orchestrates your application and database services.

### Project Evaluation (Maximum 20 Points)
- Documentation (3 points):
    - The README.md must clearly describe the project, installation process, and usage instructions.
- Poetry and Frameworks Requirements (5 points):
    - Your project must use Poetry for dependency management and meet the specific framework requirements (e.g., 5 CLI commands with options for Typer, endpoints for FastAPI, or models, form, views, and admin for Django).
- Tests (3 points):
    - Include a comprehensive test suite covering core functionalities.
- Logging (2 points):
    - Implement logging that captures key operations and errors.
- Database Integration (1 point):
    - The project must interact with a database (preferably Postgres).
- GIT Release (Tag) and Copy on Google Drive Module Folder (2 points):
    - Ensure that you tag a release in your Git repository and provide a copy in the designated Google Drive folder.
- Docker and Docker Compose (1 point):
    - Using Docker and Docker Compose to containerise your solution is a plus.

- Working Solution + Multiple Framework Implementation (3 points):
    - A fully functioning project that may integrate more than one framework (e.g., a FastAPI API combined with Typer background jobs) will score higher.

#### Describing Examples

- Typer Example:
    - Create a CLI tool where the command expense add --amount 100 --category food --note "Lunch" adds an expense record. Include commands such as list, update, delete, and summary to manage expenses.

- FastAPI Example:
    - Build a RESTful API with endpoints:
        - GET /tasks/ to retrieve all tasks.
        - POST /tasks/ to create a task.
        - PUT /tasks/{id} to update a task.
        - PATCH /tasks/{id} for partial updates.
        - DELETE /tasks/{id} to delete a task.
    - All endpoints are automatically documented in FastAPI’s interactive docs.

- Django Example:
    - Develop a SaaS solution, such as an inventory management system, with models for Product and Category, a form for product input, views to list, detail, create, and update products, and an admin interface that allows for managing these models.
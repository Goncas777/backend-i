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

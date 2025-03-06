
class Stock:
    def __init__(self):
      self.stock = {}
    
    def add_product(self,product,quantity):
      self.product = product
      self.quantity = quantity

      if self.product in self.stock:
        self.stock[quantity] += quantity

      else:
        self.stock[quantity] = quantity

    def __str__(self):
      return f"Stock: {name}, quantity: {quantity}"


    
class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def __str__(self):
    return f"Product: {self.name} costs ${self.price:.2f}"

  def __repr__(self):
    return f"Product({self.name}, {self.price})"
  


class User:
  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password = password

  def __str__(self):
    return f"User: {self.username}, Email: {self.email}"
  


name = "Teclado Gaming"
price = 35
quantity = 5 
user = "GoncaloVieira"
email = "goncalo_vieira@eticalgarve.com"
password = "Trogloditadaspasswords"


product = Product(name, price)


Stock().add_product(name, quantity)


print(product)
print(Stock())        
print(User(user, email, password))

# double underscores-private and protected __init__
# anytime you see the dunder it is a method given to you from python directly(don't override just USE IT)


class Invoice:                                # invoice class
    # dunder string- pass in self(str method to help you get visabilty what you instatiated)
    def __str__(self):
      return "This is the invoice class!"


inv = Invoice()                    # inv is instatiated for invoice
print(str(inv))                    # now print str and pass in the inv function


class Invoice:
  def __init__(self, client, total):          # dunder init takes in self and client and total
    self.client = client
    self.total = total

  def __str__(self):                                        # using string interpolation below
    # pulling in the client and total
    return f"Invoice from {self.client} for {self.total}"


# set inv to represent the invoice and passed in Google and 100 to show in the print statement
inv = Invoice('Google', 500)
# calling the str method and calling the inv function
print(str(inv))

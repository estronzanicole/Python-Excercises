# NOTES


class Invoice:                           # behavior in class is with functions---data in classes below
    def __init__(self, client, total):   # constructor function- function def dunder __init__ -auto called whenever you call the class-add data in class(first argument self, then client and total)
      # add the data tdirectly to class here by self. then variable name
      self.client = client
      # same as above-everythin in python is an object(assign whatever got passed in, and assign it to the instance)
      self.total = total

    # create a function formatter takes in self(every function takes in self)-gives you access to self
    def formatter(self):
      # now to return a formatted string using string literal syntax
      return f'{self.client} owes: ${self.total}'


# instantiate the invoices one is google-pass the values Goggle(client name and 100)
google = Invoice('Google', 100)
snapchat = Invoice('SnapChat', 200)      # same as above just snapchat

print(google.formatter())
print(snapchat.formatter())

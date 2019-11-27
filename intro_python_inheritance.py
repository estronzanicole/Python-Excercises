# Inheritance


# create the class of user
class User:
  # function init with self email first name and last name passed in
  def __init__(self, email, first_name, last_name):
    # instance attributes for email first name and last name
    self.email = email
    self.first_name = first_name
    self.last_name = last_name

  # function greeting and self
  def greeting(self):
    # returns a formatted string here passed in first and last names
    return f'Hi {self.first_name} {self.last_name}'
# is new element a new type of one of the classes you have already? if so because of admin yes


# create the admin class here(inherits from User)to declare if one class inherits from another
class AdminUser(User):
  # active users takes in self(class that inherits from class above)
  def active_users(self):
    return '500'


# tiffany is an admin user, she has an email and first name and last name
tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')

# and created a regular user here names kristine and the same attributes as above
kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

# to have acess to the active users method
print(tiffany.active_users())
# will print the full greeting because of inheritance-it works the child class has access to the attributes as the parent class and add on from there
print(tiffany.greeting())
# if you try to have kristine access
print(kristine.active_users())

# ability to create specialized classes

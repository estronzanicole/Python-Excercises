# CLASS vs INSTANCE


class Website:                         #
    def __init__(self, title):         # function init that takes in self and the title of the website
      # self.title set equal to what ever the title is passed in
      self.title = title


#instance attribute
ws = Website('My Website Title')      # set ws as the Website
# __dict__ -returns the attributes and there values in dictionary form
print(ws.__dict__)
#another instance-you would need to pass in another value
ws_two = Website('My Second Title')   # this will print out the second title
print(ws_two.__dict__)

#class attribute-title below is hard coded in


class DifferentWebsite:               # create the class DifferentWebsite
  # passin a variable here title is equal to my class title
  title = 'My Class Title'


# create the instance of the class-dq is equal to DifferentWebsite
dw = DifferentWebsite()
# simply call dw.title to return the value(not treated the same) (__dict__ won't return a dictionary)
print(dw.title)

dw_two = DifferentWebsite()
print(dw_two.title)

# differences class attrictubute belongs to class definition and called any time you need it
# instance belongs to the instance-for every other instance you must pass in a different instance

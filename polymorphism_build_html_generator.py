# Polymorphism NOTES


class Html:                                 # create a class called html
    # create a function that brings in the init method and takes in self and content
    def __init__(self, content):
        self.content = content  # stores content in a instance vraible here

    # abstract function called render and self passed in
    def render(self):
        # raise notImplementedError-have to access function or won't work
        raise NotImplementedError("Subclass must implement render method")


# create a child class called heading inherits from the Html class
class Heading(Html):
    # calls in the render fucntion
    def render(self):
        return f'<h1>{self.content}</h1>'


# class takes in the Html class
class Div(Html):
    # has it's own render method that takes in self
    def render(self):
        return f'<div>{self.content}</div>'


tags = [Div('Some content'), Heading('My Amazing Heading'), Div('Another div')]

# above-create a list called tags and add elements-call Div class and pass in content
#then heading element and pass in content
# and then Div

for tag in tags:                                                       # iterate through the list
    # print out the string value(tag-string representation) concat a colon and call the render function
    print(str(tag) + ': ' + tag.render())
    # rendered your own HTML here
    print(tag.render())

# poly means many and morphism is change so basically many changes -Polymorphism

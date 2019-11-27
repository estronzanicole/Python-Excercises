# Iterators vs Generator NOTES below


class InfiniteLineup:                        # class infinite lineup
    # create the init method here and self and players passed in
    def __init__(self, players):
        self.players = players               # so you can bring in players list

    # linup takes in self to have access to players
    def lineup(self):
        # create the variable called lineup_max and set it equal to len players (brings in a count of players)
        lineup_max = len(self.players)
        # set the index(idx) to zero
        idx = 0

        while True:                                             # create the infite loop using while true
            if idx < lineup_max:                         # conditional if the index is less than the lineup max
                # you want to-yield keyword(yielding to generator) to self players index
                yield self.players[idx]
            else:
                idx = 0                                             # set the index to zero
                # still want to yield to self players index
                yield self.players[idx]

            # increment the indx by one
            idx += 1

    # dudner repr takes in self and returns the entire object(string)
    def __repr__(self):
        return f'InfiniteLineup({self.players})'

    # dunder string method takes in self
    def __str__(self):
        # pass in a comma and join the players
        return f"InfiniteLineup with the players: {', '.join(self.players)}"


astros = [
    'Springer',
    'Bregman',
    'Altuve',
    'Correa',
    'Reddick',
    'Gonzalez',
    'McCann',
    'Davis',
    'Tucker'
]

# full lineup variable that takes in(instatiate) takes the list of players
full_lineup = InfiniteLineup(astros)
# create an instance of astros lineup-set equal to the full lineup.lineup function()
astros_lineup = full_lineup.lineup()
# in between- you have to start the process by saying next and call the astros lineup
# whenever you put a yield it tells python a generator-and next has to be used
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))

print(repr(full_lineup))

print(str(full_lineup))

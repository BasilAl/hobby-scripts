class Player():
    """  """
    def __init__(self, SL):
        self.SL = SL

    def ViewInventory(self):
        pass


class item:
    """Items will have a name, a type to define their use, a location to
    distinguish if they are in a room or in the inventory and a use if their type allows it.
    """

    def __init__(self,id, location,*args):
        self.id = id
        self.type = itype
        self.location = location
        self.name= id.


    def __str__(self):
        return "{}\nLocated in: {}\nUse Command: \'{}\'\n====\nType: {}".format(self.name, self.location, self.use,
                                                                                self.type)



    """Rooms will have a name and a description text triggering when the player enters the room"""



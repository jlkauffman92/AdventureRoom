class Item(object):
    def __init__(self, name, look):
        self.name = name
        self.look = look

    def lookAt(self):
        return self.look
class Weapon(Item):

        def __init__(self, name, look, damage):
            Item.__init__(self, name, look)
            self.damage = damage


class Gold(Item):
    pass


class Scene:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = []
        for item in items:
            self.items.append(item)
        
    def sceneDescPretty(self):
        return f"{self.name}\n\n{self.description}\n"
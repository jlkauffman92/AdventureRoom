class Item(object):
    def __init__(self, name, look, actions=[{'grab': 'it is too heavy!'}]):
        self.name = name
        self.look = look
        self.actions = actions

    def lookAt(self):
        return self.look
class Weapon(Item):

        def __init__(self, name, look, actions, damage):
            Item.__init__(self, name, look, actions)
            self.damage = damage


class Gold(Item):
    pass


class Scene:
    def __init__(self, id, description, items):
        self.id = id
        self.name = f'Scene {id}'
        self.description = description
        self.items = []
        for item in items:
            self.items.append(item)
        
    def sceneDescPretty(self):
        return f"{self.name}\n\n{self.description}\n"
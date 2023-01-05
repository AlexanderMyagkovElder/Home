class Soup():
    def __init__(self, foundation='water'):
        self.foundation = foundation
        print(f'cooking soup. step 1: {foundation}')

    def Is_it(self, component):
        self.component = component
        if self.component == 'свекла':
            print('borszcz')
        elif self.component == 'капуста':
            print('szczii')
        elif self.component == 'горох':
            print('peasing soup')
        else:
            print(f'just {self.foundation} with {component}')


a = Soup()
what_put = input('what will put in water? ')
a.Is_it(what_put)

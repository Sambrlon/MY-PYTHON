class Hero:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        print('Я', self.name, 'размером', self.size)

    def go_right(self):
        print(self.name, 'иду направо')

    def go_left(self):
        print(self.name, 'иду налево')

    def observe(self):
        print(self.name, 'осматриваюсь')


hero_1 = Hero('Артём', 12)

hero_1.go_right()
hero_1.go_left()
hero_1.observe()

print(hero_1.name)
print(hero_1.size)

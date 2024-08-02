from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)


def get_advanced_writer(file_name):

    def write_everything(*data_set):
        aw = open('example.txt', 'w', encoding='utf-8')
        aw.write("Это строчка \n['А', 'это', 'уже', 'число', 5, 'в', 'списке']")
        aw.close()

    return write_everything


f = get_advanced_writer('example.txt')
f()


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

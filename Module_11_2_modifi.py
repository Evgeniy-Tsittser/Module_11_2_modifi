import inspect


class Introspector:
    def __init__(self, name, school, age):
        self.name = name
        self.school = school
        self.age = age

    def write_file(self):
        atr_list = [self.name, self.school, self.age]
        with open('info.txt', 'w', encoding='utf-8') as file:
            for line in atr_list:
                file.write(str(line) + '\n')


def into_func(obj):
    dict_ = {'type': type(obj), 'attributes': obj.__dict__,
             'metods': [func for func, _ in inspect.getmembers(obj, predicate=inspect.ismethod)],
             'module': inspect.getmodule(obj).__name__}
    return dict_

object = Introspector('John', 'Urban', 43)
object.write_file()

print(into_func(object))
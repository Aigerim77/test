class MetaClass(type):
    
    def __new__(cls, name, bases, dict):
        print("Создание нового класса {}".format(name))
        return type.__new__(cls, name, bases, dict)

    
    def __init__(cls, name, bases, dict):
        print("Инициализация нового класса {}".format(name))
        return super(MetaClass, cls).__init__(name, bases, dict)


SomeClass = MetaClass("SomeClass", (), {})

class Nikola:
    def __init__(self, name, age):
        object.__setattr__(self, 'age', age)
        if name.lower() == "николай":
            object.__setattr__(self, 'name', name)
        else:
            object.__setattr__(self, 'name', f"Я не {name}, а Николай")
    
    def __setattr__(self, key, value):
        raise AttributeError(f"Нельзя добавлять новый атрибут '{key}' в экземпляр класса '{self.__class__.__name__}'")


try:
    user_name = input("Введите ваше имя: ")
    user_age = int(input("Введите ваш возраст: "))  
    
    person = Nikola(user_name, user_age)
    print(f"Имя: {person.name}")
    print(f"Возраст: {person.age}")

    person.middle_name = "Аркадьевич" # Попытка добавить новый атрибут
    
except AttributeError as e:
    print(e)
except ValueError:
    print("Ошибка: введено некорректное значение для возраста.")

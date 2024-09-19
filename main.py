class Person:
    # class attribute
    person_count = 0

    # instance functions: self (örneğin yerine geçen) ön eki ile işletilen fonksiyon veya özellikler bu kısımlarda kullanılır

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.person_count += 1

        p1 = Person('İlker', 40)
        p2 = Person('İlkay', 25)

        print(p1, p1.name, p1.age, p1.person_count)
        print(p2, p2.name, p2.age, p2.person_count)

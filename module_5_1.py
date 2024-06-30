class House:
    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number

    def go_to(self, n):
        for i in range(1, n+1):
            if n <= self.number_of_floors:
                print(i)
            else:
                print('"Такого этажа не существует"')
                break

            print()



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
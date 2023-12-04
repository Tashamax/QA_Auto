car_1 = input("Введіть марку автомобіля 1: ")
car_2 = input("Введіть марку автомобіля 2: ")
car_3 = input("Введіть марку автомобіля 3: ")

class Cars:
    list_of_cars = []

    def add_car(self, car):
        Cars.list_of_cars.append(car)

    def display_cars(self):
        joined_cars = " та ".join(Cars.list_of_cars)
        print("Список авто: {}".format(joined_cars))

cars_instance = Cars()

cars_instance.add_car(car_1)
cars_instance.add_car(car_2)
cars_instance.add_car(car_3)

cars_instance.display_cars()



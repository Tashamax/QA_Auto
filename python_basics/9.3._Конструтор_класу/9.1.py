windows_count = int(input("Введіть кількість вікон: "))
floors_count = int(input("Введіть кількість поверхів: "))

class Building:
    def __init__(self, windows, floors):
        self.windows_count = windows
        self.floors_count = floors

    def total_windows_count(self):
        total_windows = self.windows_count * self.floors_count
        return total_windows

building_instance = Building(windows_count, floors_count)

result = building_instance.total_windows_count()
print("Загальна кількість вікон {}".format(result))




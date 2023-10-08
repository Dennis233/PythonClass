class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("""The total area of {} is {:.2f}.
                \rThe free area is {:.2f}.
                \rFurniture list:{}."""
                .format(self.house_type, self.area,
                        self.free_area, self.item_list))

    def add_furniture(self, item):
        print("The new furniture is {}".format(item))

        if item.area > self.free_area:
            print("The house is full. {} can't be added".format(item.name))
            return

        self.item_list.append(item.name)
        self.free_area -= item.area


class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "{} is {:.2f}".format(self.name, self.area)


bed = Furniture("bed", 40)
closet = Furniture("closet", 20)
desk = Furniture("desk", 1.5)

my_house = House("room", 50)
my_house.add_furniture(bed)
my_house.add_furniture(closet)
my_house.add_furniture(desk)
print(my_house)

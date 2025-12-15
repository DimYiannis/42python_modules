class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = int(height)
        self.age = int(age)

"""
inheritance:
flower class inherits the attributes of Plant,
we use super(). to call the constructor of the parent class

bloom method:
check whether we display a mesage based on the bloom attribute
that works as a boolean
"""
class Flower(Plant):
    def __init__(self, name, height, age, color, bloom):
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom

    def ft_bloom(self):
        if self.bloom != 0:
            message = "blooming beautifully!"
            return message
        else:
            message = "not blooming yet"
            return message


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter, shade):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = shade

    def produce_shade(self):
        if self.shade != 0:
            message = "provides 78 square meters of shade"
            return message
        else:
            message = "no shade is provided"
            return message


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

"""
funcs to create objects using the above classes
and display their attributes
"""
def ft_create_flower(n, h, a, c, bloom):
    fl = Flower(n, h, a, c, bloom)
    print(f"{fl.n} ({type(fl).__name__}): {fl.h}cm, {fl.a} days, {fl.c} color")
    print(f"{fl.n} is {fl.ft_bloom()}\n")


def ft_create_tree(n, h, a, d, shade):
    t = Tree(n, h, a, d, shade)
    print(f"{t.n} ({type(t).__name__}): {t.h}cm, {t.a} days, {t.d}cm diameter")
    print(f"{t.n} {t.produce_shade()}\n")


def ft_create_veg(name, h, age, hrv_sn, nutri_val):
    v = Vegetable(name, h, age, hrv_sn, nutri_val)
    print(f"{v.name} ({type(v).__name__}): {v.h}cm, {v.age} days, {v.hrv_sn}")
    print(f"{v.name} is rich in vitamin {v.nutri_val}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    ft_create_flower("Rose", 25, 30, "red", 1)
    ft_create_tree("Oak", 500, 1825, 50, 1)
    ft_create_veg("Tomato", 80, 90, "summer harvest", "C")

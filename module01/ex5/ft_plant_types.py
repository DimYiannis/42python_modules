class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = int(height)
        self.age = int(age)

class Flower(Plant):
    def __init__(self, name, height, age, color, bloom):
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom

    def ft_bloom(self):
        if self.bloom != 0:
            message = "blooming beautifully!\n"
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

def ft_create_flower(name, height, age, color, bloom):
    flower = Flower(name, height, age, color, bloom)
    print(f"{flower.name} ({type(flower).__name__}): {flower.height}cm, {flower.age} days, {flower.color} color")
    print(f"{flower.name} is {flower.ft_bloom()}\n")

def ft_create_tree(name, height, age, trunk_diameter, shade):
    tree = Tree(name, height, age, trunk_diameter, shade)
    print(f"{tree.name} ({type(tree).__name__}): {tree.height}cm, {tree.age} days, {tree.trunk_diameter}cm diameter")
    print(f"{tree.name} {tree.produce_shade()}\n")

def ft_create_veg(name, height, age, harvest_season, nutritional_value):
    veggie = Vegetable(name, height, age, harvest_season, nutritional_value)
    print(f"{veggie.name} ({type(veggie).__name__}): {veggie.height}cm, {veggie.age} days, {veggie.harvest_season}")
    print(f"{veggie.name} is rich in vitamin {veggie.nutritional_value}")

if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    ft_create_flower("Rose", 25, 30, "red", 1)
    ft_create_tree("Oak", 500, 1825, 50, 1 )
    ft_create_veg("Tomato", 80, 90, "summer harvest", "C")


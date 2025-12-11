class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = int(height)
        self.age = int(age)

class Flower(Plant):
    def __init__(self, name, color, bloom):
        super().__init__(name)
        self.color = color
    def ft_bloom(self):
        if bloom != 0:
            return message = "blooming beautifully!\n"
        else:
            return message = "not blooming yet"

class Tree(Plant):
    def __init__(self, name, trunk_diameter, shade):
        super().__init__(name)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self)
        if shade != 0:
            message = "provides 78 square meters of shade"
        else:
            message = "no shade is provided"

class Vegetable(Plant):
    def __init__(self, name, harvest_season, nutritional_value):
        super().__init__(name)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

def ft_create_flower(flower_name, color, bloom):
    flower = Flower(flower_name, height, age)
    print(f"{flower.flower_name} ({}): {flower.height}cm, {flower.age} days, {flower.color} color\n")
    print(f"{flower.flower_name} is {flower.bloom()}")

def ft_create_tree(tree_name, trunk_diameter, shade):
    tree = Tree(tree_name, trunk_diameter, shade)
    print(f"{tree.tree_name} ({}): {tree.height}cm, {tree.age} days, {tree.trunk_diameter}cm diameter\n")
    print(f"{tree.tree_name} {tree.produce_shade()}")

def ft_create_veg(veg_name, harvest_season, nutritional_value):
    veggie = Vegetable(veg_name, harvest_season, nutritional_value)
    print(f"{veggie.veg_name} ({}): {veggie.height}cm, {veggie.age} days, {veggie.harvest_season}")
    print(f"{veggie.veg_name} is rich in vitamin {veggie.nutritional_value}")

if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    ft_create_flower("Rose", 25, 30, "red", 1)
    ft_create_tree("Oak", 500, 1825, 50, 1 )
    ft_create_veg("Tomato", 80, 90, "summer harvest", "C")


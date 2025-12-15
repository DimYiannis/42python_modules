class Plant:
    def __init__(self, name, height, agee, growth):
        self.name = name
        self.height = int(height)
        self.agee = int(agee)
        self.growth = int(growth)

    def grow(self):
        if self.name == "Rose":
            self.height += 1
        elif self.name == "Sunflower":
            self.height += 4
        else:
            self.height += 0.5

    def age(self):
        self.agee += 1


"""
in this func we create a plant using the
plant class and display some of its attributes
"""


def ft_create(flower_name, height, agee, growth):
    p = Plant(flower_name, height, agee, growth)
    print(f"Created: {p.name} ({p.height}cm {p.agee} days)")
    return 1


"""
    count as we create new plants
"""
if __name__ == "__main__":
    count = 0
    print("=== Plant Factory Output ===")
    count += ft_create("Rose", 25, 30, 0)
    count += ft_create("Oak", 200, 365, 0)
    count += ft_create("Cactus", 5, 90, 0)
    count += ft_create("Sunflower", 80, 45, 0)
    count += ft_create("Fern", 15, 120, 0)

    print(f"\nTotal plants created: {count}")

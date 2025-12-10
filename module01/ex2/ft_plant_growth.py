class Plant:
    def __init__(self, name, height, age, growth):
        self.name = name
        self.height = int(height)
        self.age = int(age)
        self.growth = int(growth);

def grow(self):
    self.height += 1

def age(self):
    self.age += 1

def get_info():
    p1 = Plant("Rose", 25, 30, 0)
    p2 = Plant("Sunflower", 80, 45, 0)
    p3 = Plant("Cactus", 15, 120, 0)
    print("=== Garden Plant Registry ===")
    print(f"{p1.name}: {p1.height}cm, {p1.age} days old")
    print(f"{p2.name}: {p2.height}cm, {p2.age} days old")
    print(f"{p3.name}: {p3.height}cm, {p3.age} days old")
    p1.growth = p1.height
    p2.growth = p2.height
    p3.growth = p3.height

if __name__ == "__main__":
    i = 1
    print("=== Day 1 ===")
    get_info() 
    while i < 8:
        p1.grow()
        p2.grow()
        p3.grow()
        p1.age()
        p2.age()
        p3.age()
    p1.growth = p1.height - p1.growth
    p2.growth = p2.height - p2.growth
    p3.growth = p3.height - p3.growth
    print("=== Day 7 ===")
    print(f"{p1.name}: {p1.age}")
    print(f"Growth this week: {p1.growth}")


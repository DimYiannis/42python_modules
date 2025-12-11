class Plant:
    def __init__(self, name, height, agee, growth):
        self.name = name
        self.height = int(height)
        self.agee = int(agee)
        self.growth = int(growth);

    def grow(self):
        if self.name == "Rose":
            self.height += 1
        elif self.name == "Sunflower":
            self.height += 4
        else:
            self.height += 0.5

    def age(self):
        self.agee += 1

def get_info():
    p1 = Plant("Rose", 25, 30, 0)
    p2 = Plant("Sunflower", 80, 45, 0)
    p3 = Plant("Cactus", 15, 120, 0) 
    print(f"{p1.name}: {p1.height}cm, {p1.agee} days old")
    print(f"{p2.name}: {p2.height}cm, {p2.agee} days old")
    print(f"{p3.name}: {p3.height}cm, {p3.agee} days old")
    p1.growth = p1.height
    p2.growth = p2.height
    p3.growth = p3.height

    return p1, p2, p3

if __name__ == "__main__":
    i = 1
    print("=== Day 1 ===")
    p1, p2, p3 = get_info() 
    initial_height1 = p1.height 
    initial_height2 = p2.height 
    initial_height3 = p3.height
    while i < 8:
        p1.grow()
        p2.grow()
        p3.grow()
        p1.age()
        p2.age()
        p3.age()
        i += 1
    p1.growth = p1.height - initial_height1
    p2.growth = p2.height - initial_height2
    p3.growth = p3.height - initial_height3
    print("=== Day 7 ===")
    print(f"{p1.name}: {p1.agee} days old")
    print(f"Growth this week: +{p1.growth}cm")
    print(f"{p2.name}: {p2.agee} days old")
    print(f"Growth this week: +{p2.growth}cm")
    print(f"{p3.name}: {p3.agee} days old")
    print(f"Growth this week: +{p3.growth}cm")






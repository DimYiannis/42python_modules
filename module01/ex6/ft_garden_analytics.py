class GardenManager:
    def __init__(self):
        self.gardens = ()

    def create_garden(self, name):
        garden = Garden(name)
        self.gardens = self.gardens + (garden,)
        return garden

    class GardenStats:
        def __init__(self, gardens):
            self.gardens = gardens

        def total_plants(self):
            total = 0
            for g in self.gardens:
                count = 0
                for p in g.plants:
                    count += 1
                total = total + count
            return total

        def total_gardens(self):
            total = 0
            for g in self.gardens:
                total += 1
            return total

        @classmethod
        def create_garden_network(cls):
            total = 0
            for g in cls.gardens:
                total += 1
            return total

        def total_score(self):
            for g in self.gardens:
                tot = 0
                for p in g.plants:
                    tot += p.height
                    if type(p).__name__ == "PrizeFlower":
                        tot += p.points
                g.score = tot
            print(
                f"Garden scores - {self.gardens[0].name}:"
                f"{self.gardens[0].score},"
                f"{self.gardens[1].name}: {self.gardens[1].score}"
            )


class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = ()
        self.score = 0

    def add_plant(self, plant, show):
        self.plants = self.plants + (plant,)
        if show == 1:
            print(f"Added {plant.name} to {self.name}'s garden")

    def show_plants(self, total_growth):
        print(f"\n=== {self.name}'s Garden Report ===")
        print("Plants in garden:")

        total_plants = 0
        t_c = 0
        f_c = 0
        p_c = 0
        height_check = 0

        for p in self.plants:
            if type(p).__name__ == "FloweringPlant":
                print(f"- {p.name}: {p.height}cm,"
                      f"{p.color} flowers (blooming)")
                f_c += 1
                total_plants += 1
            elif type(p).__name__ == "PrizeFlower":
                message = "flowers (blooming), Prize points:"
                print(f"- {p.name}: {p.height}cm,"
                      f"{p.color} {message} {p.points}")
                p_c += 1
                total_plants += 1
            else:
                print(f"- {p.name}: {p.height}cm")
                t_c += 1
                total_plants += 1
            if p.height > 0:
                height_check = 1

        print(f"\nPlants added: {total_plants} Total growth: {total_growth}cm")
        print(f"Plant types: {t_c} regular {f_c},"
              f"flowering, {p_c}, prize flowers")
        if height_check == 1:
            print("\nHeight validation test: True")
        else:
            print("\nHeight validation test: False")

    def grow_plants(self):
        print(f"\n{self.name} is helping all plants grow...")
        total_growth = 0
        for plant in self.plants:
            growth = 1
            total_growth += growth
            plant.height += growth
            print(f"{plant.name} grew {growth}cm ")
        return total_growth


class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = int(height)


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    @classmethod
    def ft_create(cls, n, h, c):
        return cls(n, h, c)


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.name = name
        self.points = points

    @classmethod
    def ft_create(cls, n, h, c, points):
        return cls(n, h, c, points)


class Tree(Plant):
    def __init__(self, name, height):
        super().__init__(name, height)

    @classmethod
    def ft_create(cls, n, h):
        return cls(n, h)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager()
    g1 = manager.create_garden("Alice")
    g2 = manager.create_garden("Bob")

    fl1 = FloweringPlant.ft_create("Rose", 25, "red")
    tr1 = Tree.ft_create("Oak", 100)
    pf1 = PrizeFlower.ft_create("Sunflower", 50, "yellow", 10)
    fl2 = FloweringPlant.ft_create("Bananas", 10, "yellow")
    fl3 = FloweringPlant.ft_create("AAAAAAAA", 2000, "teal")

    g1.add_plant(tr1, 1)
    g1.add_plant(fl1, 1)
    g1.add_plant(pf1, 1)

    g2.add_plant(fl2, 0)
    g2.add_plant(fl3, 0)

    total_growth = g1.grow_plants()

    g1.show_plants(total_growth)

    stats = GardenManager.GardenStats(manager.gardens)
    stats.total_score()
    print("Total gardens:", stats.total_gardens())
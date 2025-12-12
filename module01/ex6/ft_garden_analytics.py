class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = ()
        self.score = 0
    
    def add_plant(self, plant):
        self.plants = self.plants + (plant,) 
   
    def show_plants(self):
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming)")

    #def stats():
    # num of plants 
    # type of plants 

# class GardenManager:
  #  count = 0
   # def __init__(self):
        
  #  @classmethod
   # def  create_garden_network(cls):
        # total scores 
        # total gardens  


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = int(height)
        self.age = int(age)


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom

    @classmethod
    def ft_create(cls, n, h, a, c):
        return cls(n, h, a, c)


        print(f"{fl.n} ({type(fl).__name__}): {fl.h}cm, {fl.a} days, {fl.c} color")
       

class PrizeFlower(FloweringPlant): 
    def __init__(self, name, points):
        super().__init__(name, height, age, color, bloom)
        self.name = name
        self.points

    @classmethod
    def ft_create(n, h, a, c, points):
        return cls(n, h, a, c, points)



class Tree(Plant):
    def __init__(self, name):
        super().__init__(name, height)

    def ft_create(n, h):
        return cls(n, h)


    @staticmethod
    def ft_create_tree(n, h, a, d, shade):
        t = Tree(n, h, a, d, shade)
        print(f"{t.n} ({type(t).__name__}): {t.h}cm, {t.a} days, {t.d}cm diameter")

 
def create_garden(name):
    g = Garden(name)
    


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    g1 = Garden("Alice")
    fl1 = FloweringPlant.ft_create("Rose", 15, 20, "red", 1)

    g1.add_plant(fl1)
    g1.show_plants()
    


    


    



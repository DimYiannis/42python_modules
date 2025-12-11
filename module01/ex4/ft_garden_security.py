class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = int(height)
        self.__age = int(age)

    def set_height(self, x):
        self.__height = x

    def set_age(self, x):
        self.__age = x

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

def ft_create(flower_name, height, age):
    p = SecurePlant(flower_name, height, age)
    print(f"Plant created: {p.name}")
    ft_check_height(p, p.get_height())
    ft_check_age(p, p.get_age())
    return p

def ft_check_age(plant, age):
    if age < 0:
        print(f"Invalid operation attempted: age {age} days [REJECTED]")
        print("Security: Negative age rejected")
    else:
        plant.set_age(age)
        print(f"Age updated: {plant.get_age()} days [OK]")

def ft_check_height(plant, height):
    if height < 0:
        print(f"Invalid operation attempted: age {height} days [REJECTED]")
        print("Security: Negative age rejected")
    else:
        plant.set_height(height)
        print(f"Height updated: {plant.get_height()} days [OK]")

def ft_update_age(plant, new_age):
    if new_age < 0:
        print(f"Invalid operation attempted: age {new_age} days [REJECTED]")
        print("Security: Negative age rejected")
        print(f"Current plant: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)")
    else:
        plant.set_age(new_age)
        print(f"Age updated: {plant.get_age()} days [OK]")
        print(f"Current plant: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)")

def ft_update_height(plant, new_height):    
    if new_height < 0:
        print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
        print("Security: Negative height rejected\n")
        print(f"Current plant: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)")
    else:
        plant.set_height(new_height) 
        print(f"Height updated: {plant.get_height()}cm [OK]")
        print(f"Current plant: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)") 

if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = ft_create("Rose", 5, 30)
    print("\n") 
    ft_update_height(plant, -5)
 #   ft_update_age(plant, 100) 
    

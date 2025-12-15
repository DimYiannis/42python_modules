"""
class of plant with attributes of 
name, height and age
"""

class Plant:
    def __init__(plant, name, height, age):
        plant.name = name
        plant.height = height
        plant.age = age
"""
displaying the attributes of the plants 
we create using the plant class
"""

if __name__ == "__main__":
    p1 = Plant("Rose", "25cm", "30 days old")
    p2 = Plant("Sunflower", "80cm", "45 days old")
    p3 = Plant("Cactus", "15cm", "120 days old")
    print("=== Garden Plant Registry ===")
    print(f"{p1.name}: {p1.height}, {p1.age}")
    print(f"{p2.name}: {p2.height}, {p2.age}")
    print(f"{p3.name}: {p3.height}, {p3.age}")

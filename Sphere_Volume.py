import math

def calculateSphereVolume(radius):
    pi = math.pi
    volume = pi * (4/3) * (radius ** 3)
    return volume

userInput = float(input("please enter a radius:\t"))
print("Sphere volume:", calculateSphereVolume(userInput))
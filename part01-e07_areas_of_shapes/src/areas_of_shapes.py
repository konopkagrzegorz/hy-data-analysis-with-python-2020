#!/usr/bin/env python3

import math


def main():
    status=True
    while (status):
        shape=input("Choose a shape (triangle, rectangle, circle): ")
        if shape=="":
            status=False
            break
        elif (shape=="triangle"):
                base=int(input("Give base of the triangle: "))
                height=int(input("Give height of the triangle: "))
                area=base*height/2
                print("The area is ", area)
        elif (shape=="rectangle"):
                width=int(input("Give width of the rectangle: "))
                height=int(input("Give height of the rectangle: "))
                area=width*height
                print("The area is ", area)
        elif (shape=="circle"):
            radius = int(input("Give radius of the circle: "))
            area = math.pi * radius**2
            print("The area is ", area)
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()

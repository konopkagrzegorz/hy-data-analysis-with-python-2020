#!/usr/bin/env python3


def main():
    def triple(number):
        return number*3
    def square(number):
        return number**2
    for i in range(1,11):
        if (square(i) <= triple(i)):
            print(f"triple({i})=={triple(i)} square({i})=={square(i)}")
    
if __name__ == "__main__":
    main()

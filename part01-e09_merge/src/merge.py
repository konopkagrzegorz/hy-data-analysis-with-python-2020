#!/usr/bin/env python3

def merge(L1, L2):
    L = L1 + L2
    L.sort()
    return L

def main():
    L1 = [1, 7, 8]
    L2 = [4, 10, 11]
    print(merge(L1,L2))
    
if __name__ == "__main__":
    main()

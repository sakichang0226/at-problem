def main():
    AB,AC,BC = input().split()

    if (AB == ">"):
        if (BC == ">"):
            return "B"
        else:
            return "C" if AC == ">" else "A"
    

    if (AC == ">"):
        if (BC == ">"):
            return "B" if AB == ">" else "A"
        else:
            return "C"
    
    return "C" if BC == ">" else "B"

if __name__ == "__main__":
    print(main())
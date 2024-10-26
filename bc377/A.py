def main():
    S = input()
    counts = {"A":0, "B": 0, "C": 0}

    for i in S:
        if (counts.get(i) == None or counts.get(i) > 0):
            return "No"
        
        counts[i] += 1
    
    return "Yes"

if __name__ == "__main__":
    print(main())
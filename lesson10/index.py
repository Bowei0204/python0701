import learning

def main():
    p1 = learning.getPerson(name="1")
    print(p1.B_print())
    
    print("==================")

    p2 = learning.Person.getPerson(name="2")
    print(p2.B_print())

if __name__ == '__main__':
    main()
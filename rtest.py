
def recursive():
    print("I like to party")
    print("Do you like to party?")
    response = party_input()

def party_input():
    print("Please insert party prefrences:")
    party = input("Party???").upper()
    if party == "PARTY":
        print("Chill")
    else:
        recursive()

recursive()

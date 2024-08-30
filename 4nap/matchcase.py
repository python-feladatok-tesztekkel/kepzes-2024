nap = input("Add meg a hét egy napját:").lower()

match nap:
    case "hétfő"|"kedd"|"szerda"|"csütörtök"|"péntek":
        print(f"A {nap} munkanap!")
    case "szombat":
        print(f"A {nap} munkaszüneti nap!")
    case "vasarnap":
        print(f"A {nap} pihenő nap!")
    case _:
        print("Elirtad a nap nevét!")
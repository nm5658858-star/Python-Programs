emails = ["saifmalik@gmail.com", "misbahgmail.com", "sundas@yahoo.com"]
for x in emails:
    if "@" in x and "." in x:
        print("\033[92m" + x + " => Real Email\033[0m")
    else:
        print("\033[91m" + x + " => Fake Email\033[0m")
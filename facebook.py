emails = ["saifmalik@facebook.com", "mark.zuckerberg@facebook.com", "sundas@yahoo.com", "pythonuser@facebook.com"]
for x in emails:
    if "@" in x and "facebook" in x:
        print(f"\033[92m" + x +" => Facebook Email\033[0m")
    else:
        print(f"\033[91m" + x + " => Not a Facebook Email\033[0m")
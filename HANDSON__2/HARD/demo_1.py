held = int(input("Enter classes held: "))
attended = int(input("Enter classes attended: "))

percentage = (attended / held) * 100

if percentage >= 75:
    print(f"{percentage:.0f}% Allowed")
else:
    medical = input("Medical cause? (Y/N): ")

    if medical.upper() == 'Y':
        print(f"{percentage:.0f}% Allowed")
    else:
        print(f"{percentage:.0f}% Not allowed")
s = input("Enter the mobile number: ")
s = s.strip()
for ch in s:
    if not (ch.isdigit() or ch in "-()"):
        print("Invalid: contains invalid characters")
        exit()

ca = s.count("-")

if s.count("(") != s.count(")"):
    print("Invalid: brackets not balanced")
    exit()

digits = "".join(ch for ch in s if ch.isdigit())

if len(digits) != 10:
    print("Invalid: must contain 10 digits")
else:
    print("Valid number")
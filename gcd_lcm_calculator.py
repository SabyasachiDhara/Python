def gcd(m, n):
    fm = []
    for i in range(1, m+1):
        if m % i == 0:
            fm.append(i)

    fn = []
    for j in range(1, n+1):
        if n % j == 0:
            fn.append(j)

    cf = [f for f in fm if f in fn]
    return cf[-1]


def lcm(m, n):
    return int(m * n / gcd(m, n))


print("## GCD & LCM CALCULATOR ##")
s = int(input("Enter 1st number: "))
t = int(input("Enter 2nd number: "))

choice = input("What do you want to calculate? (GCD / LCM): ").lower()

if choice == "gcd":
    print("GCD =", gcd(s, t))
elif choice == "lcm":
    print("LCM =", lcm(s, t))
else:
    print("ERROR: Invalid choice.")

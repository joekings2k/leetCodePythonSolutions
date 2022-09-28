
wantMore = "yes"
while wantMore == "yes":
    num=input("enter your number")
    num = int(num)
    if num %2 != 0:
        print(f"{num} is an odd number")
    elif num%2 ==0:
        print(f"{num} is an even number")
    wantMore = input("wanna continue")


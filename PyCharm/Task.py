h = int(input("hour: "))
m = int(input("minute: "))
s = int(input("second: "))
h %= 12
m %= 60
s %= 60
g = 360/12*h + 30/60*m + 30/3600*s
print("Gradus: %.3f"% g)
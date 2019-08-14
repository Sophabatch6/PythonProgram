Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
Days2 = set(["A", "B", "C", "Monday", "Tuesday"])
print(Days)
print(type(Days))
for i in Days:
    print(i)
print(Days2)
Days.discard("Monday")
print(Days)
print(Days | Days2)

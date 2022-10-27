list1 = ["Americans", "Indians"]
list2 = ["Play", "watch"]
list3 = ["Baseball","cricket"]
try:
    for i in list1:
        for j in list2:
            for k in list3:
                print(f"{i} {j} {k}")
except Exception as e:
    print(e)


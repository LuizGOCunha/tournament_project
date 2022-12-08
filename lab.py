from utilities.classes import Match, Fighter, Category
def cdl(list):
    i = 0
    nl = []
    for item in list:
        if i%2 == 0:
            try:
                sl = Match(list[i], list[i+1])
                nl.append(sl)
                print(sl)
            except IndexError:
                sl = Match(list[i])
                nl.append(sl)
                print(sl)
        i+=1
    return nl

# for i in range(10):
#     cdl(list(range(i)))
#     print("************************")

a = Fighter("asdA", 90.8, 0, 30, "M")
b = Fighter("asdB", 90.8, 0, 30, "M")
c = Fighter("asdC", 90.8, 0, 30, "M")
d = Fighter("asdD", 90.8, 0, 30, "M")
list = [a,b,c,d]
# cdl(list)

categ = Category(list)
categ.create_matches()
print("fighters", categ.return_fighters())
print("matches", categ.return_matches())
print("matches fighters", categ.return_matches()[0], categ.return_matches()[1])
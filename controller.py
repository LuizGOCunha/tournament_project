from model.fighter import Fighter
from model.category import Category

# Simple manual testing so we can be absolutely sure it is working as intended (it is)

f1 = Fighter("f1", weight=50.5, belt_number=2, age=40, sex="M")
f2 = Fighter("f2", weight=50.5, belt_number=2, age=40, sex="M")
f3 = Fighter("f3", weight=50.5, belt_number=2, age=40, sex="M")
f4 = Fighter("f4", weight=50.5, belt_number=2, age=40, sex="M")
f5 = Fighter("f5", weight=50.5, belt_number=2, age=40, sex="M")
f6 = Fighter("f6", weight=50.5, belt_number=2, age=40, sex="M")
f7 = Fighter("f7", weight=50.5, belt_number=2, age=40, sex="M")
f8 = Fighter("f8", weight=50.5, belt_number=2, age=40, sex="M")
f9 = Fighter("f9", weight=50.5, belt_number=2, age=40, sex="M")

fighter_list = [f1, f2, f3, f4, f5, f6, f7, f8, f9]

flyweight = Category(fighter_list)
flyweight.create_matches()
print(flyweight)
flyweight.resolve_category(1, 2, 2, 1, 1)
print(flyweight)
flyweight.advance_category()
print(flyweight)
flyweight.resolve_category(1, 1, 2)
print(flyweight)
flyweight.advance_category()
print(flyweight)
flyweight.resolve_category(2, 2)
print(flyweight)
flyweight.advance_category()
print(flyweight)
flyweight.resolve_category(1)
print(flyweight)

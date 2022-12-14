c = 0
d = {"a": (c>20)}

def func(d):
    c=30
    if d["a"]:
        print("True!")
    else:
        print("False")

func(d)
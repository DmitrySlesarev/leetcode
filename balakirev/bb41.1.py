# def rcs(x):
#     print(f"recursion: {x}")
#     rcs(x+1)
#
# rcs(1)
def rcs3(x):
    print(f"down: x = {x}")
    print(f"up: x = {x}")


def rcs2(x):
    print(f"down: x = {x}")
    rcs3(x-1)
    print(f"up: x = {x}")

def rcs1(x):
    print(f"down: x = {x}")
    rcs2(x-1)
    print(f"up: x = {x}")

def rcs(x):
    print(f"down: x = {x}")
    if x>1: rcs(x-1)
    print(f"up: x = {x}")


# rcs1(3)
rcs(3)
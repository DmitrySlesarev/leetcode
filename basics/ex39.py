# def get_V(a, b, c, verbose=True):
#     if verbose:
#         print(f"a = {a}, b = {b}, c = {c}")
#     return a * b * c
#
# # v = get_V(1, 2, 3)
# v = get_V(1, c=2, b = 3)
# # v = get_V(a=1, 2, b = 3)  # Error!
# v = get_V(1, c=2, b = 3, verbose = False)
# print(v)

# def cmp_str(s1, s2, reg=False, trim=True):
#     if reg:
#         s1 = s1.lower()
#         s2 = s2.lower()
#     if trim:
#         s1 = s1.strip()
#         s2 = s2.strip()
#     return s1 == s2
#
# # print(cmp_str("Python ", " Python"))
# print(cmp_str("Python ", " PYTHON", reg=True, trim=False))

def add_value(value, lst = None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

t1 = add_value(1)
t2 = add_value(2, t1)
print(t1, t2)
import pdb as debug

def add(n1, n2):
    debug.set_trace()
    return n1 + n2

a = add(5, 5)
print(a)
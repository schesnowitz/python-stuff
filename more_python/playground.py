backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchucks", "pizza slice", "sandwich from mcdonalds"]
print(id(backpack))
new_bp = [item for item in backpack[:] if item != "pizza slice"]
print(new_bp)
print(id(backpack))

data = [1,2,3,4,5]
data.reverse()
print(data)

data = ['a','b','c','d','e','f','g','h']

b = data[1]
g = data[6]
print(b, g)
b, g = g, b
print(b, g)
data[1], data[6] = data[6], data[1]
print(data)



def show_excitement():
    "I am super excited for this course!"
    return "I am super excited for this course! " * 5

print(show_excitement())
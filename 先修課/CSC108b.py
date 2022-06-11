

def vincent():
    print("Hello, its me")
    print("是我 理我呀！！")
    print("你在幹麻啊！！！！")



# vincent()
# vincent()


#                  inputs (parametes)
def tell_the_truth(name, age):
    print("Hello, My name is " + name)
    print(name + " is " + str(age) + " years old. WHAT????")
    print("Unfortunately, " + name + " will probably die with " + str(100 - age) + " years")



tell_the_truth("Vincent", 19)
tell_the_truth("Alice", 18)




def triangle_area(base, height):
    area = base * height * 0.5
    return area
    


x = triangle_area(10, 20)
print(x) # 100.0

x = triangle_area(3, 5)
print(x) # 7.5
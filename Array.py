# tuple: is a point and not changing that is mutable 

Point = (1,2,3)

print(Point)
# no append and add

# list: is a array and changeable 

names = ["MD",'Shahidul',"Islam"]

print(names)

names.append("Raihan")

print(names)

# set: is a mathematical set and uniuqe

points = {1,2,4,5}

print(points)

points.add(4)
points.add(3)

print(points)

# dictionary: is a key to value and changeable 
 
pepoles = {
     "Shahidul" : "Sylhet",
     "Raihan" : "Mirpur"
}

print(pepoles["Shahidul"])

pepoles.pop("Shahidul")

print(pepoles)

pepoles["Shahidul"] = "Mipur-1"

print(pepoles)
 
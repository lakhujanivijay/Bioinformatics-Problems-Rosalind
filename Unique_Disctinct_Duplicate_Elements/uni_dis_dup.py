
#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhujanivijay@gmail.com"
__status__ = "done"

x=[1,2,3,4,5,5,6,7,7,8,9,10,11,13]

unique_elements=[]

for i in range(0, len(x)):
    counter = 1
    for j in range(0, len(x)):
        if i!=j and x[i] ==  x[j]:
            counter+=1
    if counter==1:
        unique_elements.append(x[i])
    counter=0
duplicate_elements = list(set(x) - set(unique_elements))


print "Opening the file..."
target = open("result.txt", "w")


target.write('Original list is: ')
target.write(x)
target.write("\n")
target.write('Unique elements are: ')
target.write(unique_elements)
target.write("\n")
target.write('Duplicate elements are: ')
target.write(duplicate_elements)

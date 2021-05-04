def print_vector(x,y,z):
    print('<%s, %s, %s>' % (x, y, z))


print_vector(0, 1, 0)


tuple_vec = (1,0,1)
list_vec = [1,0,1]

# This will not work
print_vector(list_vec)

# This will work
print_vector(*list_vec)

print_vector(*tuple_vec)

gen_exp = (x*x for x in range(3))
print_vector(*gen_exp)

### Dictionary unpacking

dict_vec = {'x':1, 'y':0, 'z':1}

#This will not work
print_vector(dict_vec)
# This will work
print_vector(**dict_vec)

# This will just print out the keys
print_vector(*dict_vec)
import io
tmp_compare = -1
depth_list = []
increase = 0


with open("input.txt", 'r') as f:
	depth_list = f.readlines()
	depth_list = [line.rstrip() for line in depth_list]
	
for i in range(len(depth_list)):
	depth_list[i] = int(depth_list[i])

print(depth_list)


# comparison attempt
print("Begin comparisons checker")

for x in depth_list:
    if tmp_compare == 0:
        # assume start of file
        tmp_compare = x
    else: 
        # assume not at start of file
        if x > tmp_compare:
            # we've seen an increase
            increase += 1
            tmp_compare = x
        else:
            # a decrease or same
            tmp_compare = x

# End of comparisons
print("End of Comparisons")

print("The number of increases was: {}".format(increase))

abc = input("Happy? ")
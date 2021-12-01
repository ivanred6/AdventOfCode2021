import io
tmp_compare = 0
depth_list = []
increase = 0


with open("input.txt", 'r') as f:
	depth_list = f.readlines()
	depth_list = [line.rstrip() for line in depth_list]
	
for i in range(len(depth_list)):
	depth_list[i] = int(depth_list[i])

print(depth_list)



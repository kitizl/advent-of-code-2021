#!python3

"""
	This is Advent of Code 2021 : Day 1
	Author : Nithesh Balasubramanian
	Date : 13 April 2021
	(Never too late, amirite)
"""

def test():
	depth_data = """199
	200
	208
	210
	200
	207
	240
	269
	260
	263"""

	depth_data = list(map(int, depth_data.split("\n")))

	return depth_data

# there is probably a smarter way to do this, but i am not smart.
depth_data = []
with open("day-one-data/depth-data.txt", 'r') as f:
	contents = f.read()
	depth_data = list(map(int, contents.split("\n")))


# comment out while running code.
# depth_data = test() 

shifted_depth_data = [0] + depth_data # appending to do a magic trick with

inc_num = 0

for ds, s_ds in zip(depth_data, shifted_depth_data[:-1]):
	result = ""
	if ds-s_ds == ds:
		result = "(N/A - no previous measurement)"
	elif ds-s_ds > 0:
		result = "(increased)"
		inc_num += 1
	else :
		result = "(decreased)"
	print(f"{ds} {result}")

print(f"Number of increases : {inc_num}")
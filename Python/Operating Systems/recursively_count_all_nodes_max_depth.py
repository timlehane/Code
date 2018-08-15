import os


def disk_use(path):


global depth, maxdepth, node_count, leaf_count
total = os.path.getsize(path)
node_count += 1
depth += 1
if depth > maxdepth:
    maxdepth = depth
if os.path.isdir(path):
for filename in os.listdir(path):
childpath = os.path.join(path, filename)
total += disk_use(childpath)
else:
    leaf_count += 1
print(total, path)  # for consistency with bash du cmd
print('depth, node_count, leaf_count', depth, node_count, leaf_count)
depth -= 1
return total

path = input('\n Please enter path for disk usage :- ')
depth, maxdepth, node_count, leaf_count = 0, 0, 0, 0
print('\n Total disk use for ', path, ' is ', disk_use(path))
print('maxdepth, node_count, leaf_count', maxdepth, node_count, leaf_count)

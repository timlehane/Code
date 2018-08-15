import os


def disk_use(path):


    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_use(childpath)
            print(total, path)  # for consistency with bash du cmd
            return total

            path = input('\n Please enter path for disk usage :- ')
            print('\n Total disk use for ', path, ' is ', disk_use(path))

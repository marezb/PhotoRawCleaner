'''
This is a simple program which I wrote to solve my problem with unnecessary photo raw files.
I always make photos in 2 formats jpg and raw. I usually watch photos on my computer and remove jpgs which I don't like.
As a result I stay with a bunch of unwanted raw files on my drive which take a lot of space.
To resolve this I wrote this simple script which is checking if in folder I have 2 the same files.
If there are 2 files .jpg and .raw it means that there is jpg left approved by me, so raw file should also stay.
If there is only 1 file it means that this is a raw file which should be deleted together with jpg which had been removed before.
This script finds such files in a given folder and deletes them automatically.
'''

import os

# provide the path to folder with files you want to delete 
path=r'D:\Zdjecia\10180327'
os.chdir(path)


curdir = os.getcwd()
files = os.listdir()

print(curdir)
print(f'Amount of files in folder: {len(files)}')

# here we create list of files to compare for duplicates by creating list
# without extension .raw .jpg. .arw(for sony) file name example DSC02641.ARW
photoset = list()
for photo in files:
    photoset.append(photo[:8])

print(f'Amount of files to be checked for deletion {len(photoset)}\n')

# loop to check for duplicates and single photos
checked = {}
for x in photoset:
    if x not in checked:
        checked[x] = 1
    else:
        checked[x] += 1

# here we create list for deletion we want to delete raws which have no
# jpgs 'friend'
to_delete = list()
for name, amount in checked.items():
    if amount == 1:
        # change extension if you want to delete different raw file
        to_delete.append(name + '.ARW')

print(f'to delete: {to_delete}')

approval = input(f'\nwe have {len(to_delete)} files to delete - are you sure? "y" or "n" ')
if approval == "y":
    for byebye in to_delete:
        try:
            os.remove(byebye)
            print(f'{byebye} has been just removed')
        except Exception as e:
            print(e)
else:
    print('nothing has been deleted')

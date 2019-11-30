# photo-raw-cleaner

This is a simple program which I wrote to solve my problem with unnecessary photo raw files.
I always make photos in 2 formats jpg and raw. I usually watch photos on my computer and remove jpgs which I don't like.
As a result I stay with a bunch of unwanted raw files on my drive which take a lot of space.
To resolve this I wrote this simple script which is checking if in folder I have 2 the same files.
If there are 2 files .jpg and .raw it means that there is jpg left approved by me, so raw file should also stay.
If there is only 1 file it means that this is a raw file which should be deleted together with jpg which had been removed before.
This script finds such files in a given folder and deletes them automatically.



Example of one usage:

C:\Users\Marek\AppData\Local\Programs\Python\Python37-32\python.exe C:/Users/Marek/Dropbox/Coding/Pycharm/Projects/myprogs/raw_cleaner.py

DSC08282.ARW
DSC08282.JPG
DSC08283.ARW
DSC08283.JPG
DSC08284.ARW
DSC08284.JPG
DSC08285.ARW
DSC08285.JPG
DSC08286.ARW
DSC08286.JPG
DSC08287.ARW
DSC08287.JPG
DSC08288.ARW
DSC08288.JPG
DSC08289.ARW
DSC08289.JPG
DSC08290.ARW
DSC08290.JPG
DSC08291.ARW
DSC08291.JPG
DSC08292.ARW
DSC08293.ARW
DSC08293.JPG
DSC08294.ARW
DSC08294.JPG
DSC08295.ARW
DSC08295.JPG
DSC08296.ARW
DSC08297.ARW
DSC08297.JPG
DSC08298.ARW
DSC08298.JPG
DSC08299.ARW
DSC08299.JPG
DSC08299a.jpg
DSC08300.ARW
DSC08300.JPG
DSC08301.ARW
DSC08301.JPG
DSC08302.ARW
DSC08302.JPG
DSC08303.ARW
DSC08303.JPG
DSC08304.ARW
DSC08304.JPG
DSC08305.ARW
DSC08305.JPG
DSC08306.ARW
DSC08306.JPG
DSC08307.ARW
DSC08307.JPG
DSC08308.ARW
DSC08308.JPG
DSC08309.ARW
DSC08309.JPG
DSC08310.ARW
DSC08310.JPG
DSC08311.ARW
DSC08311.JPG
DSC08312.ARW
DSC08312.JPG
DSC08313.ARW
DSC08313.JPG
DSC08314.ARW
DSC08314.JPG
DSC08315.ARW
DSC08315.JPG
DSC08316.ARW
DSC08316.JPG
DSC08317.ARW
DSC08317.JPG
DSC08318.ARW
DSC08318.JPG
DSC08319.ARW
DSC08319.JPG
DSC08320.ARW
DSC08320.JPG
DSC08321.ARW
DSC08321.JPG

D:\Zdjecia\10180327
Amount of files in folder: 79
Amount of files to be checked for deletion 79

to delete: ['DSC08292.ARW', 'DSC08296.ARW']

we have 2 files to delete - are you sure? "y" or "n" y
DSC08292.ARW has been just removed
DSC08296.ARW has been just removed

Process finished with exit code 0

# photo-raw-cleaner

This is a simple program which I wrote to solve my problem with unnecessary photo raw files.
I always make photos in 2 formats jpg and raw. I usually watch photos on my computer and remove jpgs which I don't like.
As a result I stay with a bunch of unwanted raw files on my drive which take a lot of space.
To resolve this I wrote this simple script which is checking if in folder I have 2 the same files.
If there are 2 files .jpg and .raw it means that there is jpg left approved by me, so raw file should also stay.
If there is only 1 file it means that this is a raw file which should be deleted together with jpg which had been removed before.
This script finds such files in a given folder and deletes them automatically.

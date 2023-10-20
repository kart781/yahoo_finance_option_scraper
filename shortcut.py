import os
import glob

filename = glob.glob('*.{}'.format('csv'))

for i in filename:
    os.remove(i)
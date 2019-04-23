import os, sys, time, datetime
from myfunc import clear

clear()
print('----------- Jam untuk kuliah -----------')
print()
a = datetime.datetime.now()
print("Sekarang : ",a)
kampus = int(input('Kampus : K'))
if kampus == 1:
    b = datetime.timedelta(minutes=30)
elif kampus == 2:
    b = datetime.timedelta(minutes=45)
elif kampus == 3:
    b = datetime.timedelta(minutes=50)
else:
    print("Kampus tidak ada.")
    sys.exit()
print()
print('Kamu harus berangkat jam', datetime.datetime.time(a-b))

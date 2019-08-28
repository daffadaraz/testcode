import os, sys, time, datetime
from datetime import date
from myfunc import clear, enterinp

clear()

# Assignment
tgljadi = date(2017,4,22)
today = date.today()
lamaHari = today - tgljadi
tahun = lamaHari.days/365
bulan = lamaHari.days/30
bulantahun = bulan % 12
jam = lamaHari.days * 24
menit = jam * 60

# Output
print('------ Ambang dan Ratu -------')
print()
print("Tanggal Jadi :", tgljadi)
print("Sekarang     :", today)
print()
print("Sudah ",('%d' % tahun)," Tahun dan ",('%d'% bulantahun)," Bulan")
print()
print("Atau")
print(('%.2f' % bulan)," Bulan")
print(lamaHari.days," Hari")
print(jam," Jam")
print(jam*60," Menit")
print()
enterinp()

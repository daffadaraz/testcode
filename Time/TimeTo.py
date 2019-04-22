import os, sys, time,datetime
from datetime import date
from clear import clear

clear()

print('---------------- Sisa Waktu ----------------')
print()
print('1.  Januari   31 Hari')
print('2.  Februari  28 Hari (29 Hari Tahun Kabisat)')
print('3.  Maret     31 Hari')
print('4.  April     30 Hari')
print('5.  Mei       31 Hari')
print('6.  Juni      30 Hari')
print('7.  Juli      31 Hari')
print('8.  Agustus   31 Hari')
print('9.  September 30 Hari')
print('10. Oktober   31 Hari')
print('11. November  30 Hari')
print('12. December  31 Hari')
print('Masukkan Tanggal (dengan Angka)')
tglTujuan = int(input('Tanggal : '))
bulanTujuan = int(input('Bulan   : '))
tahunTujuan = int(input('Tahun   : '))
clear()

tujuan = date(tahunTujuan,bulanTujuan,tglTujuan)
today = date.today()
lamaHari = abs(today - tujuan)

bulan = (lamaHari.days)/30
minggu = (lamaHari.days)/7
hari  = lamaHari.days

print("Sekarang       : ",today)
print("Tanggal Tujuan : ", tujuan)
print()
print("Sisa Waktu")
print(('%.2f' % bulan)," Bulan")
print(('%.2f' % minggu)," Minggu")
print(hari," Hari")
print()

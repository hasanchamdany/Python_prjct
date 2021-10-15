#fungsi untuk menghitung RAV
def calcRAV(q, L):
  return 0.5*q*L

#fungsi untuk menghitung RBV
def calcRBV(q, L):
  return 0.5*q*L

#fungsi untuk menghitung momen maksimal
def calcMomenMax(q, L):
  return 0.125*q*(L**2)

#input variabel untuk proses hitungan
q = float(input("masukkan Nilai beban merata = "))
L = float(input("masukkan Nilai Panjang = "))

#opsi untuk pilih fitur hitungan
print("pilih opsi hitungan :" "\n" "1. hitung RAV" "\n" "2. hitung RBV" "\n" "3. hitung momen Maksimal" "\n" "**pilih angka 1-3**")
case = int(input("masukkan pilihan = "))


if case == 1:
  hasilRAV = calcRAV(q, L)
  print("hasil RAV = " , hasilRAV)
elif case == 2:
  hasilRBV = calcRBV(q, L)
  print("hasil RBV = " , hasilRBV)
elif case == 3:
  hasilMomenMax = calcMomenMax(q, L)
  print("hasil momen Max = ", hasilMomenMax)
else:
  print("pilih sesuai dengan yang ada pada Opsi hitungan ! ")


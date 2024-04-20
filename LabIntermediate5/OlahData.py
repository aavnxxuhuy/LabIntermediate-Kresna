data_toko = open("./LabIntermediate5/File IO/icecream.txt", "r") #Membaca file icecream.txt
cantumin_data = open("./LabIntermediate5/File IO/hasildata.txt", "w") #Membuat file hasildata.txt

salesData = {} #Membuat dictionary untuk menyimpan data penjualan

def mecah_data(data_toko):
  toko_1 = []
  toko_2 = []
  toko_3 = []
  baca_data = data_toko.readline() #Membaca baris pertama dari file icecream.txt
  while baca_data != "" : #Membaca file icecream.txt hingga akhirnya
    mecah_kata = baca_data.split(":") #Memisahkan kata dari file icecream.txt

    for i in range(len(mecah_kata)):
      if i != 0 :
        mecah_kata[i] = float(mecah_kata[i]) #Mengubah isi data menjadi float

    toko_1.append(mecah_kata[1])
    toko_2.append(mecah_kata[2])
    toko_3.append(mecah_kata[3])
    #Menambahkan data harga varian sesuai tokonya

    salesData[mecah_kata[0]] = [mecah_kata[1], mecah_kata[2], mecah_kata[3]] #Menambahkan data ke dictionary
    baca_data = data_toko.readline()

  tampilkan_data(salesData, toko_1, toko_2, toko_3) #Memanggil fungsi tampilkan_data

  data_toko.close()
  cantumin_data.close()
  #Menutup file


def tampilkan_data(salesData, toko_1, toko_2, toko_3):
  total_toko_1 = sum(toko_1)
  total_toko_2 = sum(toko_2)
  total_toko_3 = sum(toko_3)
  #Mentotalkan harga dari tiap toko

  cantumin_data.write("%-15s %10s %10s %10s %12s \n" % ("Rasa","Toko 1", "Toko 2", "Toko 3", "Total Harga")) #Menulis row data bagian ke file hasildata.txt

  for i in salesData:
    total_sales_rasa = sum(salesData[i])
    cantumin_data.write("%-15s %10.2f %10.2f %10.2f %12.2f \n" % (i, salesData[i][0], salesData[i][1], salesData[i][2], total_sales_rasa)) #Menulis row isi data sesuai bagiannya dan jumlah sesuai rasanya

  cantumin_data.write("%-15s %10.2f %10.2f %10.2f \n" % ("Total", total_toko_1, total_toko_2, total_toko_3,))  #Menulis row jumlah data sesuai tokonya

mecah_data(data_toko)
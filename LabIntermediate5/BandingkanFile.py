def baca_file(nama_file):
  kata = []
  file = open(nama_file, "r") #Membaca file
  while True: 
    for line in file :
      wordList = line.split() #Memisahkan kata berdasarkan spasi
      for word in wordList : 
        word = word.strip("`~!@#$%^&*()-_=+|[]{}':;?/<>.,") #Menghapus tanda baca
        kata.append(word)  # Tambahkan kata ke list
    return kata

def hitung_huruf(nama_file):
  total_huruf = len(nama_file)  # Menghitung total huruf dalam sebuah file
  huruf_unik = len(set(nama_file))  # Menghitung huruf unik dalam sebuah file
  return total_huruf, huruf_unik

# Bandingkan setiap huruf pada file alice dengan setiap huruf pada file words
def bandingkan_file(basis_data, teks_random):
  huruf_typo = []
  for huruf in teks_random:
    if huruf not in basis_data:
      huruf_typo.append(huruf) #Tambahkan huruf yang tidak ada dalam basis data ke dalam list
  return huruf_typo

def main():
  file_cerita = baca_file("./LabIntermediate5/File IO/alice.txt") #Membaca file alice

  total_huruf, huruf_unik = hitung_huruf(file_cerita) #Menghitung total huruf dan huruf unik dalam file alice
  print("Total huruf dalam file itu adalah ", total_huruf, " dan huruf unik didalamnya ada ", huruf_unik)

  basis_data = set(baca_file("./LabIntermediate5/File IO/words.txt")) #Membaca file words dan mengubahnya menjadi set agar program cepat tereksekusi

  kumpulan_typo = bandingkan_file(basis_data, file_cerita)
  kumpulan_typo = set(kumpulan_typo) #Mengubah kumpulan typo menjadi set agar tidak ada double kata yang salah
  print("Kumpulan huruf typo dalam file itu, yaitu :")
  for huruf in kumpulan_typo:
    print(huruf) #Menampilkan kumpulan typo

main()
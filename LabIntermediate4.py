#fungsi main dilaksanakan
import random

secretWord = ["software", "hardware", "internet", "database", "python", "programmer", "network", "security", "virus", "cyber", "hacker", "malware", "phishing", "spam",]
jumlah_kalah = 0
jumlah_menang = 0


def main(kalah, menang):
  print("Selamat datang, di permainan Hangmaman \nBy AAVNXX × HYOKITO_equipment x IMac Prasmul")
  hangman(kataRandom(secretWord), kalah, menang) #memanggil fungsi permainan hangman, dengan statement secretWord 

# Fungsi untuk memilih kata rahasia dan menghapus yang sudah terpilih
def kataRandom(secretWord):
  a = random.randint(0, len(secretWord)-1)
  kataTebakan = secretWord[a]
  secretWord.remove(kataTebakan)
  return kataTebakan

#fungsi jika ingin bermain hangmaman lagi
def main_lagi(kalah, menang):
  while True:
    main_lagi = input("\nApakah ada ingin bermain lagi (y/n)? ").lower()
    if main_lagi == "y":
      hangman(kataRandom(secretWord), kalah, menang)  
    elif main_lagi == "n":
      print("Terima kasih telah bermain")
      break
    else :
      print("Input tidak valid")
      continue

#fungsi untuk mengupdate display jika sudah berhasil menebak
def display(tebakan,kataRahasia, tebakan_baru): 
  update = ""
  for i in range(len(kataRahasia)):
    if kataRahasia[i] == tebakan:
      update+= tebakan
    else:
      update += tebakan_baru[i]
  #mengupdate display sesuai tebakannya
  return update

#fungsi permainan hangman dan logika berjalannya
def hangman(kataRahasia, kalah, menang):
  tebakan_baru = "_" * len(kataRahasia)
  huruf_sementara = []
  ngulang = 0
  nyawa = 6

  #jika masih ada kesempatan maka akan terus berjalan
  while nyawa > 0:
    print("\nKata yang harus ditebak adalah: ", tebakan_baru , "\nKamu punya", nyawa, "kesempatan lagi")
    tebakan = input("Masukkan huruf tebakan kamu: ").lower()

    #jika tebakan tidak satu huruf dan bukan huruf, maka akan diminta untuk input lagi
    if len(tebakan) != 1 or not tebakan.isalpha():
      print("Masukkan hanya satu huruf dan huruf hanya boleh huruf")
      continue
    #jka tebakan sudah pernah maka akan diminta untuk input lagi
    elif tebakan in huruf_sementara:
      ngulang = ngulang + 1
      if ngulang <=2 :
        print("Kamu sudah menebak huruf ini sebelumnya")
      elif ngulang <= 5 :
        print("Kamu menebak lagi huruf ini")
      else  :
        print("Ganti tebakan hurufnya ya!")
      continue
    #jika tebakan salah, maka akan diminta untuk input lagi dan nyawa dikurang 1
    elif tebakan not in kataRahasia.lower():
      huruf_sementara.append(tebakan)
      print("Kamu salah menebak hurufnya dan kehilangan 1 nyawa")
      nyawa -= 1
      continue
    #jika tebakan benar, maka akan diminta untuk input lagi dan akan update displaynya
    else:
      huruf_sementara.append(tebakan)
      print("Kamu benar menebak hurufnya")
      tebakan_baru = display(tebakan, kataRahasia, tebakan_baru)

    #jika tebakan benar, maka akan menampilkan pesan
    if "_" not in tebakan_baru:
      print("\nAkhirnya! Selesai juga menebak kata ", kataRahasia, " dengan benar! ")
      break

    #jika tebakan salah, maka akan menampilkan pesan
  if nyawa == 0 and "_" in tebakan_baru:
    print("\nSayang! kamu tidak bisa menebak katanya dengan benar! ")
    kalah += 1
  else :
    menang +=1
  print("Kamu sudang menang ", menang, " kali dan kamu sudah kalah ", kalah, " kali")
  main_lagi(kalah, menang)

main(jumlah_kalah, jumlah_menang)
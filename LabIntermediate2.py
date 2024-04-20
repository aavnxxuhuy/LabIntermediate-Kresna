def main():
  kata = "stanley"
  tebakan = "_" * len(kata)
  huruf_benar = []
  ngulang = 0
  nyawa = 6

  print("Hangmaman by aavnxx × hyokito_equipment \nJumlah huruf yang harus ditebak adalah", len(kata), "huruf")

  while nyawa > 0:
    print("\nKata yang harus ditebak adalah: ", tebakan)
    huruf_tebakan = input("Masukkan huruf tebakan kamu:").lower()

    if len(huruf_tebakan) != 1 or not huruf_tebakan.isalpha():
      print("Masukkan huruf dan hanya 1 aja yaa")
      continue

    elif huruf_tebakan in huruf_benar:
      ngulang = ngulang + 1
      if ngulang <=2 :
        print("Kamu sudah menebak huruf ini sebelumnya")
        continue
      elif ngulang <= 5 :
        print("Kamu dah nebak nFi tadi")
        continue
      else  :
        print("Ganti tebakan hurufnya!")

    elif huruf_tebakan not in kata:
      print("Tebakan salah")
      nyawa -= 1
      continue

    else:
      huruf_benar.append(huruf_tebakan)
      tebakan_baru = ""
      for i in range(len(kata)):
        if kata[i] == huruf_tebakan:
          tebakan_baru += huruf_tebakan
        else:
          tebakan_baru += tebakan[i]
      tebakan = tebakan_baru
      print("Tebakan kamu benar")
      if "_" not in tebakan:
        print("\nAkhirnya! Selesai juga menebak kata ", kata, " dengan benar!")
        break

main ()

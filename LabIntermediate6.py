class Fraction:
  #Penentuan awal bahwa numerator dan denominator itu 0
  def __init__(self):
    self.numerator = 0
    self.denominator = 0

  #Memastikan bahwa numerator dan denominator itu int dan denominator itu tidak 0
  def set_number(self, numerator, denominator):
    if (numerator is float) or (denominator is float):
      raise ValueError("Denominator and numerator must be integers")
    elif denominator == 0 :
      raise ValueError("Denominator cannot be 0")
    else:
      self.numerator = numerator
      self.denominator = denominator  

  #Menampilkan pecahannya
  def get_fraction(self):
    return f"{self.numerator}/{self.denominator}"

  #Menampilkan hasil desimalnya
  def get_float(self):
    return self.numerator/self.denominator

#Proses pengisian nilai, berdasarkan class yang telah di deklarasikan
uhuy = Fraction()
uhuy.set_number(-1,-6)
print("The fractions is ", uhuy.get_fraction(), "and the float is ", uhuy.get_float())





  
  
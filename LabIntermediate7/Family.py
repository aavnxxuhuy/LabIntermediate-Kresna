class Family:
   def __init__(self):
        self._father = "Raka"
        self._mother = "Cening"
        self._children = ["Aditya","Kresna","Ayu"]
      # Menampilkan nama ayah, bunda, dan anak

   def __iter__(self):
        self._members = [self._father, self._mother] + self._children
        return iter(self._members)
      # Menggabungkan nama ayah, bunda, dan anak menjadi satu list

keluarga = Family()

for member in keluarga:
     print (member)

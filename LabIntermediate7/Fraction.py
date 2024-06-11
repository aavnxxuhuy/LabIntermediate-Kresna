class Fraction:

    # Kode dari awal
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("The numerator and denominator must be integers.")

        if numerator == 0:
            self._numerator = 0
            self._denominator = 1
        else:
            if (numerator < 0 and denominator >= 0) or (numerator >= 0 and denominator < 0):
                sign = -1
            else:
                sign = 1
            a = abs(numerator)
            b = abs(denominator)
            while a % b != 0:
                tempA = a
                tempB = b
                a = tempB
                b = tempA % tempB
            self._numerator = abs(numerator) // b * sign
            self._denominator = abs(denominator) // b

    # Kode untuk menambahkan pecahan
    def __add__(self, rhsValue):
        num = (self._numerator * rhsValue._denominator + self._denominator * rhsValue._numerator)
        den = self._denominator * rhsValue._denominator
        return Fraction(num, den)

    # Kode untuk mengurangi pecahan
    def __sub__(self, rhsValue):
        num = (self._numerator * rhsValue._denominator - self._denominator * rhsValue._numerator)
        den = self._denominator * rhsValue._denominator
        return Fraction(num, den)

    # Kode untuk mengalikan pecahan
    def __mul__(self, rhsValue):
        num = self._numerator * rhsValue._numerator
        den = self._denominator * rhsValue._denominator
        return Fraction(num, den)

    # Kode untuk menambahkan pecahan
    def __truediv__(self, rhsValue):
        num = self._numerator * rhsValue._denominator
        den = self._denominator * rhsValue._numerator
        return Fraction(num, den)

    # Kode untuk menampilkan pecahan secara lengkap
    def __repr__(self):
        return f"{self._numerator}/{self._denominator}"
 
# Contoh
frac1 = Fraction(3, 4)
frac2 = Fraction(1, 2)

# penambahan
print(frac1 + frac2)  

# pengurangan
print(frac1 - frac2)  

# perkalian
print(frac1 * frac2) 

# pembagian
print(frac1 / frac2) 
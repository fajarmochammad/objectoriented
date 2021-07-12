class Segitiga():
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return 'penggunaan package segitiga'

    def hitung_luas(self):
        return (self.alas * self.tinggi)/2


s1 = Segitiga(4,5)
print (s1.hitung_luas())
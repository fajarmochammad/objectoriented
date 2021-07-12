class PersegiPanjang:
    def __init__(self, p, l):
        self.p = p
        self.l = l

    def info(self):
        return 'package persegipanjang'

    def hitung_luas(self):
        return self.p * self.l


p1 = PersegiPanjang(3,4)
print (p1.hitung_luas())

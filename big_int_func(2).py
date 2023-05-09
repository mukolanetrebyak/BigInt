class BigNumbers:
    def __init__(self, value=0):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
    def setHex(self, hex_string):
        self.value = int(hex_string, 16)
    
    def getHex(self):
        return hex(self.value)[2:]
    
    def INV(self):
        return BigNumbers(~self.value)
    
    def XOR(self, other):
        return BigNumbers(self.value ^ other.value)
    
    def OR(self, other):
        return BigNumbers(self.value | other.value)
    
    def AND(self, other):
        return BigNumbers(self.value & other.value)
    
    def shiftR(self, n):
        return BigNumbers(self.value >> n)
    
    def shiftL(self, n):
        return BigNumbers(self.value << n)

# тест
a = BigNumbers()
b = BigNumbers()
c = BigNumbers()
a.setHex("e035c6cfa42609b998b883bc1699df885cef74e2b2cc372eb8fa7e7")
b.setHex("5072f028943e0fd5fab3273782de14b1011741bd0c5cd6ba6474330")
c = a.AND(b)
print(c.getHex())

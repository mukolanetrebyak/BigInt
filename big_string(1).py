class BigNumbers:
    def __init__(self, digits):
        self.digits = digits
        self.size = len(digits)
    
    @classmethod
    def from_hex_string(cls, hex_string):
        digits = []
        for i in range(0, len(hex_string), 8):
            digits.append(int(hex_string[i:i+8], 16))
        return cls(digits)
    
    def to_hex_string(self):
        hex_string = ""
        for i in range(self.size):
            hex_string += format(self.digits[i], '08x')
        return hex_string
    
    def set_number(self, hex_string):
        self.digits = []
        for i in range(0, len(hex_string), 8):
            self.digits.append(int(hex_string[i:i+8], 16))
        self.size = len(self.digits)

my_num = BigNumbers([0xFFFFFFFF, 0x12345678])
my_num.set_number("ABCDEF0123456789")
hex_string = my_num.to_hex_string()
print(hex_string)  


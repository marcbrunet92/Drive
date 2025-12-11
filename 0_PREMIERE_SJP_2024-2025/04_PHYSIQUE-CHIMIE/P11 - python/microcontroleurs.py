import serial,time


class arduino():
    def __init__(self,port):
        self.serie = serial.Serial(port,baudrate=115200)
        synchro = ord(self.serie.read())
        while synchro != 0:
            synchro = ord(self.serie.read())

    def sortie_numerique(self,pin,etat):
        self.serie.write(chr(1).encode('latin-1'))
        self.serie.write(chr(pin).encode('latin-1'))
        self.serie.write(chr(etat).encode('latin-1'))

    def entree_numerique(self,pin):
        self.serie.write(chr(2).encode('latin-1'))
        self.serie.write(chr(pin).encode('latin-1'))
        val=ord(self.serie.read())
        return val

    def sortie_analogique(self,pin,val):
        self.serie.write(chr(3).encode('latin-1'))
        self.serie.write(chr(pin).encode('latin-1'))
        self.serie.write(chr(val).encode('latin-1'))

    def entree_analogique(self,pin):
        self.serie.write(chr(4).encode('latin-1'))
        self.serie.write(chr(pin).encode('latin-1'))
        val1=ord(self.serie.read())
        val2=ord(self.serie.read())
        return val1*256 + val2

    def son(self,pin,freq,duree=0):
        self.serie.write(chr(5).encode('latin-1'))
        self.serie.write(chr(pin).encode('latin-1'))
        self.serie.write(chr(freq>>8 & 255).encode('latin-1'))
        self.serie.write(chr(freq & 255).encode('latin-1'))
        self.serie.write(chr(duree>>8 & 255).encode('latin-1'))
        self.serie.write(chr(duree & 255).encode('latin-1'))
        time.sleep(duree/1000)

    def module_us(self,echo,trig):
        self.serie.write(chr(6).encode('latin-1'))
        self.serie.write(chr(echo).encode('latin-1'))
        self.serie.write(chr(trig).encode('latin-1'))
        val1=ord(self.serie.read())
        val2=ord(self.serie.read())
        return val1*256 + val2

    def resistance_pt100(self,cs,di,do,clk):
        self.serie.write(chr(7).encode('latin-1'))
        self.serie.write(chr(cs).encode('latin-1'))
        self.serie.write(chr(di).encode('latin-1'))
        self.serie.write(chr(do).encode('latin-1'))
        self.serie.write(chr(clk).encode('latin-1'))
        val1=ord(self.serie.read())
        val2=ord(self.serie.read())
        return 430*(val1*256 + val2)/32768

    def fermer(self):
        self.serie.close()
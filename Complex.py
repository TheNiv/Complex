import math
def main():


    class ComplexNum:
        def __init__(self,real,imaginary=0.0):
            self.real=real
            self.imaginary=imaginary

        def getCis(self):#Returns the complex number with the cis format
            r=math.sqrt(pow(self.real,2)+pow(self.imaginary,2))
            Q=math.degrees(math.atan(abs(self.imaginary)/abs(self.real)))
            return Cis(r,Q)


        def getReal(self):
            return self.real

        def getImg(self):
            return self.imaginary

        def getConverse(self):
            return ComplexNum(self.real,-self.imaginary)



        def cRoot(self,n=2):
            cis=self.getCis()
            r=cis.getQ()
            Q=cis.getR()
            real=(r**(1/n))*(math.cos(math.radians(Q/n)))
            imaginary=(r**(1/n))*math.sin(math.radians(Q/n))
            return ComplexNum(real,imaginary)

        def solutions(self,n=2):#returns an array of the solutions of the equation z^n=self
            cis = self.getCis()
            r = cis.getR()
            Q = cis.getQ()
            solutions=[]
            k=0
            for i in range(n):
                solutions.append(Cis((r**(1/n)),Q/n+360*k/n).toNormal())
                k=k+1
            return solutions

        def sum(self,cnums):#Sums the numbers in an array and returns it
            try:
                sum = ComplexNum(0)
                for cnum in cnums:
                    if not isinstance(cnum, ComplexNum):
                        raise TypeError
                    sum=sum+cnum
                return sum
            except TypeError:
                print('if not isinstance(cnum,ComplexNum):')

        def __pow__(self, power, modulo=None):#Defnition of ** between 2 Cis instances
            cis=self.getCis()
            cis.r=cis.getR()**power
            cis.Q=cis.getQ()*power
            return cis


        def __truediv__(self, cnum):#Defnition of / between 2 Complex instances
            try:
                if not isinstance(cnum,ComplexNum):
                    raise TypeError
                converse = ComplexNum(cnum.getReal(), -cnum.getImg())
                up = self * converse
                down = cnum * converse
                real = up.getReal() / down.getReal()
                imaginary = up.getImg() / down.getReal()
                return ComplexNum(real, imaginary)
            except TypeError:
                print('TypeError.Type should be a ComplexNum instance')


        def __mul__(self, cnum):#Defnition of * between 2 Complex instances
            try:
                if not isinstance(cnum,ComplexNum):
                    raise TypeError
                img = self.imaginary * cnum.getReal() + cnum.getImg() * self.real
                real = self.real * cnum.getReal()-self.imaginary * cnum.getImg()
                return ComplexNum(real,img)
            except TypeError:
                print('TypeError.Type should be a ComplexNum instance')

        def __sub__(self, cnum):#Defnition of - between 2 Complex instances
            try:
                if not isinstance(cnum,ComplexNum):
                    raise TypeError
                return ComplexNum(self.real - cnum.getReal(),self.imaginary - cnum.getImg())
            except TypeError:
                print('TypeError.Type should be a ComplexNum instance')

        def __add__(self, cnum):#Defnition of + between 2 Complex instances
            try:
                if not isinstance(cnum,ComplexNum):
                    raise TypeError
                return ComplexNum(self.real + cnum.getReal(),self.imaginary + cnum.getImg())
            except TypeError:
                print('TypeError.Type should be a ComplexNum instance')

        def __repr__(self):#The format you get after using repr(Complex instance)
            return 'Complex({0},{1})'.format(self.real,self.imaginary)

        def __str__(self):#the format of printing Cis instance or using str(Complex instance)
            return f'{self.real}-{abs(self.imaginary)}i'if self.imaginary<0 else  f'{self.real}+{self.imaginary}i'

    class Cis(ComplexNum):
        def __init__(self, r, Q):
            self.r = r
            self.Q = Q
            ComplexNum.__init__(self, r * math.cos(math.radians(Q)), r * math.sin(math.radians(Q)))

        def getConverse(self):#Returns the converse of the number
            num=Cis(self.r,-self.Q)
            return num

        def getR(self):#Returns the radius of the number
            return self.r

        def getQ(self):#Returns the angle of the number
            return self.Q

        def toNormal(self):#Returns the Cis instance as normal complex num
            return ComplexNum (self.r*math.cos(math.radians(self.Q)),self.r*math.sin(math.radians(self.Q)))

        def solutions(self,n=2):#returns an array of the solutions of the equation z^n=self
            cis = self.getCis()
            r = cis.getR()
            Q = cis.getQ()
            solutions=[]
            k=0
            for i in range(n):
                solutions.append(Cis((r**(1/n)),Q/n+360*k/n))
                k=k+1
            return solutions

        def __truediv__(self, cnum):#Defnition of / between 2 Cis instances
            try:
                if not isinstance(cnum,Cis):
                    raise TypeError
                if self.getR()==cnum.getR():
                    Q = self.getQ() - cnum.getQ()
                    return Cis(self.getR(),Q)
                else:
                    selfNormal=ComplexNum(self.real,self.imaginary)
                    cnumNormal=ComplexNum(cnum.getReal(),cnum.getImg())
                    return ComplexNum.__truediv__(selfNormal,cnumNormal).getCis()
            except TypeError:
                print('TypeError.Type should be a ComplexNum instance')

        def __mul__(self, cnum):#Defnition of * between 2 Cis instances
            try:
                if not isinstance(cnum,Cis):
                    raise TypeError
                if self.getR()==cnum.getR():
                    Q=self.getQ()+cnum.getQ()
                    return Cis(self.getR(),Q)
                else:
                    return ComplexNum.__mul__(self,cnum).getCis()
            except TypeError:
                print('TypeError.Type should be a ComplexNum instance')

        def __pow__(self, power, modulo=None):#Defnition of ** between 2 Cis instances
                return Cis(self.r**power,self.Q*power)

        def __add__(self, cnum):#Defnition of + between 2 Cis instances
            return ComplexNum.__add__(self,cnum).getCis()


        def __repr__(self):#The format you get after using repr(Cis instance)
            return 'Cis({0},{1})'.format(self.r,self.Q)

        def __str__(self):#the format of printing Cis instance or using str(Cis instance)
            return f'{self.r} cis {self.Q}(degrees)'

        def __getitem__(self, item):#returns a[item]
            pass
        def __setitem__(self, key, value):#a[key]=value
            pass
        def __delitem__(self, key):#del a[key]
            pass







if __name__ == '__main__':
        main()
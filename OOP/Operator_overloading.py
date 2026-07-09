class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,other):
        return self.num + other.num
    def __mul__(self,other):
        return self.num * other.num
    def __sub__(self,other):
        return self.num - other.num
    def __truediv__(self,other):
        return self.num / other.num
    def __eq__(self,other):
        return self.num == other.num
    def __gt__(self,other):
        return self.num > other.num
    def __ls__(self,other):
        return self.num < other.num
    
n1 = 30
n2 = 67

print("Addition:", n1 + n2)
print("Multiplication:", n1 * n2)
print("Substraction:", n1 - n2)
print("Division:", n1 / n2)
print("Equal:", n1 == n2)
print("Greater than:", n1 > n2)
print("Lesser than:", n1 < n2) 
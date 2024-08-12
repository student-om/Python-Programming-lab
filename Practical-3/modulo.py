def modulo(a,b):
  z=a//b #floor division -> 5//2=2, -5//2=-3  ->  go on the left side
  mul=(b*z)
  return a-mul
# formula -> divident = (divisor*quotient)+rem
#rem = dividend - (divisor*quotient)

def fun(x):
  return x+1

x=(modulo(9,2))
print((modulo(-9,2)))
print((modulo(-7,3)))


print(x)
  
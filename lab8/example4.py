def binary_to_dec(b):
  sum_=0
  x=len(b)-1
  for i in range(len(b)):
    sum_+=int(b[i])*(2**x)
    x-=1
  return sum_
def dec_to_binary(d):
  b=""
  while d>0:
    b+=str(d%2)
    d//=2
  
  return b[::-1]

def main():
  print(binary_to_dec("10010"))
  print(dec_to_binary(18))

main()
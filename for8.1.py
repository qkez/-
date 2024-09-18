for x in range  (0,1000000):
 num1 = x//100000
 num2 = x//10000 % 10
 num3 = x//1000 % 10
 num4 = x//100 % 10
 num5 = x//10 % 10
 num6 = x % 10

 if (num1 + num2 + num3 + num4 + num5 + num6) == 13:
     if 9<x<100:
         print(f"0000{x}")
     elif  99<x<1000:
         print(f"000{x}")
     elif 999 <x<10000:
         print(f"00{x}")
     elif 9999 <x<100000:
         print(f"0{x}")
     else:
         print(x)
else:
    pass


i=0
f=1 
s=20
while i<100:

    if s < 1: 
        print(f)
        break
    s=s-3
    f=f+s
    f=f+2
    i+=1




i=0
t=0
s=0
while i < 100 :
    if s > 10:
        print(t)
        break
    t = t + 2 * s
    s = s + 2
    i += 1



s1= int(input())
s2= int(input())
s3= int(input())

if (s1>s2 and s1>s3):
    print(f"{s1} en büyük sayidir")
elif (s2>s1 and s2>s3):
    print(f"{s2} en büyük sayidir")
elif (s3>s2 and s3>s1):
    print(f"{s3} en büyük sayidir")




tt = 0
tç = 0
i = 1

while i < 1000:
    if i > 99:
        print(f"1 den 99 a kadar olan tek sayıların toplamı: {tt}/ 1 den 99 a kadar olan çift sayıların toplamı : {tç}")
        break
    tt = tt + i
    tç = tç + i +1
    i = i + 2



tt = 1
tç = 2
i = 1

while i < 1000:
    if i > 3:
        print(f"1 den 99 a kadar olan tek sayıların çarpımı : {tt}/ 1 den 99 a kadar olan çift sayıların çarpımı : {tç}")
        break
    tt = tt * i
    tç = tç *(i + 1)
    i = i + 2



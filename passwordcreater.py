import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
k = ""
a = int(input("şifrenizin uzunluğunu girin"))
for  j in range(a):
    i = random.choice(karakterler)
    k += i
print(k)

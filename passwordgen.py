import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols=",./;'\][{]:()*%$#@!"
all=lower+upper+symbols
length=(int)(input("enter length\n"))

password="".join(random.sample(all,length))
print(password)
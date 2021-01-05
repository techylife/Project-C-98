import os
import shutil

main = "./mainfile.txt"
troll = "./trollfile.txt"
f_main = open(main)
mainText = f_main.readlines()
f_troll = open(troll)
trollText = f_troll.readlines()

# for line in f_main :
#     sentence = line.split('.')

print(mainText,"\n",trollText)
dest = shutil.copy(troll,main)
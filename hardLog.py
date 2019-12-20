from whatsParser import *
import matplotlib.pyplot as plt
users=getUsers("text/jose.txt")
print(users)

for i in users:
    if(i.name==None):
        continue
    else:

        i.analysis_log(True)

plt.show()

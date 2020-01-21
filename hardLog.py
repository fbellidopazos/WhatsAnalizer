from object_conversation import conversation
import matplotlib.pyplot as plt
from whatsParser import getUsers

conv=conversation("text/log.txt")

conv.conv_log()

plt.show()
'''

users=getUsers("text/jose.txt")

users[2].analysis_log(False)
plt.show()
'''

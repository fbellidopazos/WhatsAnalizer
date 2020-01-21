# WhatsAnalizer
## Contents
* hardLog.py  -- Unifies the whole program
* whatsParser.py -- Extract the messages and author from a whastApp log
* objects_user_message.py -- Python Objects User and Message
* objects_conversation.py -- Python Object Conversation
* Test.py -- Some PyTest to check some certain functions
## How To
1. Clone Repository
1. Get WhatsApp log txt (From WhatsApp)
1. edit/create "main/hardLog"

  #### Group Analize
```python
from object_conversation import conversation
import matplotlib.pyplot as plt
from whatsParser import getUsers
conv=conversation("text/log.txt")
conv.conv_log()
plt.show()
```
#### Single Analize
Edit users[2] to get the user
```Python
from object_conversation import conversation
import matplotlib.pyplot as plt
from whatsParser import getUsers
users=getUsers("text/jose.txt")
users[2].analysis_log(False)
plt.show()
```
4. Run

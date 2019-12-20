import re
import objects_user_messages as ob


def isDate(str):
    '''
    Returns True if str matches "dd/mm/yy hh:mm".
    Else False
    :param str:
    :return boolean:
    '''
    if(bool(re.search(r"[\d]{1,2}/[\d]{1,2}/[\d]{1,2} [\d]{1,2}:[\d]{1,2}",str))):
        stuff=str.split("-")

        date=stuff[0].split(" ")[0]
        time = stuff[0].split(" ")[1]
        dd,mm,yy = date.split("/")
        hh,min = time.split(":")
        return 1<=int(dd)<=31 and 1<=int(mm)<=12 and 0<=int(yy) and 0<=int(hh)<=23 and 0<=int(min)<=59

    return False


def startsWithAuthor(s):
    '''
    Returns True if s matches a name or phone number.
    Else False
    :param s:
    :return boolean:
    '''
    patterns = [
        '([\w]+):',                        # First Name
        '([\w]+[\s]+[\w]+):',              # First Name + Last Name
        '([\w]+[\s]+[\w]+[\s]+[\w]+):',    # First Name + Middle Name + Last Name
        '([+]\d{2} \d{5} \d{5}):',         # Mobile Number (India)
        '([+]\d{2} \d{3} \d{3} \d{4}):',   # Mobile Number (US)
        '([+]\d{2} \d{4} \d{7})'           # Mobile Number (Europe)
    ]
    pattern = '^' + '|'.join(patterns)
    result = re.match(pattern, s)
    if result:
        return True
    return False


def getDataPoint(line:str):
    '''
    Splits a line in date,time,author and message
    :param line:
    :return date,time,author, message:
    '''
    # line = 18/06/17, 22:47 - Loki: Why do you have 2 numbers, Banner?
    splitLine = line.split(' - ')  # splitLine = ['18/06/17, 22:47', 'Loki: Why do you have 2 numbers, Banner?']

    dateTime = splitLine[0]  # dateTime = '18/06/17, 22:47'

    date, time = dateTime.split(' ')  # date = '18/06/17'; time = '22:47'

    message = ' '.join(splitLine[1:])  # message = 'Loki: Why do you have 2 numbers, Banner?'

    if message.__contains__(":"):  # True
        splitMessage = message.split(': ')  # splitMessage = ['Loki', 'Why do you have 2 numbers, Banner?']
        author = splitMessage[0]  # author = 'Loki'
        message = ' '.join(splitMessage[1:])  # message = 'Why do you have 2 numbers, Banner?'
    else:
        author = None
    return date, time, author, message


def author_in_users(users,name):
    for i in range(0,len(users)):
        if ( users[i].name==name):
            return i
    return -1

def getUsers(filepath:str):
    '''
    :param filepath:
    :return UsersArray:
    '''
    # Inicialize the values to be used
    users=[]
    splitted_data=[]
    # Open WhatsApp Log
    f=open(filepath,'r',encoding="utf8")

    '''
    We detect a whole line/message and save it 
    Detection done by the date 
        if it start with date then is a new line
        else it is the continuation of the previous
    '''
    for i in f:
        if(isDate(i)):
            splitted_data.append(i)
        else:
            splitted_data[len(splitted_data)-1]+=i
    '''
    We get  date, time, author, message  from a given line
        If the author did not exist in Users Array then we add it 
        else we add message to that user
    '''
    for i in splitted_data:
        try:
            date, time, author, message = getDataPoint(i)
        except:
            print("Error\n==================================================================================")
            print(i)
        index=author_in_users(users,author)
        if index!=-1:
            aux_message=ob.message(date,time,message)
            users[index].add_message(aux_message)
        else:
            aux_user=ob.user(author)
            aux_message = ob.message(date, time, message)
            aux_user.add_message(aux_message)
            users.append(aux_user)

    return users



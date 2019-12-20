import unittest
import objects_user_messages as ob
from whatsParser import *

class Tester(unittest.TestCase):

    def test_message_contructor(self):
        message=ob.message("2/12/19","20:33","This is a test message")
        self.assertEqual("2/12/19", message.date)
        self.assertEqual("20:33",message.time)
        self.assertEqual("This is a test message",message.text)

    def test_message_length(self):
        message=ob.message("2/12/19","20:33","This is a test message")

        self.assertEqual(len(message),22)

    def test_message_count(self):
        message = ob.message("2/12/19", "20:33", "This is a test message")

        self.assertEqual(message.count_symbol("s"),5)
        self.assertEqual(message.count_symbol("t"),2)
        self.assertEqual(message.count_symbol("T"),1)

    def test_message_weekday(self):
        message1 = ob.message("2/12/19", "20:33", "This is a test message")
        message2 = ob.message("2/13/19", "20:33", "This is a test message")
        message3 = ob.message("31/12/19", "20:33", "This is a test message")

        self.assertEqual(message1.week_day(),"Monday")
        self.assertEqual(message3.week_day(),"Tuesday")
        with self.assertRaises(ValueError):
            message2.week_day()

    def test_get_hour(self):
        message = ob.message("2/12/19", "20:33", "This is a test message")
        self.assertEqual(message.get_hour(),20)

    def test_user_constructor(self):
        user=ob.user("Fernando Bellido")

        self.assertEqual(user.name,"Fernando Bellido")
        self.assertEqual(user.messages,[])

    def test_user_constructor2(self):
        with self.assertRaises(TypeError):
            user = ob.user("Fernando Bellido", ob.message("44616", "46", "Message"))

    def test_user_total_message(self):
        user=ser=ob.user("Fernando Bellido")
        self.assertEqual(user.total_messages(),0)

    def test_user_add_message(self):
        user =  ob.user("Fernando Bellido")
        self.assertEqual(user.total_messages(), 0)
        user.add_message(ob.message("2/12/19","-","M1"))
        user.add_message(ob.message("2/12/19", "-", "M2"))
        user.add_message(ob.message("2/12/19", "-", "M3"))
        self.assertEqual(user.total_messages(),3)
        user.add_message(ob.message("22/12/19", "-", "M4"))
        self.assertEqual(user.total_messages(),4)
        user.add_message(ob.message("223/12/19", "-", "M6"))
        self.assertEqual(user.total_messages(), 5)

    def test_user_add_message2(self):
        user =  ob.user("Fernando Bellido")
        m1=ob.message("2/12/19","-","M1")
        m2=ob.message("2/12/19", "-", "M2")
        m3=ob.message("2/12/19", "-", "M3")
        m4=ob.message("22/12/19", "-", "M4")
        m5=ob.message("22/12/19", "-", "M4")

        user.add_message(m1)
        user.add_message(m2)
        user.add_message(m3)
        user.add_message(m4)
        user.add_message(m5)

        self.assertEqual(user.messages[0],[m1,m2,m3])
        self.assertEqual(user.messages[1], [m4, m5])

        self.assertEqual(user.total_messages(),5)
    def test_whatsParser_isDate(self):
        str = "6/12/19"
        str2 = "6/12/19 9:43"
        str3 = "50/12/19 9:43"
        str4 = "6/12/19 25:61"
        str5 = "50/13/0000 25:69"
        self.assertEqual(isDate(str),False,f"{str} : {False}")
        self.assertEqual(isDate(str2),True,f"{str2} : {True}")
        self.assertEqual(isDate(str3),False,f"{str3} : {False}")
        self.assertEqual(isDate(str4),False,f"{str4} : {False}")
        self.assertEqual(isDate(str5), False, f"{str5} : {False}")
    def test_user_toString(self):
        userA=ob.user(None)
        userB=ob.user("Fernando")
        arr=[userA,userB]
        self.assertEqual(str(userA),"None")
        self.assertEqual(str(userB),"Fernando")
        self.assertEqual(repr(userA), "None")
        self.assertEqual(repr(userB), "Fernando")
        self.assertEqual(str(arr),"[None, Fernando]")






if __name__ == '__main__':
    unittest.main()
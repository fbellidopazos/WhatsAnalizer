import matplotlib.pyplot as plt
from whatsParser import getUsers
class conversation:
    def __init__(self,dir):
       self.users=getUsers(dir)
       for i in self.users:
            if(i.name==None):
                self.users.remove(i)
                break

    def hardLog(self):
        for i in self.users:
            i.analysis_log(True)
        plt.draw()

    def comparison(self):

        labels=[]
        values=[]
        for i in self.users:
            nums=i.total_messages()
            labels.append(f"{i.name} : {nums}")
            values.append(nums)
        plt.title("Number of messages comparison")
        plt.pie(values,labels=labels,shadow=True,autopct="%1.1f%%")



    def weeday_comparison(self):

        for i in self.users:
            i.weekday_analysis(False,False)
        plt.title(f"Comparison Weekday")
        plt.legend(self.users)

    def hour_comparison(self):

        for i in self.users:
            i.hour_analysis(False,False)
        plt.title(f"Comparison Hour")
        plt.legend(self.users)

    def average_length_comparison(self):

        values=[]
        labels=[]
        for i in self.users:
            val=i.average_length()
            values.append(val)
            labels.append(f"{i.name} : {val}")
        plt.pie(values,labels=labels,shadow=True,autopct="%1.1f%%")
        # draw circle
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.title("Average length Comparison")

    def conv_log(self):
        plt.figure("Conversation Analysis")

        plt.subplot(2, 2, 1)
        self.comparison()
        plt.subplot(2, 2, 2)
        self.weeday_comparison()
        plt.subplot(2, 2, 3)
        self.hour_comparison()
        plt.subplot(2, 2, 4)
        self.average_length_comparison()

        plt.subplots_adjust(left=0.03, bottom=0.05, right=0.97, top=0.95, wspace=0.13, hspace=0.16)
        plt.draw()
        plt.figure("Conversation Analysis 2")
        self.conv_day_log()
        plt.draw()
    def conv_day_log(self):
        for i in self.users:
            i.daily_quantity_analysis(True,False,False)
        plt.title("Day Comparison")
        plt.legend(self.users)
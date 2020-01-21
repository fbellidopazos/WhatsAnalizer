import calendar
import matplotlib.pyplot as plt
from datetime import date,timedelta
from collections import OrderedDict
# https://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates/7274316
class user:
    def __init__(self,name):
        self.name=name
        self.messages=[]


    def total_messages(self):
        res = 0
        for i in self.messages:
            res += len(i)

        return res


    def add_message(self,message):
        if(self.total_messages()==0):
            self.messages.append([message])
        elif(self.messages[len(self.messages)-1][0].date==message.date):
            self.messages[len(self.messages) - 1].append(message)
        else:
            self.messages.append([message])

    def print_all_messages(self):
        for i in self.messages:
            for j in i:
                print(f"\n============================================================================="
                      f"\nMessage :\n {j.text}")

    def average_messages(self):
        return self.total_messages()/len(self.messages)
    def average_length(self):
        total_length=0
        total_messages=0
        for i in self.messages:
            for j in i:
                total_length+=len(j)
                total_messages+=1

        return total_length/total_messages

    def average_hour(self):
        hours = [0 for i in range(0, 24)]
        for i in self.messages:
            for j in i:
                hours[j.get_hour()] += 1
        return sum(hours)/24
    def find_day(self,dd,mm,yy):
        for i in self.messages:
            yy2,mm2,dd2=i[0].get_date()
            if(dd2==dd and mm2==mm and yy2==yy):
                return i
        return -1
    def daily_quantity_analysis(self,withGaps:bool,images=True,average=True):
       # fig=plt.figure()
        x_axis=[]
        y_axis=[]
        y_images=[]
        if(withGaps):
            first_day=None


            for i in self.messages:
                aux_year, aux_month, aux_day = i[0].get_date()
                last_day = date(aux_year, aux_month, aux_day)
                if(first_day!=None):
                    delta = last_day - first_day
                    for j in range(delta.days):
                        day = first_day + timedelta(days=j)
                        # Append en los arrays
                        x_axis.append(f"{day.day}/{day.month}/{day.year-2000}")
                        y_axis.append(0)
                        if images:
                            y_images.append(0)

                x_axis.append(i[0].date)
                y_axis.append(len(i))
                if images:
                    y_images.append(self.count_images_aDay(i))
                first_day=last_day+timedelta(days=1)



        else:
            for i in self.messages:
                x_axis.append(i[0].date)
                y_axis.append(len(i))
                if images:
                    y_images.append(self.count_images_aDay(i))

        plt.bar(x_axis,y_axis)
        if images:
            plt.bar(x_axis,y_images)
        if average:
            average=self.average_messages()
        plt.xlabel("Days")
        plt.ylabel("Number of Messages")
        plt.xticks(x_axis, x_axis, fontsize=float(5.5),rotation='vertical')
        if average:
            plt.axhline(y=average,linewidth=1, color='k')
        if images:
            plt.legend(["Average","NºMessages","NºImages/Vids/Stickers/..."],prop={'size': 6})
        plt.title(f' {self.name} - daily_quantity_analysis')
        #plt.show()

    def hour_analysis(self,images=True,average=True):
        #fig=plt.figure()
        x_axis=[i for i in range(0,24)]
        y_axis=[0 for i in range(0,24)]
        y_images=[0 for i in range(0,24)]
        for i in self.messages:
            for j in i:
                y_axis[j.get_hour()]+=1
                if(images and j.text.find("<Multimedia omitido>")!=-1):
                    y_images[j.get_hour()]+=1

        plt.bar(x_axis,y_axis)
        if images:
            plt.bar(x_axis,y_images)
        average_hour=sum(y_axis)/24
        plt.xlabel("Hours")
        plt.ylabel("Number of Messages/hour")
        if average:
            plt.axhline(y=average_hour, linewidth=1, color='k')
        if images:
            plt.legend(["Average", "NºMessages","NºImages/Vids/Stickers/..."],prop={'size': 6})
        plt.title(f' {self.name} - hour_analysis')
        #plt.show()

    def weekday_analysis(self,images=True,average=True):
        #fig=plt.figure()
        weekday=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        weekday_numb=[0 for i in range(0,len(weekday))]
        y_images=[0 for i in range(0,len(weekday))]
        for i in self.messages:
            for j in i:
                index=j.week_day_int()
                weekday_numb[index]+=1

                if (images and j.text.find("<Multimedia omitido>") != -1):
                    y_images[index] += 1

        average_weekday=sum(weekday_numb)/7
        plt.bar(weekday,weekday_numb)
        if(images):
            plt.bar(weekday,y_images)
        plt.xlabel("WeekDays")
        if average:
            plt.axhline(y=average_weekday, linewidth=1, color='k')
        plt.ylabel("Number of Messages/WeekDay")
        plt.title(f' {self.name} - weekday_analysis')
        if(images):
            plt.legend(["Average","NºMessages","NºImages/Vids/Stickers/..."],prop={'size': 6})

        #plt.show()

    def length_messages_log(self):
        sum = 0
        messages = 0
        dict = OrderedDict({0: 0})
        for i in self.messages:
            for j in i:
                val = len(j)
                if (val in dict):
                    dict[val] += 1
                else:
                    dict[val] = 1

                sum += val
                messages += 1

        x_axis=[]
        y_axis=[]
        for keys in dict:
            x_axis.append(keys)
            y_axis.append(dict[keys])

        average = sum / messages

        plt.axvline(x=average, linewidth=1, color='k')
        plt.bar(y_axis,x_axis)
        plt.title(f' {self.name} - length_analysis')
        plt.xlabel("Length of message")
        plt.ylabel("Number of messsages")
        plt.legend(["Average", "NºMessages"], prop={'size': 6})


    def analysis_log(self,withGap,images=True,average=True):
        plt.figure(f"Analysis of {self.name}  with total Messages: {self.total_messages()}")
        plt.subplot(2, 1, 1)
        self.daily_quantity_analysis(withGap)
        plt.subplot(2, 2, 3)
        self.weekday_analysis(images,average)
        plt.subplot(2, 2, 4)
        self.hour_analysis(images,average)
        plt.subplots_adjust(left=0.05,bottom=0.05,right=0.99,top=0.95,wspace=0.2,hspace=0.26)

        plt.figure(f"Analysis of {self.name}  with total Messages: {self.total_messages()} part 2")
        self.length_messages_log()
        plt.draw()


    def count_images_aDay(self,day):
        res=0
        for i in day:
            if(i.text.find("<Multimedia omitido>")!=-1):
                res+=1
        return res

    def __str__(self):
        if (self.name == None):
            return "None"
        return self.name
    def __repr__(self):
        if(self.name==None):
            return "None"
        return self.name




class message:
    def __init__(self,date,time,message):
        self.date=date
        self.time=time
        self.text=message

    def count_symbol(self,s):
        return int(self.text.count(s))

    def __len__(self):
        return int(len(self.text))



    def week_day_string(self):
        aux=self.date.split("/")
        weekday=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        if(2000+int(aux[2])<=1970 or not(1<=int(aux[1])<=12) or not(1<=int(aux[0])<=31) ):
            raise ValueError
        return str(weekday[calendar.weekday(2000+int(aux[2]),int(aux[1]),int(aux[0]))])
    def week_day_int(self):
        aux=self.date.split("/")
        if(2000+int(aux[2])<=1970 or not(1<=int(aux[1])<=12) or not(1<=int(aux[0])<=31) ):
            raise ValueError
        return calendar.weekday(2000+int(aux[2]),int(aux[1]),int(aux[0]))
    def get_hour(self):
        return int(self.time.split(":")[0])
    def get_date(self):
        aux = self.date.split("/")
        return 2000+int(aux[2]),int(aux[1]),int(aux[0])

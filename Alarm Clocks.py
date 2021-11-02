from playsound import playsound
import datetime

alarmH = int(input("Enter the Hour: "))
alarmM = int(input("Enter the Minute: "))
am_pm = input("AM or PM: ")

if am_pm == 'PM':
    alarmH += 12

while True:
    if alarmH == datetime.datetime.now().hour and alarmM == datetime.datetime.now().minute:
        print("Wake up hoe")
        playsound('helpherself.mp3')
        break



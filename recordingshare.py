import os
import datetime

sourcepath = os.path.join('C:\\', 'Users', os.getlogin().lower(), 'Videos', 'Lync Recordings')
destpath = '\\\\dewdfg213.wdf.global.corp.sap\\technology\\40_Public\\Projects\\CloudEngineering\\30_CE_Team_Infos\\2_Knowledge\\Recordings\\2019'
tempdest = os.path.join('C:\\', 'Users', os.getlogin().lower(), 'Downloads', 'PythonLearning')

foldercheck = os.path.isdir(sourcepath)
print(foldercheck)

if foldercheck is True:
    os.chdir(sourcepath)
    print(os.getcwd())
else:
    print('Check source folder path again.')

today = datetime.date.today()

# print(help(datetime))
print(today)
print(os.listdir(sourcepath))

Day = datetime.datetime.today().strftime("%d")
Month = datetime.datetime.today().strftime("%b")
Year = datetime.datetime.today().strftime("%Y")
# Day = str(3)

if Day == '1' or Day == '21' or Day == '31':
    print('CE handover BLR-SOF' + Day + 'st' + Month + Year)
elif Day == '2' or Day == '22':
    print('CE handover BLR-SOF' + Day + 'nd' + Month + Year)
elif Day == '3' or Day == '23':
    print('CE handover BLR-SOF' + Day + 'rd' + Month + Year)
else:
    print('CE handover BLR-SOF' + Day + 'th' + Month + Year)

print(datetime.datetime.today().day)
print(datetime.datetime.today().month)
print(datetime.datetime.today().year)


# for file in os.listdir('Lync Recordings\\'):
#    filetime = dt.datetime.fromtimestamp(
#        os.path.getctime('Lync Recordings\\' + file))
#    print(filetime)
#    if filetime.date() == today:
#        print('true')

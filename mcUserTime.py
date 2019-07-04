import os
import gzip

def convertTime(string):
    hour, minute, second = [int(x) for x in string.split(':')]
    seconds = second + (minute * 60) + (hour * 3600)
    return seconds

def userList():
    users = []
    userCache = open('.\\usercache.json')
    elements = userCache.readlines()[0].replace('{', '').replace('}', '').replace('[', '').split(',')
    for element in elements:
        if '"name":' in element:
            user = element[8:-1]
            users.append(user)
    return users

directory = '.\\logs'
done = False
while not done:
    print('Users:', userList())
    username = input('Enter username: ')
    totalTime = 0

    for fileName in os.listdir(directory):
        filePath = directory + '\\' + fileName
        print('Now analyzing:', filePath)
        # if it is a gz file:
        if fileName[-3:] == '.gz':
            file = gzip.open(filePath, 'rt')
            content = file.read()
            lines = content.split('\n')
        # if it is uncompressed:
        else:
            file = open(filePath, 'r')
            lines = file.readlines()
        for line in lines:
            if (': ' + username + '[' in line) and ('logged in with entity id' in line):
                login = convertTime(line[1:9])
                print('   Logged in at', line[1:9])
            elif ' ' + username + ' left the game' in line:
                logout = convertTime(line[1:9])
                if login > logout:
                    logout += 86400  # if user logged out the next day, add 24h to logout
                print('   Logged out at', line[1:9])
                totalTime += logout - login
                print('   Session time:', logout - login, 'seconds')

    if totalTime == 0:
        print(username, 'has never played on the server')
    else:
        print('TOTAL PLAY TIME:')
        print(round(totalTime / 3600, 2), 'hours')
    if input('Run again? [Y/N] ')[0].lower() == 'n':
        done = True
import sys
import requests
from dateutil import tz
from datetime import datetime
import jwt
import random
import string

class basic:
    def writeLog(filename, msg):
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('CST')
        utc = datetime.utcnow()
        utc = utc.replace(tzinfo=from_zone)
        localTime = utc.astimezone(to_zone)
        
        ip = sys.argv[1]
        port = sys.argv[2]
        
        toWrite = '[ ' + datetime.strftime(localTime, "%Y-%m-%d %H:%M:%S") + ' ] [ ' + ip + ':' + port + ' ] ' + msg + '\n'
        try:
            f = open(filename, 'a')
            f.write(toWrite)
        except:
            print('Cannot open file : ' + filename)
        
    # def connect(page_route, logPath):
    #     # ip = sys.argv[1]
    #     # port = sys.argv[2]
    #     ip = 'localhost'
    #     port = '9999'
        
    #     url = 'http://' + ip +':'+ port + page_route
    #     try:
    #         r = requests.get(url)
    #         r.close()
    #         if(r.status_code == 404):
    #             basic.writeLog(logPath, 'Can\'t access ' + url)
    #         else:
    #             basic.writeLog(logPath, url + ' is alive')
    #         exit(1)
    #     except:
    #         basic.writeLog(logPath, 'Could not connect to '+url)
    #         basic.writeLog(logPath, 'Web server closed')
    #         exit(0)
        
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjk5OSwidXNlciI6InVzZXIxIiwicGFzc3dvcmQiOiJ1c2VyMXBhc3N3b3JkIiwiZW1haWwiOiJ1c2VyMUBleGFtcGxlLmNvbSIsImNyZWRpdCI6OTk5OTk5LCJwcml2aWxlZ2UiOjF9.P0l99ua5G2EtIdFgIEGPOQHHh41aSHIz7YOTUT3Rphk
class MyJWT:
    def __generateToken():
        token = jwt.encode({"uid": 999,"user": "user1","password": "user1password","email": "user1@example.com","credit": 999999,"privilege": 1}, 'secret_key')
        return token
    
    def __randomTestingString(size=10, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    
    def checkJWTissue(self, target_route):
        ip = sys.argv[1]
        port = sys.argv[2]
        
        url = 'http://' + ip + ':' + port + target_route
        
        hackerToken = self.__generateToken().decode('utf-8')
        
        cookie = {'token': hackerToken}

        try:
            req = requests.get(url,cookies = cookie)
            
            # cannot use hacked token => jwt is fixed
            if req.status_code == 404:
                basic.writeLog('patch.log', 'jwt fixed !')
                return 1
            else:
                basic.writeLog('patch.log', 'jwt not fixed ...')
                return 0

        except:
            basic.writeLog('patch.log',  'can\'t check whether jwt is fixed or not ...')
            basic.writeLog('patch.log',  'maybe web server is closed')
            return 0
    
          
        # try:
        #     req = requests.get(url, cookies = {'token': self.__generateToken()})
        #     # check jwt
        #     if req.status_code == 404:
        #         basic.writeLog('./patch.log', 'Cannot request ' + url + ' with hacker\'s token !')
        #         patchedOrNot = 1
        #     else:
        #         basic.writeLog('./patch.log', 'Still can request ' + url + ' with hacker\'s token')
        #         basic.writeLog('./patch.log', 'JWT still work with ' + url)
        #         # if hacker's token still works with
        #         # check command injection
        #         if target_route == '/admin/ctrl':
        #             try:
        #                 randomTestingString = self.__randomTestingString()
        #                 cmd = 'test | echo ' + randomTestingString
        #                 payload = {'domain': cmd}
        #                 cmdReq = requests.post(url, data = payload, cookies = {'token': self.__generateToken()})
        #                 if randomTestingString in cmdReq.text:
        #                     basic.writeLog('./patch.log', 'Oops, Command injection still there')
        #                 else:
        #                     basic.writeLog('./patch.log', 'Command injection fixed')
        #                     # patchedOrNot = 0
        #                 cmdReq.close()
        #             except:
        #                 basic.writeLog('./patch.log', 'Cannot post ' + url + ' to check command injection')
        #     req.close()
        # except:
        #     basic.writeLog('./patch.log', 'Cannot check jwt issue for ' + url + ' cause web server closed')
        # exit(patchedOrNot)
    
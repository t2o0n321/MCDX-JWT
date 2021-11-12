import os
import sys
import time
sys.path.append(os.path.dirname(__file__) + '/utils')
from utils.tools import basic
from utils.tools import MyJWT as jwt

if __name__ == '__main__':
    
    WebServiceRoutes = [
        '/',
        '/shop',
        '/users',
        '/api/auth/login',
        '/api/auth/logout'
    ]
    
    jwtBugRoute = [
        '/admin/ctrl', 
        '/users/profile'
    ]
    
    while True:
        # check if the serices are working
        for i in WebServiceRoutes:
            basic.connect(i, './patch.log')
        
        # check if the user fixed the bugs 
        for i in jwtBugRoute:
            jwt.reqWithToken(jwt, i)
        
        time.sleep(3)
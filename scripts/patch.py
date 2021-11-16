import os
import sys
import time
from tools import basic
from tools import MyJWT as jwt

if __name__ == '__main__':
    
    jwtBugRoute = [
        '/admin/ctrl',
        '/users/profile'
    ]
    
    # check if the user fixed the bugs 
    for i in jwtBugRoute:
        if(jwt.checkJWTissue(jwt, i) == 0):
            exit(0)
    exit(1)
            
        

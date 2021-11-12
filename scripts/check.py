import sys
import os
import time
sys.path.append(os.path.dirname(__file__) + '/utils')
from utils.tools import basic

if __name__ == '__main__':
    
    checkRoutes = [
        '/',
        '/shop',
        '/users',
        '/api/auth/login',
        '/api/auth/logout',
        '/admin/ctrl'
    ]
    
    while True:
        for i in checkRoutes:
            basic.connect(i, './check.log')
        time.sleep(3)
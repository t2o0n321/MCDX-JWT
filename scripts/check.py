from tools import basic
import requests
import sys

if __name__ == '__main__':
    
    checkRoutes = [
        '/',
        '/shop',
        '/users',
        '/api/auth/login',
        '/api/auth/logout',
        '/admin/ctrl'
    ]

    ip = sys.argv[1]
    port = sys.argv[2]
    
    for i in checkRoutes:
        url = 'http://' + ip +':'+ port + i
        try:
            r = requests.get(url)
            basic.writeLog('check.log', url + 'is alive')
        except:
            basic.writeLog('check.log', 'Cannot connect to ' + url + ' ...')
            exit(0)
    exit(1)
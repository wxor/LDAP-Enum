import datetime
import argparse

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    parser = argparse.ArgumentParser(description="LDAP test")
    authargs = parser.add_argument_group('Details')
    
    authargs.add_argument('-i', '--ipaddress', required=False, dest='ipaddress', help='IP address the DC')
    authargs.add_argument('-d', '--domain', required=False, dest='domain', help='Domain')
    authargs.add_argument('-u', '--user', required=False, dest='username', help='Username to test')
    authargs.add_argument('-p', '--password', required=False, dest='password', help='Password to test')
    authargs.add_argument('-ul', '--userlist', required=False, dest='userlist', help='Test user with list')
    authargs.add_argument('-pl', '--passlist', required=False, dest='passlist', help='Test password with list')

    args = parser.parse_args()

    #passList = [line.rstrip('\n') for line in open(args.passlist)]
    #for x in passList:
    test_creds("xxxx", "xxxxxx")
    test_creds(username, password) 

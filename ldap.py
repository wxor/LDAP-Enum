import ldap

def test_creds(username, password):
   LDAP_SERVER = 'ldap://xxxxxx.LOCAL'
   LDAP_USERNAME = '%s@xxxxx.LOCAL' % username
   LDAP_PASSWORD = password
   base_dn = 'DC=xxxxx-BANK,DC=LOCAL'
   ldap_filter = 'userPrincipalName=%s@xxxxxx.LOCAL' % username
   attrs = ['memberOf']
   try:
       ldap_client = ldap.initialize(LDAP_SERVER)
       ldap_client.set_option(ldap.OPT_REFERRALS,0)
       ldap_client.simple_bind_s(LDAP_USERNAME, LDAP_PASSWORD)
   except ldap.INVALID_CREDENTIALS:
       ldap_client.unbind()
       return 'INVALID CREDENTIALS'
   except ldap.SERVER_DOWN:
       return 'SERVER DOWN'
   print "Connection Successful!"
   req = str(ldap_client.search_s(base_dn, ldap.SCOPE_SUBTREE, ldap_filter, attrs)[0][1]['memberOf'])
   ldap_client.unbind()
   return req

print check_credentials(adUser, adPass)

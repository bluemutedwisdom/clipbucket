#!/usr/bin/python
"""Set ClipBucket admin password, email and domain to serve

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively
    --domain=   unless provided, will ask interactively
                DEFAULT=www.example.com
"""

import sys
import getopt
import hashlib

from dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

DEFAULT_DOMAIN="www.example.com"


def clipbucket_hash(password):

    def md5(s):
        return hashlib.md5(s).hexdigest()

    def sha1(s):
        return hashlib.sha1(s).hexdigest()

    return md5(md5(sha1(sha1(md5(password)))))

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email=', 'domain='])
    except getopt.GetoptError, e:
        usage(e)

    email = ""
    domain = ""
    password = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val
        elif opt == '--domain':
            domain = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "ClipBucket Password",
            "Enter new password for the ClipBucket 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "ClipBucket Email",
            "Enter email address for the ClipBucket 'admin' account.",
            "admin@example.com")

    if not domain:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        domain = d.get_input(
            "ClipBucket Domain",
            "Enter the domain to serve ClipBucket.",
            DEFAULT_DOMAIN)

    if domain == "DEFAULT":
        domain = DEFAULT_DOMAIN

    hash = clipbucket_hash(password)

    m = MySQL()
    m.execute('UPDATE clipbucket.users SET password=\"%s\", email=\"%s\" WHERE username=\"admin\";' % (hash, email))

    m.execute('UPDATE clipbucket.config SET value=\"%s\" WHERE name=\"support_email\";' % email)
    m.execute('UPDATE clipbucket.config SET value=\"%s\" WHERE name=\"website_email\";' % email)
    m.execute('UPDATE clipbucket.config SET value=\"%s\" WHERE name=\"welcome_email\";' % email)

    m.execute('UPDATE clipbucket.config SET value=\"http://%s\" WHERE name=\"baseurl\";' % domain)
    

if __name__ == "__main__":
    main()


import socket
import smtplib
import dns.resolver

def check_mail(mail):
    domain = mail.split("@")[1]
    print(domain)
    records = dns.resolver.query(domain, 'MX')
    print(records)
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)
    # Get local server hostname
    host = socket.gethostname()

    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    server.connect(mxRecord)
    server.helo(host)
    server.mail('amalandomnic@gmail.com')
    code, message = server.rcpt(str(mail))
    server.quit()
    if code == 250:
        return True
    else:
        return False
print(check_mail("amalandomnic@gmail.com"))

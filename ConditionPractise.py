email = "dear customer, your account will expire soon. click the link below to verify your account. regards, support@securebank.com"
if(email.endswith(".com")):
    print("Valid address")
    if(email.find("click")!=-1):
        print("There is a link")
        if(email.count("account")>=2):
            print("Urgent activity")
        else:
            print("Normal activity")
    else:
        print("Link not found")

if(len(email)<=100):
    print("Short mail")
else:
    print("Long mail")
import time
from datetime import datetime as dt

# Creating a custom variable of datetime - 'dt'
host_test = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = '127.0.0.1'
website_list = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com"]

while True:
    if dt (dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        with open(host_path, 'r+') as file:
            content = file.read()
            # print(content)
            # Check to see if the  sites to be blocked are in the host file
            # First we iterate throught the list of websites
            for website in website_list:
                # Check to see if each website is in the content of the host file.
                if website in content:
                    pass
                else:
                    # If site is not in the content of the host file we write the website to the host file
                    file.write(redirect + " " + website + " \n")
        print('Cannot access webiste during working hours')
        
       
    else:
        # 
        with open(host_path, 'r+') as file:
            # read the content of the file line by line and store each line in a list - 'content'
            content = file.readlines() 
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print('Site Blocker relaxed, Enjoy browsing')
    time.sleep(5)


    
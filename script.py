# This script was made by Colton McAda and Chris Garcia

import os.path

# This is function pulls the logs from the website and saves into a file if the log file is not currently in the directory
def savelogs():
    if not os.path.exists('./logs.txt'):
        import urllib.request
        urllib.request.urlretrieve('https://s3.amazonaws.com/tcmg476/http_access_log','logs.txt')

savelogs()

# This function will take that log file and delete any bad lines
def clean_logs():
    if not os.path.exists('./cleanlogs.txt'):
        with open("cleanlogs.txt", "w") as out:
            with open("logs.txt") as f:
                for line in f:
                    if len(line) > 38:
                        out.write(line)

clean_logs()

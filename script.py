# This script was made by Colton McAda and Chris Garcia (with maybe some help from the internet).

import os.path

# This is function pulls the logs from the website and saves into a file if the log file is not currently in the directory.
def savelogs():
    if not os.path.exists('./logs.txt'):
        import urllib.request
        urllib.request.urlretrieve('https://s3.amazonaws.com/tcmg476/http_access_log','logs.txt')

savelogs()

# This function will take that log file and delete any bad lines.
def clean_logs():
    if not os.path.exists('./cleanlogs.txt'):
        with open("cleanlogs.txt", "w") as out:
            with open("logs.txt") as f:
                for line in f:
                    if len(line) > 38:
                        out.write(line)

clean_logs()

# This function will return the answer to how many requests were made in the log. Note that any corrupt requests were thrown out.
def total_requests():
    num_lines = 0
    with open('cleanlogs.txt','r') as f:
        for i in f:
            num_lines += 1
    print('This is the total amount of requests in the log file: ',num_lines)

total_requests()

# This code will go through the lines of logs, assign the file to a value in a list, then count how many times that value appears over 
# multiple lines. Afterwards, it will return the least and most appeared file in the logs. 
def file_count():
    import re
    file_dict = {}
    for line in open('cleanlogs.txt'):
        pieces = re.split('.*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*', line)
        try:
            file = pieces[4]
        except IndexError:
            continue
        if file in file_dict:
            file_dict[file] += 1
        else:
            file_dict[file] = 1

    maximum = max(file_dict, key=file_dict.get)
    minimum = min(file_dict, key=file_dict.get)
    print('The most requested file is ', maximum,' with ', file_dict[maximum],' requests.')
    print('The least requested file is ', minimum,' with ', file_dict[minimum],' requests.')

file_count()

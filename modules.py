import time
import os
import pandas

while True:
    if os.path.exists('files/temps_today.csv'):
        data = pandas.read_csv('files/temp_today.csv')
        # print(data.mean()[st1]) for only station 1
        print(data.mean())
    else:
        print('file does not exist')
        time.sleep(10)
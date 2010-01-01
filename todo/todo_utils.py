import datetime
import subprocess
import os
import todo_config

def open_day(num_days=0):
    day = datetime.date.today() + datetime.timedelta(num_days)
    day = day.strftime("%Y-%m-%d")
    subprocess.call("%s %s" % (todo_config.EDITOR, day), shell=True)

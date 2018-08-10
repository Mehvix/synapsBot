#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from datetime import datetime, timedelta

start_time = time.time()


def uptime():
    sec = time.time() - start_time
    sec = str(sec).split(".")
    sec = timedelta(seconds=int(sec[0]))
    d = datetime(1, 1, 1) + sec

    return "{}:{}:{}:{} (DAYS:HOURS:MIN:SEC)".format(d.day - 1, d.hour, d.minute, d.second)


def get_time():
    # Decides if startup is during AM or PM ours (yea damn 'murica time)
    if datetime.now().hour > 13:
        cur_hour = datetime.now().hour - 12
        am_or_pm = "PM"
    else:
        cur_hour = datetime.now().hour
        am_or_pm = "AM"

    # Puts "0" in front of number time
    if datetime.now().minute < 10:
        cur_min = "0{}".format(datetime.now().minute)
    else:
        cur_min = datetime.now().minute

    if datetime.now().second < 10:
        cur_sec = "0{}".format(datetime.now().second)
    else:
        cur_sec = datetime.now().second

    return "{0}:{1}:{2} {3}".format(cur_hour, cur_min, cur_sec, am_or_pm)

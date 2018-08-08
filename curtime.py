#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime


def get_time():
    # Decides if startup is during AM or PM ours (yea damn 'murica time)
    if datetime.datetime.now().hour > 13:
        cur_hour = datetime.datetime.now().hour - 12
        am_or_pm = "PM"
    else:
        cur_hour = datetime.datetime.now().hour
        am_or_pm = "AM"

    # Puts "0" in front of number time
    if datetime.datetime.now().minute < 10:
        cur_min = "0{}".format(datetime.datetime.now().minute)
    else:
        cur_min = datetime.datetime.now().minute

    if datetime.datetime.now().second < 10:
        cur_sec = "0{}".format(datetime.datetime.now().second)
    else:
        cur_sec = datetime.datetime.now().second

    return "{0}:{1}:{2} {3}".format(cur_hour, cur_min, cur_sec, am_or_pm)

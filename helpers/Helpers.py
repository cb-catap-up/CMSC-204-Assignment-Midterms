import time

def clear_console():
    print('\033c', end='')

def add_break_point(time_for_sleep=7, sleep_only = False):
    if not sleep_only:
        clear_console()
    time.sleep(time_for_sleep)
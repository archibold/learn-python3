import time

def notification(title, message):
    import os
    cmd = 'ntfy -t "{0}" send "{1}"'.format(title, message)
    os.system(cmd)

while(1):
    notification("Break time", "Do some eyes exec and move your back")
    time.sleep(1800)

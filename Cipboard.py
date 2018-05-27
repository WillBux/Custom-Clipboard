__Author__ = "Will Buxton"

import subprocess
from pynput import keyboard
from pynput.keyboard import Key
import os
copy = """osascript -e 'tell application "System Events" to keystroke "c" using {command down}'"""
paste = """osascript -e 'tell application "System Events" to keystroke "v" using {command down}'"""


buckets = {1: "", 2: "", 3: "", 4: "", 5: "", 6: ""}


def f1():
    os.system(copy)
    buckets[1] = getClipboardData()


def f2():
    setClipboardData(buckets[1])
    os.system(paste)


def f3():
    os.system(copy)
    buckets[2] = getClipboardData()


def f4():
    setClipboardData(buckets[2])
    os.system(paste)


def f5():
    os.system(copy)
    buckets[3] = getClipboardData()


def f6():
    setClipboardData(buckets[3])
    os.system(paste)


def f7():
    os.system(copy)
    buckets[4] = getClipboardData()


def f8():
    setClipboardData(buckets[4])
    os.system(paste)


def f9():
    os.system(copy)
    buckets[5] = getClipboardData()


def f10():
    setClipboardData(buckets[5])
    os.system(paste)


def f11():
    os.system(copy)
    buckets[6] = getClipboardData()


def f12():
    setClipboardData(buckets[6])
    os.system(paste)


def on_press(key):
    if key == Key.f1:
        f1()
    elif key == Key.f2:
        f2()
    elif key == Key.f3:
        f3()
    elif key == Key.f4:
        f4()
    elif key == Key.f5:
        f5()
    elif key == Key.f6:
        f6()
    elif key == Key.f7:
        f7()
    elif key == Key.f8:
        f8()
    elif key == Key.f9:
        f9()
    elif key == Key.f10:
        f10()
    elif key == Key.f11:
        f11()
    elif key == Key.f12:
        f12()


def on_release(key):
    return key


def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

def setClipboardData(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()





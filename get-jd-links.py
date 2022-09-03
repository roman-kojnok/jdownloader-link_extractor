#!/usr/bin/env python3
import platform
import os
import glob
import shutil

iam = os.getlogin()
win = "C:/Users/" + iam + "/AppData/Local/JDownloader 2.0/cfg"
mac = "/Users/" + iam + "/bin/JDownloader 2.0/cfg"
nix = "/home/" + iam + "/jd2/cfg"
print(iam)

comp = platform.system()

jdown = ""
if comp == "Windows":
    jdown = win
    print("\n" + comp + " OS Detected.\n")
elif comp == "Darwin":
    jdown = mac
    print("\n" + comp + " OS Detected.\n")
elif comp == "Linux":
    jdown = nix
    print("\n" + comp + " OS Detected.\n")
else:
    print("\n" + "Unsupported OS!\n")

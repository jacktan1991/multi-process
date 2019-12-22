#! /usr/bin/env python
# coding:utf8

import os

def main():
    # all codes before fork will be calles only once
    print("main start...")

    pid = os.fork()
    print("this point for child process is 'resume'-ing running, while for parent procss is 'continue'-ing running")
    if pid == 0:
        # Codes running in the child process eventually.
        print("%d (child) just was created by %d." % (os.getpid(), os.getppid()))
    else:
        # Codes running in the parent process eventually.
        print("%d (parent) just created %d." % (os.getpid(), pid))

    print("main end...")

if __name__ == "__main__":
    main()

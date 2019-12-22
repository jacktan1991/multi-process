#! /usr/bin/env python
# coding:utf8

import os
import logging
logging.basicConfig(level=logging.DEBUG, datefmt="%Y-%m-%d %H:%M:%S", format="[%(asctime)s.%(msecs)03d]pid-%(process)d;(%(filename)s#L%(lineno)d)-%(levelname)s %(message)s")

def main():
    logging.debug("main start...")

    pid = os.fork()
    logging.debug("this point for child process is 'resume'-ing running, while for parent procss is 'continue'-ing running")
    if pid == 0:
        # Codes running in the child process eventually.
        logging.debug("%d (child) just was created by %d." % (os.getpid(), os.getppid()))
    else:
        # Codes running in the parent process eventually.
        logging.debug("%d (parent) just created %d." % (os.getpid(), pid))

    logging.debug("main end...")

if __name__ == "__main__":
    main()

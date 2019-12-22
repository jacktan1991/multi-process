#! /usr/bin/env python
# coding:utf8

import os
import urllib
import logging
logging.basicConfig(level=logging.DEBUG, datefmt="%Y-%m-%d %H:%M:%S", format="[%(asctime)s.%(msecs)03d]pid-%(process)d;(%(filename)s#L%(lineno)d)-%(levelname)s %(message)s")

def main():
    # all codes before fork will be calles only once
    logging.debug("main start...")

    foo = {"v": "foo"}
    BAR = {"v": "BAR"}

    (lambda *args, **kwargs: foo.update(v=kwargs['v']) or logging.info("foo.v updated to %s by pid-%d", kwargs['v'], os.getpid()))(v="Foo")

    logging.info("Befor fork: foo=%s, BAR=%s", str(foo), str(BAR))

    # fork之后，父进程继续；子进程不会再重新运行fork前的语句，而是直接“继承”了数据的瞬时状态
    pid = os.fork()
    logging.info("this point for child process is 'resume'-ing running" if pid == 0 else "this point for parent procss is 'continue'-ing running")  # if 和 else 代码在父、子进程都有可见性
    logging.info("After fork: foo=%s, BAR=%s", str(foo), str(BAR))
    if pid == 0:
        # Codes running in the child process eventually.
        logging.debug("%d (child) just was created by %d." % (os.getpid(), os.getppid()))
        urllib.urlopen("http://httpbin.org/delay/5")
    else:
        # Codes running in the parent process eventually.
        logging.debug("%d (parent) just created %d." % (os.getpid(), pid))
        urllib.urlopen("http://httpbin.org/delay/5")

    logging.debug("main end...")

if __name__ == "__main__":
    main()

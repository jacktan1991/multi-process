#! /usr/bin/env php
<?php

function main() {
    print("main start...\n");

    $pid = pcntl_fork();
    print("this point for child process is 'resume'-ing running, while for parent procss is 'continue'-ing running\n");
    if ($pid === 0) {
        // Codes running in the child process eventually.
        printf("%d (child) just was created by %d.\n", getmypid(), posix_getppid());
    } else {
        // Codes running in the parent process eventually.
        printf("%d (parent) just created %d.\n", getmypid(), $pid);
    }

    print("main end...\n");
}

main();

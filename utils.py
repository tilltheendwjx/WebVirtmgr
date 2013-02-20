import time
def retry(func, expectedException=Exception, tries=None,
          timeout=None, sleep=1, stopCallback=None):
    """
    Retry a function. Wraps the retry logic so you don't have to
    implement it each time you need it.

    :param func: The callable to run.
    :param expectedException: The exception you expect to receive when the
                              function fails.
    :param tries: The number of time to try. None\0,-1 means infinite.
    :param timeout: The time you want to spend waiting. This **WILL NOT** stop
                    the method. It will just not run it if it ended after the
                    timeout.
    :param sleep: Time to sleep between calls in seconds.
    :param stopCallback: A function that takes no parameters and causes the
                         method to stop retrying when it returns with a
                         positive value.
    """
    if tries in [0, None]:
        tries = -1

    if timeout in [0, None]:
        timeout = -1

    startTime = time.time()

    while True:
        tries -= 1
        try:
            return func()
        except expectedException:
            if tries == 0:
                raise

            if (timeout > 0) and ((time.time() - startTime) > timeout):
                raise

            if stopCallback is not None and stopCallback():
                raise

            time.sleep(sleep)
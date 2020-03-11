from contextlib import contextmanager
from datetime import datetime
from time import sleep
from logging import getLogger, DEBUG, INFO

hugtools_logger = getLogger(__name__)

class HugTimer(object):
    def __init__(self, label=None, timestamps=False, log_level=0):
        """
        HugTimer: A context manager timer
        
        Parameters
        ----------
        label : str, optional
            Display name of timer, by default "Timer"
        timestamps : bool, optional
            whether or not to log timestamps for start and stop, by default False
        """
        super().__init__()

        self.logger = getLogger(__name__)
        self.logger.setLevel(log_level)
        self.timestamps = timestamps
        self.label = label or "Timer"
        

    def __enter__(self):
        self.start = datetime.now()
        if self.timestamps:
            self.logger.debug(f"{label} started at {self.start}")

        return self.start

    def __exit__(self, exception_type, exception_value, traceback):
        self.stop = datetime.now()
        if self.timestamps:
            self.logger.debug(f"{label} stopped at {self.stop}")
        
        self.delta = self.stop - self.start
        print(f"{self.label} took {self.delta}")


def time_function(fn):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        hugtools_logger.debug(f"Start {fn.__name__} at: {start}")
        return_var = fn(*args, **kwargs)
        stop = datetime.now()
        hugtools_logger.debug(f"Stop {fn.__name__} at: {stop}")
        print(f"Duration: {stop - start}")
        return return_var
    return wrapper

def tests(*args, **kwargs):
    hugtools_logger.setLevel(INFO)

    with HugTimer("Test", log_level=INFO) as timer:
        sleep(2)

if __name__ == "__main__":
    tests()
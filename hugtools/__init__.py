from threading import Thread
from contextlib import contextmanager
from datetime import datetime
from time import sleep
from logging import getLogger, DEBUG, INFO
import json

hugtools_logger = getLogger(__name__)

# Classes


class Dummy(object):
    pass

    @classmethod
    def from_json(cls, json_input):
        c = cls()
        if not isinstance(json_input, dict):
            json_input = json.loads(json_input)

        for attr_name, attr in json_input.items():
            try:
                int(attr_name)
                attr_name = "_" + attr_name
                setattr(c, attr_name, attr)
            except ValueError:
                setattr(c, attr_name, attr)
        return c


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

    def checkpoint(self):
        check = datetime.now()
        delta = check - self.start
        print(f"{self.label} at {self.delta}")

# Functions


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


# check for freeze:


def status_check(fn, args=[], kwargs={}, interval=2):
    """
    WIP
    """

    def still_running(name, args, kwargs):
        print("Still running",
              f"{name}({(', '.join([repr(arg) for arg in args]) + ', ' + ', '.join([str(key) + '=' + repr(value) for key, value in kwargs.items()])).strip(', ')})")

    process = Thread(target=still_running, name="status_check",
                     args=[fn.__name__, args, kwargs])
    process.start()
    result = fn(*args, **kwargs)
    process.join()
    return result

# tests


def tests(*args, **kwargs):
    hugtools_logger.setLevel(INFO)

    # print("test HugTimer")
    # with HugTimer("Test", log_level=INFO) as timer:
    #     sleep(2)

    # print("test time_function")
    # time_function(sleep)(2)

    print("test status_check")
    status_check(sleep, args=[10], interval=2)


if __name__ == "__main__":
    tests()

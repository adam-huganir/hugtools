from datetime import datetime
from typing import Callable, Optional

from ._logging import logger


class HugTimer:
    def __init__(self, label: Optional[str] = None, timestamps: bool = False):
        """
        HugTimer: A context manager timer

        Parameters
        ----------
        label : str, optional
            Display name of timer, by default "Timer"
        timestamps : bool, optional
            whether or not to log timestamps for start and stop, by default False
        """
        self.timestamps = timestamps
        self.label = label or "Timer"

    def __enter__(self):
        self.start = datetime.now()
        if self.timestamps:
            logger.debug(f"{self.label} started at {self.start}")

        return self.start

    def __exit__(self, exception_type, exception_value, traceback):
        self.stop = datetime.now()
        if self.timestamps:
            logger.debug(f"{self.label} stopped at {self.stop}")

        self.delta = self.stop - self.start
        print(f"{self.label} took {self.delta}")

    def checkpoint(self):
        check = datetime.now()
        delta = check - self.start
        print(f"{self.label} at {delta}")


def time_function(fn: Callable) -> Callable:
    """
    A simple wrapper function that will log start time, stop time, and duration for anything you run to _loglevel

    Args:
        fn (Callable): the callable you wish to time

    Returns:
        Callable: the wrapped callable
    """

    def wrapper(*args, _loglevel="debug", **kwargs):
        start = datetime.now()
        getattr(logger, _loglevel)(f"Start {fn.__name__} at: {start}")
        return_var = fn(*args, **kwargs)
        stop = datetime.now()
        getattr(logger, _loglevel)(f"Stop {fn.__name__} at: {stop}")
        getattr(logger, _loglevel)(f"Duration: {stop - start}")
        return return_var

    return wrapper

from typing import Callable


class Job:

    job_id: int
    job_function: Callable
    args: tuple

    def __init__(self, func, args):
        self.job_function = func
        self.args = args

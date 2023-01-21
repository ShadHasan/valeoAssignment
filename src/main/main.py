from lib.Schedular import Schedular
from models.Job import Job
from sample.Dummy import fib, even


jobs = {"1": Job(fib, 100), "2": Job(even, 100)}

if __name__ == "__main__":
    schedular = Schedular()
    schedular.start()
    job = "no"
    while True:
        if job == "shut":
            schedular.shutdown()
            break

        print("Jobs: {}".format(jobs))
        job = input("Pick the job, or shut to stop")
        if jobs.get(job):
            schedular.load_job(jobs.get(job))
        if job != "shut":
            job = "no"

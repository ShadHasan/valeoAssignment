import threading
from time import sleep
from models.Job import Job


class Schedular(threading.Thread):

    pool_size = 100
    pools = {}
    job_loader = {}
    max_time = 10  # In minutes
    interval = 0.25   # In minutes
    __shutdown = False
    __job_id = 1

    def __int__(self, pool_size=100, max_time=10, interval=0.25):
        self.pool_size = pool_size
        self.max_time = 10
        self.interval = interval

    def get_job(self, job_id):
        return self.pools[job_id]

    def load_job(self, job: Job):
        job.job_id = self.__job_id
        self.job_loader[self.__job_id] = job
        self.__job_id = self.__job_id + 1

    def shutdown(self):
        self.__shutdown = True
        print("Please wait 15 second to shutdown")

    def run(self):
        while not self.__shutdown:
            self.schedular()

    def schedular(self):
        print("Running schedular")
        clean_load = []
        deletable_job = []
        runnable_job = {}
        for job_id in self.job_loader.keys():
            runnable_job[self.job_loader[job_id].job_function] = self.job_loader[job_id].args
            clean_load.append(job_id)
        for job in clean_load:
            del self.job_loader[job]
        for k, v in runnable_job.items():
            thread = threading.Thread(target=k, args=(v,))
            thread.start()
        for job_id in self.pools.keys():
            if not self.pools[job_id].is_alive():
                deletable_job.append(job_id)
            else:
                print("Current alive job {}".format(job_id))
        for job in deletable_job:
            del self.pools[job]
        interval = self.interval * 60
        print("Next scheduling after {} s".format(interval))
        sleep(interval)



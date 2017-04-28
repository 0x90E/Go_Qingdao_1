import threadpool


class AsyncTask:

    pool = None
    callback = None

    def __init__(self, max_tasks, callback):
        self.pool = threadpool.ThreadPool(max_tasks)
        self.callback = callback
        pass

    def append_task(self, task_info):
        requests = threadpool.makeRequests(self.callback, task_info)
        [self.pool.putRequest(req) for req in requests]

    def wait(self):
        self.pool.wait()


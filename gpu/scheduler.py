import threading
from queue import Queue


class GPUScheduler:

    def __init__(self, workers=4):

        self.queue = Queue()
        self.workers = workers

    def submit(self, fn, *args):

        self.queue.put((fn, args))

    def run_worker(self):

        while True:

            fn, args = self.queue.get()
            fn(*args)
            self.queue.task_done()

    def start(self):

        for _ in range(self.workers):

            t = threading.Thread(target=self.run_worker, daemon=True)
            t.start()

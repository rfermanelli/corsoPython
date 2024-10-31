class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []
    def put(self,elem):
        self.queue.insert(0,elem)
    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            QueueError

obj_queue = Queue()
obj_queue.put(0)
obj_queue.put(1)

for i in range(100):
    obj_queue.get()


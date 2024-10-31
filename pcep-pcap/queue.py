class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.__queue_list = []

    def put(self, element):
        self.__queue_list.insert(0, element)

    def get(self):
        try:
            return self.__queue_list.pop()
        except QueueError:
            return 'Queue empty'
#

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
#try:
for i in range(4):
    print(que.get())
#except:
#    print("Queue error")

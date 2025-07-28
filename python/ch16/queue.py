class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def status_queue(self):
        return self.queue


q1 = Queue()
q1.dequeue()
q1.enqueue(1)
q1.enqueue(2)
q1.dequeue()
print(q1.status_queue())
q1.enqueue(3)
q1.enqueue(4)
q1.dequeue()
print(q1.status_queue())

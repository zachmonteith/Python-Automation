import random

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        """this will be O(n) time where n is the number of items currently in the queue.  must shift all indices when popping from front.  I chose this approach, rather than enqueueing at front, because I like the way it looks better: elements move to the front of the queue, and enqueue at the back of the queue, just like humans lining up for something.  either way, one of these methods will be constant time and the other linear."""
        if self.items:
            return self.items.pop(0)
        return None

    def peek(self):
        """constant runtime, as we are only accessing a value by index, not reindexing any values"""
        if self.items:
            return self.items[0]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    #create 3 classes that, together, model how a printer could take print jobs out of a print queue.
    #requirements: 1) class called PrintQueue that follows normal queue DS impl.
    #              2) class called Job: pages attribute (1-10 pages, could do random)
        #                               print_page() - decrement pages
        #                               check_complete() - check if all pages printed
        #            3) class called Printer: get_job() should dequeue PrintQueue.
        #                                    print_job() should uhhh print. the job.

class PrintQueue(Queue):
    pass

class Job:

    def __init__(self, pages=random.randint(1,10)):
        self.pages = pages

    def check_complete(self):
        return self.pages == 0

    def print_page(self):
        if self.check_complete():
            print("job complete")
        else:
            print("printing page {}".format(self.pages))
            self.pages -= 1

class Printer:

    def __init__(self):
        self.print_queue = PrintQueue()

    def get_job(self):
        if self.print_queue.is_empty():
            return None
        return self.print_queue.dequeue()

    def print_job(self):
        job = self.get_job()
        if job != None:
            while job.check_complete() == False:
                job.print_page()
            print("job complete")
        else:
            print("no jobs in queue!")

    def create_job(self, job=Job()):
        self.print_queue.enqueue(job)
        print("job added to queue")

        

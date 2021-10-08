class Queue(object):
    def __init__(self, size):
        self.queue = 
        self.size = -1

    def enqueue(self, item):
        '''This function adds an item to the rear end of the queue '''

        if(self.isFull() == True):
            self.queue.insert(item)
        else:
            print('Queue is Full!')

    def dequeue(self):
        ''' This function removes an item from the front end of the queue '''
        if(self.isEmpty() != true):
            return queue.pop()
        else:
            print('Queue is Empty!)

    def isEmpty(self):
        ''' This function checks if the queue is empty '''
        return self.queue != []

    def isFull(self):
        ''' This function checks if the queue is full '''
        return self.queue == self.size

    def peek(self):
        ''' This function helps to see the first element at the front end of the queue '''
        if(self.isEmpty() != true):
            return self.queue[1]
        else:
            print('Queue is Empty!')
            

if __name__ == '__main__':
    myQueue = Queue(10)
    myQueue.enqueue(4)
    myQueue.enqueue(5)
    myQueue.enqueue(6)
    
    print(myQueue)
    
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    
    print(myQueue)
    
    myQueue.dequeue()
    
    print(myQueue)

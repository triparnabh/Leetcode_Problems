

class Queue:
    stack1 = []
    stack2 = []

    def enQueue(self, x):

        stack1.append(x)


    def dequeue(self):

        if len(stack2)<= 0:
            if len(stack1)<=0:
                exit()
        else:
            while len(stack1)!= 0:
                x = stack1.pop()
                stack2.append(x)

        return stack2.pop()


def main():

    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

main()
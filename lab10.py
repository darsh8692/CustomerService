from random import randint
# Amazon Customer Service
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self): # Check if the line is empty
        return self.items == []

    def enqueue(self, call):  # Add a complaint to the line
        self.items.insert(0, call)

    def dequeue(self):  # Remove a complaint from the line when done
        return self.items.pop()

    def size(self): # Check how many calls are in the line (size of the queue)
        return len(self.items)

    def display(self):  # displays queue
        print(self.items)

    def displayCall(self):
        return print(str(self.items[-1]))

    def getCall(self):
        randVal = randint(1, 1000)
        Complain = input(
            'What is the complain for your Item? \n'
            ' 1.Return\n'
            ' 2.Replace\n'
        )
        Reason = input(
            'Type the Reason out of 3 for your Return or Replace? \n'
            ' 1.Item No Longer Needed \n'
            ' 2.Damaged Item \n'
            ' 3.Item Never Received \n'
        )

        Dict = {
            "Complain_ID": randVal,
            "Complain": Complain,
            "Reason": Reason
        }
        return Dict

call = Queue()
print("Welcome to Amazon Customer Service!")

for i in range(1000):
    Choice = int(input('\n       [SERVICES]    \n'
                           '1. File a complain\n'
                           '2  Show all Complains\n'
                           '3. Print out your Complain\n'
                           '4. Exit the system\n'))
    if Choice == 1:
        x = call.getCall()
        call.enqueue(x)
    elif Choice == 2:
        if call.isEmpty():
            print("-> No Complains in the queue!")
        else:
            for item in call.items:
                print(item)
            print("Total Complains: ",call.size())
    elif Choice == 3:
        call.displayCall()
        if call.isEmpty():
            pass
            print("You must file a Complain to print!")
        else:
            call.dequeue()
            print("\n-> Your Complain was filed Successfully")
    elif Choice == 4:
        print("Sorry For the the Inconvenience, We will get to you as soon as possible!")
        exit(1)

class UserDefinedDataStructure():

    def __init__(self):
        pass

    def toString(self):
        pass


class Node(UserDefinedDataStructure):

    def __init__(self, data):
        super().__init__()

        self.data = data
        self.next = None

    def toString(self):
        return str(self.data)


class LinkedList(UserDefinedDataStructure):

    def __init__(self, data):

        super().__init__()

        self.headNode = Node(data)

    def append(self, x):

        currentNode = self.headNode

        while currentNode.next != None:
            currentNode = currentNode.next

        currentNode.next = Node(x)

    def add(self, i, x):

        if i == 0:

            oldHeadNode = self.headNode
            self.headNode = Node(x)
            self.headNode.next = oldHeadNode

        else:

            j = 0

            previousNode = None
            currentNode = self.headNode

            while j < i:
                j += 1
                previousNode = currentNode
                currentNode = currentNode.next

            oldCurrentNode = currentNode
            currentNode = Node(x)

            if previousNode != None:
                previousNode.next = currentNode

            currentNode.next = oldCurrentNode

    def removeAt(self, i):

        if i == 0:

            self.headNode = self.headNode.next

        else:

            j = 0

            previousNode = None
            currentNode = self.headNode

            while j < i:
                j += 1
                previousNode = currentNode
                currentNode = currentNode.next

            previousNode.next = currentNode.next

    def remove(self):

        previousNode = None
        currentNode = self.headNode

        while currentNode.next != None:
            previousNode = currentNode
            currentNode = currentNode.next

        if previousNode != None:
            previousNode.next = None

    def toString(self):

        currentNode = self.headNode
        string = ''

        while currentNode != None:
            string = str(currentNode.data) if len(string) == 0 else string + ', ' + str(currentNode.data)
            currentNode = currentNode.next

        return string
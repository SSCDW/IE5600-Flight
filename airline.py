from linklist import *


class AirlineAlreadyEnrolledException(Exception):
    pass


class Airline():
    def __init__(self, Airline_Name, IATA_Code):
        self.Airline_Name = Airline_Name
        self.IATA_Code = IATA_Code
        # self.ariline_list =LinkedList(None)

    def get_fullname(self):
        return self.Airline_Name + ' ' + self.IATA_Code


class Airline_list():
    def __init__(self):

        self.airline_list = LinkedList(None)

    def add_Airline(self, airline):
        currentNode = self.airline_list.headNode
        name = airline.Airline_Name
        code = airline.IATA_Code
        whether_append = True  # judge whether append the new object
        if currentNode.data != None:
            if name != currentNode.data.Airline_Name or code != currentNode.data.IATA_Code:
                while currentNode.next != None:
                    if name == currentNode.next.data.Airline_Name and code == currentNode.next.data.IATA_Code:
                        whether_append = False
                        break
                    else:
                        currentNode = currentNode.next
                        # whether_append = True

                if whether_append == False:
                    raise AirlineAlreadyEnrolledException('Airline ' + name + ' ' + code + 'already Exist ')

                self.airline_list.append(airline)  # append the new record in the list

            else:
                raise AirlineAlreadyEnrolledException('Airline ' + name + ' ' + code + 'already Exist ')



        else:
            self.airline_list = LinkedList(airline)  # append the new record in the list
            # ariline_list.append(airline)#append the new record in the list

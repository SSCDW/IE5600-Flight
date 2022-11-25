from linklist import *
from airline import *
class AircraftAlreadyEnrolledException(Exception):
    pass


class Aircraft(Airline):
    def __init__(self, IATA_Code, Plane_Type):

        super().__init__(self, IATA_Code)
        self.IATA_Code = IATA_Code
        self.Plane_Type = Plane_Type
        self.Cabin_Class = {'Cabin Class F': {'Seat Configuration': [], 'start num': '', 'end num': ''},
                            'Cabin Class J': {'Seat Configuration': [], 'start num': '', 'end num': ''},
                            'Cabin Class Y': {'Seat Configuration': [], 'start num': '', 'end num': ''}}
        self.total_seats = 0  # total num of seats
        self.f_seats = 0
        self.j_seats = 0
        self.y_seats = 0
        # self.ariline_list =LinkedList(None)


    def get_cabin_class(self, key, list, start_num, end_num):
        if key == 'F':
            self.Cabin_Class['Cabin Class F']['Seat Configuration'] = list
            self.Cabin_Class['Cabin Class F']['start num'] = start_num
            self.Cabin_Class['Cabin Class F']['end num'] = end_num
        elif key == 'J':
            self.Cabin_Class['Cabin Class J']['Seat Configuration'] = list
            self.Cabin_Class['Cabin Class J']['start num'] = start_num
            self.Cabin_Class['Cabin Class J']['end num'] = end_num
        elif key == 'Y':
            self.Cabin_Class['Cabin Class Y']['Seat Configuration'] = list
            self.Cabin_Class['Cabin Class Y']['start num'] = start_num
            self.Cabin_Class['Cabin Class Y']['end num'] = end_num

    def calculate_seats(self):  # calculate total number of the seats

        # f =
        self.f_seats = (int(self.Cabin_Class['Cabin Class F']['end num'])
                        - int(self.Cabin_Class['Cabin Class F']['start num']) + 1) * sum(
            self.Cabin_Class['Cabin Class F']['Seat Configuration'])
        # j =
        self.j_seats = (int(self.Cabin_Class['Cabin Class J']['end num'])
                        - int(self.Cabin_Class['Cabin Class J']['start num']) + 1) * sum(
            self.Cabin_Class['Cabin Class J']['Seat Configuration'])
        # y =
        self.y_seats = (int(self.Cabin_Class['Cabin Class Y']['end num'])
                        - int(self.Cabin_Class['Cabin Class Y']['start num']) + 1) * sum(
            self.Cabin_Class['Cabin Class Y']['Seat Configuration'])
        self.total_seats = self.f_seats + self.j_seats + self.y_seats

    def print_info(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print('Aircraft Type {} created for {}'.format(self.Plane_Type, self.IATA_Code))
        for i in list(self.Cabin_Class.keys()):
            stratnum = self.Cabin_Class[i]['start num']
            endnum = self.Cabin_Class[i]['end num']
            start_alphabet = alphabet[0]
            end_alphabet = alphabet[sum(self.Cabin_Class[i]['Seat Configuration']) - 1]
            total_seats_in_key = (int(self.Cabin_Class[i]['end num']) - int(
                self.Cabin_Class[i]['start num']) + 1) * sum(self.Cabin_Class[i]['Seat Configuration'])

            print('{} -Seat {}{} to {}{} through {}{} to {}{},{} seats'
                  .format(i, stratnum, start_alphabet, stratnum, end_alphabet, endnum, start_alphabet, endnum,
                          end_alphabet, total_seats_in_key))

        print('Total {} seats'.format(self.total_seats))


class Aircraft_list():
    def __init__(self):
        self.aircraft_list = LinkedList(None)

    def add_Aircraft(self, aircraft):
        currentNode = self.aircraft_list.headNode
        Plane = aircraft.Plane_Type
        code = aircraft.IATA_Code
        whether_append = True  # judge whether append the new object
        check_count = 0
        if currentNode.data != None:  # 如果最开始的node是空的，直接不用判断加入新的object
            if Plane != currentNode.data.Plane_Type or code != currentNode.data.IATA_Code:  # 判断当head node的Plane_Type和IATA_Code不一样时，head node无重复，但next有可能有重复的元素
                while currentNode.next != None:  # 检查head node后面的元素
                    if Plane == currentNode.next.data.Plane_Type and code == currentNode.next.data.IATA_Code:  # 判断除head node之外有没有重复的
                        check_count = 0
                        for key_check in currentNode.next.data.Cabin_Class:  # 甚至要检查每个cabin class里的元素 = =
                            if aircraft.Cabin_Class[key_check]['Seat Configuration'] == \
                                    currentNode.next.data.Cabin_Class[key_check]['Seat Configuration'] and \
                                    aircraft.Cabin_Class[key_check]['start num'] == \
                                    currentNode.next.data.Cabin_Class[key_check]['start num'] and \
                                    aircraft.Cabin_Class[key_check]['end num'] == \
                                    currentNode.next.data.Cabin_Class[key_check]['end num']:
                                check_count += 1
                            if check_count == 3:
                                whether_append = False
                                raise AircraftAlreadyEnrolledException(
                                    'Aircraft ' + Plane + ' ' + 'IATA Code' + ' ' + code + ' ' + 'already Exist ')
                            currentNode = currentNode.next

                    else:
                        currentNode = currentNode.next
                        # whether_append = True

                if not whether_append:
                    raise AircraftAlreadyEnrolledException(
                        'Aircraft ' + Plane + ' ' + 'IATA Code' + ' ' + code + ' ' + 'already Exist ')

                self.aircraft_list.append(aircraft)  # append the new record in the list

            else:
                check_count = 0
                for key_check in list(currentNode.next.data.Cabin_Class.keys()):  # 甚至要检查每个cabin class里的元素 = =
                    if aircraft.Cabin_Class[key_check]['Seat Configuration'] == \
                            currentNode.next.data.Cabin_Class[key_check]['Seat Configuration'] and \
                            aircraft.Cabin_Class[key_check]['start num'] == \
                            currentNode.next.data.Cabin_Class[key_check]['start num'] and \
                            aircraft.Cabin_Class[key_check]['end num'] == currentNode.next.data.Cabin_Class[key_check][
                        'end num']:
                        check_count += 1
                    if check_count == 3:
                        whether_append = False
                        raise AircraftAlreadyEnrolledException(
                            'Aircraft ' + Plane + ' ' + 'IATA Code' + ' ' + code + ' ' + 'already Exist ')

                    self.aircraft_list.append(aircraft)  # append the new record in the list

        else:
            self.aircraft_list = LinkedList(aircraft)  # append the new record in the list
            # ariline_list.append(airline)#append the new record in the list

    # def add_Airline(self, airline):

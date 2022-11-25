from linklist import *
from airline import *
from aircraft import *
import datetime
import copy


class FlightAlreadyEnrolledException(Exception):
    pass


class Flight(Aircraft):
    def __init__(self, IATA_Code, Outbound, Return, Origin_IATA, Destin_IATA, Departure, Flight_Time, Stopover,
                 Plane_Type,
                 Cabin_Class=None, total_seats=0, f_seats=0, j_seats=0, y_seats=0):

        super().__init__(IATA_Code, Plane_Type)
        # self.IATA_Code = IATA_Code
        self.Outbound = Outbound
        self.Return = Return
        self.Origin_IATA = Origin_IATA
        self.Destin_IATA = Destin_IATA
        self.Departure = Departure
        self.Flight_Time = Flight_Time
        self.Stopover = Stopover
        self.Cabin_Class2 = {}



        self.Plane_Type = Plane_Type
        # self.Cabin_Class = Cabin_Class
        # self.total_seats = total_seats  # total num of seats
        # self.f_seats = f_seats
        # self.j_seats = j_seats
        # self.y_seats = y_seats
        # self.ariline_list =LinkedList(None)
        self.avaliable_seats = 0  # count avaliable seats
        self.customer_list = []
        self.booked_seats = set()  # 存储座位排布信息


    def get_flight_info(self, aircraft_list):  # 继承和获得之前创建的aircraft类的信息
        currentNode = aircraft_list.aircraft_list.headNode
        Plane = self.Plane_Type
        code = self.IATA_Code
        if currentNode.data != None:  # 其实这步在这里没必要，因为aircraft list肯定不为空
            if Plane != currentNode.data.Plane_Type or code != currentNode.data.IATA_Code:  # 判断当head node的Plane_Type和IATA_Code不一样时，head node无重复，但next有可能有重复的元素
                while currentNode.next != None:  # 检查head node后面的元素
                    if Plane != currentNode.next.data.Plane_Type or code != currentNode.next.data.IATA_Code:
                        currentNode = currentNode.next
                    else:
                        self.Cabin_Class = copy.deepcopy(currentNode.next.data.Cabin_Class)
                        self.total_seats = currentNode.next.data.total_seats
                        self.f_seats = currentNode.next.data.f_seats
                        self.j_seats = currentNode.next.data.j_seats
                        self.y_seats = currentNode.next.data.y_seats
                        break



            else:
                self.Cabin_Class = copy.deepcopy(currentNode.next.data.Cabin_Class)
                self.total_seats = currentNode.data.total_seats
                self.f_seats = currentNode.data.f_seats
                self.j_seats = currentNode.data.j_seats
                self.y_seats = currentNode.data.y_seats

    def get_fare_amount(self, fare_info):
        temp_dict = {}
        for key in list(self.Cabin_Class.keys()):  # 将价格信息加入到对应的cabin class中
            temp_dict['Fare Amount'] = fare_info[key]['Fare Amount']
            self.Cabin_Class[key].update(temp_dict)







# 存储flight的信息，并且有验证是否重复功能
class Flight_list():
    def __init__(self):
        self.flight_list = LinkedList(None)

    def add_flight(self, flight):
        currentNode = self.flight_list.headNode  # 照例先取个headNode
        # 取出object要检验的特性
        code = flight.IATA_Code
        outbound = flight.Outbound
        return_num = flight.Return
        origin_iata_code = flight.Origin_IATA
        destin_iata_code = flight.Destin_IATA
        depature_time = flight.Departure
        flight_time = flight.Flight_Time
        stopover = flight.Stopover
        aircraft_type = flight.Plane_Type
        # 开始检验
        whether_append = True  # judge whether append the new object
        if currentNode.data != None:  # 先判断headNode是否为空，如果是空则可直接把object存入
            judge1 = 0
            for keys in list(currentNode.data.__dict__.keys()):
                if currentNode.data.__dict__[keys] == flight.__dict__[keys]:
                    judge1 += 1

            if judge1 <= 18:  # 当headNode并没有全部相等时,检查下面的nextNode  重要：！因为后续写代码的时候还增加了一些特征，但是不考虑了，因为仅在输入新Flight的时候使用
                while currentNode.next != None:  # 检查head node后面的元素
                    judge2 = 0
                    for keys in list(currentNode.next.data.__dict__.keys()):
                        if currentNode.next.data.__dict__[keys] == flight.__dict__[keys]:
                            judge2 += 1
                    if judge2 <= 18:  # 当nextNode并没有全部相等时
                        currentNode = currentNode.next
                    else:
                        whether_append = False
                        raise FlightAlreadyEnrolledException('Flight already Exist !')

                if whether_append:  # 检查完所有的，如果没有重复的，则加入链表
                    self.flight_list.append(flight)  # append the new record in the list


            else:
                whether_append = False
                raise FlightAlreadyEnrolledException('Flight already Exist !')


        else:
            self.flight_list = LinkedList(flight)  # append the new record in the list

        whether_append = True  # judge whether append the new object to the linklist
        check_count = 0

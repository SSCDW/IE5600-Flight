from linklist import *
from airline import *
from aircraft import *
import datetime
import copy

class Customer():
    def __init__(self, trip_type, origin, destination, departure_date, cabin_class, num_passengers):
        self.trip_type = trip_type
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.cabin_class = cabin_class
        self.num_passengers = num_passengers
        self.result_list = []
        self.order = []
        self.seat = []

    def search_all_stopover(self, currentnode_data, flight_list):
        currentnode_data = currentnode_data
        currentNode = flight_list.flight_list.headNode
        return_list = []
        while currentNode != None:
            if currentNode.data.Destin_IATA == self.destination and currentnode_data.Destin_IATA ==currentNode.data.Origin_IATA and currentnode_data.Departure + datetime.timedelta(hours=int(currentnode_data.Flight_Time[0]),minutes=int(currentnode_data.Flight_Time[2])) + datetime.timedelta(hours=2) <= currentNode.data.Departure < currentnode_data.Departure + datetime.timedelta(hours=int(currentnode_data.Flight_Time[0]),minutes=int(currentnode_data.Flight_Time[2])) + datetime.timedelta(hours=24):
                return_list.append([currentnode_data, currentNode.data])
            if currentnode_data.Destin_IATA == currentNode.data.Origin_IATA and currentnode_data.Departure + datetime.timedelta(hours=int(currentnode_data.Flight_Time[0]),minutes=int(currentnode_data.Flight_Time[2])) + datetime.timedelta(hours=2) <= currentNode.data.Departure < currentnode_data.Departure + datetime.timedelta(hours=int(currentnode_data.Flight_Time[0]),minutes=int(currentnode_data.Flight_Time[2])) + datetime.timedelta(hours=24):
                node_return = self.search_all_stopover(currentNode.data, flight_list)
                if node_return != []:
                    for result in node_return:
                        return_list.append([currentNode.data] + result)
            currentNode = currentNode.next
        return return_list


    def requirement_search(self, flight_list):
        if self.trip_type == 'One-Way':  # 对于单程票和双程票的查询结果有点不同，这里先是单程票
            currentNode = flight_list.flight_list.headNode
            temp_IATA = None
            temp_datetime = None
            avaliable_seats = None
            flight_time = None

            while currentNode != None:
                if currentNode.data.Origin_IATA == self.origin and currentNode.data.Destin_IATA == self.destination and self.departure_date - datetime.timedelta(hours=24) <= currentNode.data.Departure <= self.departure_date + datetime.timedelta(hours=24):#node起点和终点都ok
                    self.result_list.append([currentNode.data])
                    currentNode = currentNode.next
                    continue
                elif currentNode.data.Origin_IATA == self.origin and self.departure_date - datetime.timedelta(hours=24) <= currentNode.data.Departure <= self.departure_date + datetime.timedelta(hours=24):
                    list_search_result = self.search_all_stopover(currentNode.data, flight_list)
                    if list_search_result != []:
                        self.result_list.extend(list_search_result)
                        #for single in list_search_result:
                        #self.result_list.append([currentNode.data] + single)

                currentNode = currentNode.next
    def show_result(self):
        count_result = 1
        for i in self.result_list:
            list_fare_count = []
            print("result {}".format(count_result))
            for j in i:
                if self.cabin_class == 'Y':
                    list_fare_count.append(int(j.Cabin_Class['Cabin Class Y']['Fare Amount'][1:]))
                    print('{}{},{} to {}, Depart {},Arrive {},Class{} {}'.format(j.IATA_Code,j.Outbound,j.Origin_IATA,j.Destin_IATA,j.Departure,j.Departure,self.cabin_class,j.Cabin_Class['Cabin Class Y']['Fare Amount']))
                elif self.cabin_class == 'F':
                    list_fare_count.append(int(j.Cabin_Class['Cabin Class F']['Fare Amount'][1:]))
                    print('{}{},{} to {}, Depart {},Arrive {},Class{} {}'.format(j.IATA_Code, j.Outbound, j.Origin_IATA,
                                                                                 j.Destin_IATA, j.Departure,
                                                                                 j.Departure, self.cabin_class,
                                                                                 j.Cabin_Class['Cabin Class F'][
                                                                                     'Fare Amount']))
                elif self.cabin_class == 'J':
                    list_fare_count.append(int(j.Cabin_Class['Cabin Class J']['Fare Amount'][1:]))
                    print('{}{},{} to {}, Depart {},Arrive {},Class{} {}'.format(j.IATA_Code, j.Outbound, j.Origin_IATA,
                                                                             j.Destin_IATA, j.Departure,
                                                                             j.Departure, self.cabin_class,
                                                                             j.Cabin_Class['Cabin Class J'][
                                                                                 'Fare Amount']))

            print('{} stopover, Total Fare ${}'.format(len(i)-1,int(self.num_passengers)*sum(list_fare_count)))
            count_result+=1
    def select_result(self,number,seat):
        select_flight = self.result_list[number-1]
        self.seat.extend(seat)
        self.order.append(select_flight)
        for i in select_flight:
                i.customer_list.append(self)












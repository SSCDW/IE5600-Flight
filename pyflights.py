from linklist import *
from airline import *
from aircraft import *
from customer import *
from flight import *
import datetime







def main():
    # Initial Data of Airline
    airline1 = ['Singapore Airlines', 'SQ']
    airline2 = ['Qantas', 'QF']
    airline1_class = Airline(airline1[0], airline1[1])
    airline2_class = Airline(airline2[0], airline2[1])
    airline_linklist = Airline_list()
    airline_linklist.add_Airline(airline1_class)
    airline_linklist.add_Airline(airline2_class)

    # Initial Data of AirCraft
    # aircraft1
    aircraft_list = Aircraft_list()
    aircraft1 = ['SQ', 'Boeing 747', {'F': {'Seat Configuration': [1, 1, 1], 'start num': '1', 'end num': '10'},
                                      'J': {'Seat Configuration': [2, 2, 2], 'start num': '11', 'end num': '20'},
                                      'Y': {'Seat Configuration': [3, 4, 3], 'start num': '21', 'end num': '50'}}]
    aircraft1_class = Aircraft(aircraft1[0], aircraft1[1])
    for key in list(aircraft1[2].keys()):
        aircraft1_class.get_cabin_class(key, aircraft1[2][key]['Seat Configuration'], aircraft1[2][key]['start num'],
                                        aircraft1[2][key]['end num'])

    aircraft1_class.calculate_seats()  # 得到此飞机类型的座位信息
    aircraft_list.add_Aircraft(aircraft1_class)
    # aircraft2
    aircraft2 = ['QF', 'Boeing 747', {'F': {'Seat Configuration': [1, 1, 1], 'start num': '1', 'end num': '10'},
                                      'J': {'Seat Configuration': [2, 2, 2], 'start num': '11', 'end num': '20'},
                                      'Y': {'Seat Configuration': [3, 4, 3], 'start num': '21', 'end num': '50'}}]
    aircraft2_class = Aircraft(aircraft2[0], aircraft2[1])
    for key in list(aircraft2[2].keys()):
        aircraft2_class.get_cabin_class(key, aircraft2[2][key]['Seat Configuration'], aircraft2[2][key]['start num'],
                                        aircraft2[2][key]['end num'])

    aircraft2_class.calculate_seats()
    aircraft_list.add_Aircraft(aircraft2_class)

    # Initial Data for Flight
    format1 = '%d' + ' ' + '%b' + ' ' + '%y' + ',' + ' ' + '%I' + ':' + '%M' + ' ' + '%p'  # 调整输入的datetime信息为标准的datetime数据类型
    flight_list = Flight_list()
    # Initial Flight 1
    flight1 = ['SQ', '123', '321', 'SIN', 'NRT', '5 Dec 22, 10:00 AM', ['6', 'hour', '30', 'minute'], ['3', 'hour'],
               'Boeing 747']
    flight1_canbinclass_dict = {
        'Cabin Class F': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$2000'},
        'Cabin Class J': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$1000'},
        'Cabin Class Y': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$500'}}
    flight1_datetime = datetime.datetime.strptime(flight1[5].strip(), format1)
    flight1_class1 = Flight(flight1[0], flight1[1], flight1[2], flight1[3], flight1[4], flight1_datetime, flight1[6],
                            flight1[7], flight1[8])
    flight1_class1.get_flight_info(aircraft_list)
    flight1_class1.get_fare_amount(flight1_canbinclass_dict)
    flight_list.add_flight(flight1_class1)
    # Initial Flight 2
    flight2 = ['SQ', '456', '654', 'SYD', 'SIN', '4 Dec 22, 10:00 PM', ['8', 'hour', '0', 'minute'], ['2', 'hour'],
               'Boeing 747']
    flight2_canbinclass_dict = {
        'Cabin Class F': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount':  '$1500'},
        'Cabin Class J': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$750'},
        'Cabin Class Y': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$300'}}
    flight2_datetime = datetime.datetime.strptime(flight2[5].strip(), format1)
    flight2_class2 = Flight(flight2[0], flight2[1], flight2[2], flight2[3], flight2[4], flight2_datetime, flight2[6],
                            flight2[7], flight2[8])
    flight2_class2.get_flight_info(aircraft_list)
    flight2_class2.get_fare_amount(flight2_canbinclass_dict)
    flight_list.add_flight(flight2_class2)
    # Initial Flight 3
    flight3 = ['SQ', '789', '987', 'SYD', 'NRT', '5 Dec 22, 09:00 AM', ['14', 'hour', '0', 'minute'], ['2', 'hour'],
               'Boeing 747']
    flight3_canbinclass_dict = {
        'Cabin Class F': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$3500'},
        'Cabin Class J': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$2500'},
        'Cabin Class Y': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$1500'}}
    flight3_datetime = datetime.datetime.strptime(flight3[5].strip(), format1)
    flight3_class3 = Flight(flight3[0], flight3[1], flight3[2], flight3[3], flight3[4], flight3_datetime, flight3[6],
                            flight3[7], flight3[8])
    flight3_class3.get_flight_info(aircraft_list)
    flight3_class3.get_fare_amount(flight3_canbinclass_dict)
    flight_list.add_flight(flight3_class3)
    # Initial Flight 4
    flight4 = ['QF', '789', '987', 'SYD', 'NRT', '5 Dec 22, 01:00 PM', ['14', 'hour', '30', 'minute'], ['2', 'hour'],
               'Boeing 747']
    flight4_canbinclass_dict = {
        'Cabin Class F': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$3200'},
        'Cabin Class J': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$2200'},
        'Cabin Class Y': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$1200'}}
    flight4_datetime = datetime.datetime.strptime(flight4[5].strip(), format1)
    flight4_class4 = Flight(flight4[0], flight4[1], flight4[2], flight4[3], flight4[4], flight4_datetime, flight4[6],
                            flight4[7], flight4[8])
    flight4_class4.get_flight_info(aircraft_list)
    flight4_class4.get_fare_amount(flight4_canbinclass_dict)
    flight_list.add_flight(flight4_class4)
    # Initial Flight 5
    flight5 = ['SQ', '123', '321', 'SIN', 'NRT', '12 Dec 22, 10:00 AM', ['6', 'hour', '30', 'minute'], ['3', 'hour'],
               'Boeing 747']
    flight5_canbinclass_dict = {
        'Cabin Class F': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$2000'},
        'Cabin Class J': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$1000'},
        'Cabin Class Y': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$500'}}
    flight5_datetime = datetime.datetime.strptime(flight5[5].strip(), format1)
    flight5_class5 = Flight(flight5[0], flight5[1], flight5[2], flight5[3], flight5[4], flight5_datetime, flight5[6],
                            flight5[7], flight5[8])
    flight5_class5.get_flight_info(aircraft_list)
    flight5_class5.get_fare_amount(flight5_canbinclass_dict)
    flight_list.add_flight(flight5_class5)
    # Initial Flight 6
    flight6 = ['SQ', '456', '654', 'SYD', 'SIN', '11 Dec 22, 10:00 PM', ['8', 'hour', '0', 'minute'], ['2', 'hour'],
               'Boeing 747']
    flight6_canbinclass_dict = {
        'Cabin Class F': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$1500'},
        'Cabin Class J': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$750'},
        'Cabin Class Y': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$300'}}
    flight6_datetime = datetime.datetime.strptime(flight6[5].strip(), format1)
    flight6_class6 = Flight(flight6[0], flight6[1], flight6[2], flight6[3], flight6[4], flight6_datetime, flight6[6],
                            flight6[7], flight6[8])
    flight6_class6.get_flight_info(aircraft_list)
    flight6_class6.get_fare_amount(flight6_canbinclass_dict)
    flight_list.add_flight(flight6_class6)
    # Initial Flight 7
    flight7 = ['SQ', '789', '987', 'SYD', 'NRT', '12 Dec 22, 09:00 AM', ['14', 'hour', '0', 'minute'], ['2', 'hour'],
               'Boeing 747']
    flight7_canbinclass_dict = {
        'Cabin Class F': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$3500'},
        'Cabin Class J': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$2500'},
        'Cabin Class Y': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$1500'}}
    flight7_datetime = datetime.datetime.strptime(flight7[5].strip(), format1)
    flight7_class7 = Flight(flight7[0], flight7[1], flight7[2], flight7[3], flight7[4], flight7_datetime, flight7[6],
                            flight7[7], flight7[8])
    flight7_class7.get_flight_info(aircraft_list)
    flight7_class7.get_fare_amount(flight7_canbinclass_dict)
    flight_list.add_flight(flight7_class7)
    # Initial Flight 8
    flight8 = ['QF', '789', '987', 'SYD', 'NRT', '12 Dec 22, 01:00 PM', ['14', 'hour', '30', 'minute'], ['2', 'hour'],
               'Boeing 747']
    flight8_canbinclass_dict = {
        'Cabin Class F': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$3200'},
        'Cabin Class J': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$2200'},
        'Cabin Class Y': {'Seat Configuration': [], 'start num': '', 'end num': '', 'Fare Amount': '$1200'}}
    flight8_datetime = datetime.datetime.strptime(flight8[5].strip(), format1)
    flight8_class8 = Flight(flight8[0], flight8[1], flight8[2], flight8[3], flight8[4], flight8_datetime, flight8[6],
                            flight8[7], flight8[8])
    flight8_class8.get_flight_info(aircraft_list)
    flight8_class8.get_fare_amount(flight8_canbinclass_dict)
    flight_list.add_flight(flight8_class8)


    #start loops

    dic_info = {}
    while True:
        key = input('Please choose activation(1 is for Create Airline, 2 is for Create Aircraft Type, 3 is for Create Flight, 4 is for Search and Book Flight:')
        if key == '1':  # Create Airline

            a = input('please input the Airline Name: ')
            b = input('please input the IATA Code: ')

            airline3 = Airline(a, b)
            try:

                airline_linklist.add_Airline(airline3)

            except AirlineAlreadyEnrolledException as err:

                if len(err.args) > 0: print(err.args[0])
        # airline_linklist.add_Airline(airline3)

        elif key == '2':  # Create Aircraft Type
            c = input('Please input IATA Code: ')
            d = input('Please input Aircraft Type Name:')
            loops = True
            temp_aircraft = Aircraft(c, d)  # New object aircraft
            while loops:
                action = input('Please select whether add a class (input "Y"or "y" as Yes, input "N" or "n"as No):')
                if action == 'Y' or action == 'y':
                    temp_class = ''
                    loop2 = True

                    while loop2:
                        cabin_class = input('Please input a cabin class ("F","J","Y"):')
                        if cabin_class in ['F', 'J', 'Y']:

                            if cabin_class == 'F':
                                temp_class = 'Cabin Class F'
                            elif cabin_class == 'J':
                                temp_class = 'Cabin Class J'
                            elif cabin_class == 'Y':
                                temp_class = 'Cabin Class Y'

                            seat_configuration = []
                            seat_c1, seat_c2, seat_c3 = input(
                                'Please input a seat configuration:(example: 1-1-1):').split('-')
                            seat_configuration = [int(seat_c1), int(seat_c2), int(seat_c3)]

                            start_row = input('Starting Row Number:')
                            end_row = input('Starting Row Number:')
                            temp_aircraft.get_cabin_class(cabin_class, seat_configuration, start_row, end_row)
                            loop2 = False


                        else:  # cabin_class not in ['F', 'J', 'Y']:#print error information

                            print('Input error, please input correct cabin class')
                            loop2 = False

                    # loops = True

                elif action == 'N' or action == 'n':  # end the input
                    loops = False  # end loops
                    try:  # 检验输入的飞机是否已存在

                        aircraft_list.add_Aircraft(temp_aircraft)
                        temp_aircraft.calculate_seats()  # 计算有多少seats，但是这个应该让下面的print_info()函数内部调用最好，这里因为不知道后面还需不需要先写成外面调用
                        temp_aircraft.print_info()  # print出输入飞机的信息

                    except AircraftAlreadyEnrolledException as err:
                        if len(err.args) > 0: print(err.args[0])

        elif key == '3':  # Create Flight
            iata_code = input('Please input IATA Code: ')
            outbound_num = input('Please input Outbound Flight Number:')
            return_num = input('Please input Return Flight Number (Optional):')
            origin_iata = input('Please input Origin Airport IATA Code:')
            destination_iata = input('Please input Destination Airport IATA Code:')
            departure = input('Please input Departure Date/Time(example:5 Dec 22, 10:00 AM):')  # 出发时间，存为datetime
            flight_time = []
            flight_time = input('Please input Flight Time:').split(' ')  # 飞行时间，存到list里
            stopover = []
            stopover = input('Please input Stopover Duration:').split(' ')  # 停留时间，存到list里
            aircraft = input('Please input Aircraft Type Name:')
            # 将出发时间存成datetime数据格式
            format1 = '%d' + ' ' + '%b' + ' ' + '%y' + ',' + ' ' + '%I' + ':' + '%M' + ' ' + '%p'  # 调整输入的datetime信息为标准的datetime数据类型
            departure_departure_datetime = datetime.datetime.strptime(departure.strip(), format1)  # 正确的储存形式

            fare_dict_temp = {'Cabin Class F': {'Seat Configuration': [], 'start num': '', 'end num': ''},
                              'Cabin Class J': {'Seat Configuration': [], 'start num': '', 'end num': ''},
                              'Cabin Class Y': {'Seat Configuration': [], 'start num': '',
                                                'end num': ''}}  # 存储每个Cabin Class的价格信息

            flight_temp = Flight(iata_code, outbound_num, return_num, origin_iata, destination_iata,
                                 departure_departure_datetime,
                                 flight_time, stopover, aircraft, fare_dict_temp)  # 先创建下object

            flight_temp.get_flight_info(aircraft_list)  # 得到此类飞机的座位信息
            if flight_temp.Cabin_Class['Cabin Class J'][
                'Seat Configuration'] == []:  # 先判断是否已经有定义好的此类飞机（此步骤非必要或唯一，只是多一步检验）
                print('There is no such aricraft type exist!')
                continue
            else:  # 当成功输入以上内容，可以继续输入每个cabin class的价格信息
                for keys in list(fare_dict_temp.keys()):  # 输入每个cabin class的价格
                    if keys == 'Cabin Class F':
                        fare_amount = input('Please input fare of cabin class F:（example:$3200):')
                        fare_dict_temp[keys]['Fare Amount'] = fare_amount
                    elif keys == 'Cabin Class J':
                        fare_amount = input('Please input fare of cabin class J:（example:$3200):')
                        fare_dict_temp[keys]['Fare Amount'] = fare_amount
                    elif keys == 'Cabin Class Y':
                        fare_amount = input('Please input fare of cabin class Y:（example:$3200):')
                        fare_dict_temp[keys]['Fare Amount'] = fare_amount
            flight_temp.get_fare_amount(fare_dict_temp)  # 将fare的信息加入到Flight object的对应cabin class中
            # 接下来检验是否重复，如果不重复，则可以储存，否则报错
            try:  # 检验输入的Flight是否已存在
                flight_list.add_flight(flight_temp)
            except FlightAlreadyEnrolledException as err:
                if len(err.args) > 0: print(err.args[0])
        elif key == '4':#Customer book flight
            trip_type = input('Please input your trip type (One-Way or Return):')
            origin = input('Please input your origin:')
            destination = input('Please input your destination:')
            format2 = '%d' + ' ' + '%b' + ' ' + '%y'  # 调整输入的datetime信息为标准的datetime数据类型
            departure_date = input('Please input the departure date(Example: 5 Dec 22):')
            departure_date_datetime = datetime.datetime.strptime(departure_date.strip(), format2)  # 正确的储存形式
            cabin_class_selection = input('Please select your cabin class(F,J,Y or No Preference):')
            num_passenger = input('Please input a number of passengers:')
            customer_temp = Customer(trip_type,origin,destination,departure_date_datetime,cabin_class_selection,num_passenger)
            customer_temp.requirement_search(flight_list)
            customer_temp.show_result()
            select_result = input('Please select Flight:')
            select_seat_list = []
            for i in range(int(num_passenger)):#输入用户需要的座位号，同时检查其选择是否可行
                for j in range(len(customer_temp.result_list[int(select_result)-1])):
                    select_seat = input('Please select Seat for Passenger {} (Example:1-21A):'.format(i+1))
                    select_seat_list.append(select_seat)
                customer_temp.select_result(int(select_result),select_seat_list)
            print('Your flight is confirmed!')





if __name__ == '__main__':
    main()

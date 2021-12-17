#  Sean Pharris StuID#: 001307124
import sys
from csv_read import *
from package import *

#  retrieves objects from table/CSV file
package_table = get_package_csv()
#  retrieves objects from table/CSV file
distance_table = get_distance_csv()
#  retrieves objects from table/CSV file
locations = get_address_csv()


#  O(N^2) -- Function changes status of package when delivered and gives delivery truck parameters
def status_update(truck, time_delivery):
    #  sets starting distance
    distance_total = 0
    #  sets distance of starting point, which is 0 because there is no travel distance to where the truck starts
    starting_point = 0
    #  O(N) -- goes through all packages
    for i in range(len(truck)):
        package, starting_point, dist = find_nearest(starting_point, truck)  # closest package address and distance
        time_delivery += int((dist / 18) * 60)  # distance of next delivery/speed of truck * minutes in hour
        package.time_delivered = format_time(time_delivery)
        package.status_of_package = "delivered"  # status change after delivery
        distance_total += dist
        truck.remove(package.package_id)  # the package is removed from list
    hub_dist = float(distance_table[starting_point][0])  # float used for distance -- ex. 7.2 miles
    distance_total += hub_dist
    time_delivery += int((hub_dist / 18) * 60)
    return distance_total  # tracking distance for reporting


#  O(1) -- formats time for reporting
def format_time(minutes):
    hour_format = "{:02d}".format(int(minutes / 60))
    minute_format = "{:02d}".format(minutes % 60)
    time_format = hour_format + ':' + minute_format
    return time_format


track_delivery = []


#  O(N) -- manually loaded packages, truck start times, and distance trackers
def make_deliveries():
    truck1 = [13, 14, 15, 16, 19, 20, 1, 37, 40, 21, 4, 26, 34, 29, 30]  # truck1 list with preset packages
    truck1_start_time = 480  # truck1 starts at 08:00 (480 minutes / 60 minutes = 8:00)
    truck2 = [2, 5, 7, 8, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35, 39]
    truck2_start_time = 540  # truck2 starts at 09:00 (540 minutes / 60 minutes = 9:00)
    truck3 = [3, 9, 18, 36, 38, 6, 25, 28, 31, 32, 40]
    truck3_start_time = 600  # truck3 starts at 10:00 (600 minutes / 60 minutes = 10:00)

    for i in truck1:
        package = package_table.search(i)
        package.start_time = "08:00"
    for i in truck2:
        package = package_table.search(i)
        package.start_time = "09:00"
    for i in truck3:
        package = package_table.search(i)
        package.start_time = "10:00"

    truck1_mileage = status_update(truck1, truck1_start_time)  # sets packages/start time of truck in "status update"
    track_delivery.append(truck1_mileage)  # adds truck mileage to list

    truck2_mileage = status_update(truck2, truck2_start_time)  # sets packages/start time of truck in "status update"
    track_delivery.append(truck2_mileage)  # adds truck mileage to list

    truck3_mileage = status_update(truck3, truck3_start_time)  # sets packages/start time of truck in "status update"
    track_delivery.append(truck3_mileage)  # adds truck mileage to list

    all_mileage = truck1_mileage + truck2_mileage + truck3_mileage  # sums all truck distances
    track_delivery.append(all_mileage)  # adds all truck distances to list


#  Nearest neighbor algo
def find_nearest(delivered_now, out_for_del):
    #  set nearest distance value
    nearest = 18.0
    #  set nearest delivery
    delivery_near = None
    #  set nearest address
    address_near = None
    #  find next package
    for package_number in out_for_del:
        #  get the package
        package = package_table.search(package_number)
        #  get location from dictionary
        package_address_number = locations[package.address][0]
        #  if the next location is greater than the current (at start is 0)
        if package_address_number > delivered_now:
            #  then get the difference between delivery stops
            distance = float(distance_table[package_address_number][delivered_now])
        else:
            distance = float(distance_table[delivered_now][package_address_number])
            #  make sure this is the shortest distance possible between stops
        if distance < nearest:
            nearest = distance
            delivery_near = package
            address_near = package_address_number
    return delivery_near, address_near, nearest


#  O(1) -- initial ui on program start
def intro_ui():
    print('______________________________________________________________')
    print("                   WGUPS Main Menu        \n"
          "type the letter to see desired information\n"
          "   a - distances traveled by each truck   \n"
          "   b - package information by time        \n"
          "   c - package information by package id  \n"
          "   d - exit program                       \n")
    print('______________________________________________________________')
    return intro_ui


#  O(N) -- output for 'a'
def distance_ui():
    print('Distance Menu')
    print("Type '1', '2', '3', or 'all' to see desired delivery truck \n"
          " Type 'r' to return to main menu")
    print('______________________________________________________________')
    x = input()
    if x == '1':
        print("First truck's total distance: %.2f miles" % track_delivery[0])
        print('______________________________________________________________')
        distance_ui()
    elif x == '2':
        print("Second truck's total distance: %.2f miles" % track_delivery[1])
        print('______________________________________________________________')
        distance_ui()
    elif x == '3':
        print("Third truck's total distance: %.2f miles" % track_delivery[2])
        print('______________________________________________________________')
        distance_ui()
    elif x == 'all':
        print("Total of all truck's distance: %.2f miles" % track_delivery[3])
        print('______________________________________________________________')
        distance_ui()
    elif x == 'r':
        intro_ui()


#  O(N^2) -- output for 'b'
def time_ui():
    print("Type time of interest with the format of HH:MM")
    print('______________________________________________________________')
    time1 = input()
    time2 = input()
    if ":" in time1 and time2:
        time_range = []
        out_of_range = []
        for i in range(1, package_table.list_items() + 1):
            p_lookup = package_table.search(i)
            if time1 <= p_lookup.time_delivered <= time2:
                time_range.append(p_lookup)
            elif p_lookup.time_delivered < time1:
                time_range.append(p_lookup)
            elif p_lookup.start_time > time2:
                p_lookup.status_of_package = "At the hub"
                out_of_range.append(p_lookup)
            else:
                p_lookup.status_of_package = "en route"
                out_of_range.append(p_lookup)
        print("Status of all packages between: %s" % time1, " and  %s:" % time2)
        print("Packages that have been delivered")
        print('______________________________________________________________')
        for p_lookup in time_range:
            p_lookup.time_ui_output()
        print('______________________________________________________________')
        print("Packages that have not been delivered")
        print('______________________________________________________________')
        for p_lookup in out_of_range:
            p_lookup.time_ui_not_del()


#  O(N) -- output for 'c'
def each_package_ui():
    print("Type the package id of interest")
    print('______________________________________________________________')
    x = input()
    try:
        pt = package_table.search(int(x))
        if int(x) in range(1, package_table.list_items() + 1):
            pt.package_id_interface()
            pt.address_interface()
            pt.deadline_interface()
            pt.city_interface()
            pt.zip_interface()
            pt.weight_interface()
            pt.status_interface()
            pt.delivery_time_interface()
        else:
            print("invalid input")
            print('______________________________________________________________')
    except Exception:
        print("invalid input")
        print('______________________________________________________________')


#  O(N)
if __name__ == '__main__':
    make_deliveries()
    intro_ui()
    #  While loop for user interface
    #  The following funtions are located in user_interface
    x = ''
    while x == 'a' or 'b' or 'c' or 'd':  # long as user input a, b, c, or d
        x = input()
        if x == 'a':
            distance_ui()
        elif x == 'b':
            time_ui()
            intro_ui()
        elif x == 'c':
            each_package_ui()
            intro_ui()
        elif x == 'd':  # d -- exits program
            sys.exit()
        elif x != 'a' or 'b' or 'c' or 'd':
            print('invalid input')
            intro_ui()

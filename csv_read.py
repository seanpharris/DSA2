import csv
from hashtable import ChainingHashTable
from package import Package


#  stores package data from  WGUPS Package File.csv file used to pass to trucks list
package_list = []
#  stores distance data from WGUPS Distance Table.csv file used for distance
distances = []
#  dictionary for delivery locations from WGUPS Address File.csv
locations = {}
#  calls ChainingHashTable class for functions used on the tables
package_table = ChainingHashTable()


#  O(N) -- Retrieves data from package CSV file and creates each item as an object in the table
def get_package_csv():
    with open("WGUPS Package File.csv") as infile:
        csv_reader = csv.reader(infile)
        for row in csv_reader:
            pack = Package(row)
            package_table.insert(pack.package_id, pack)
        return package_table


#  O(N) -- Retrieves data from distance CSV file and creates each item as an object in the table
def get_distance_csv():
    with open("WGUPS Distance Table.csv") as infile:
        distance_table = []
        csv_reader = csv.reader(infile)
        for row in csv_reader:
            distance_table.append(row)
        return distance_table


#  O(N) -- Retrieves data from distance CSV file and creates each item as an object in the table
def get_address_csv():
    with open("WGUPS Address File.csv") as infile:
        address_dict = {}
        csv_reader = csv.reader(infile)
        for row in csv_reader:
            address_dict[row[0]] = [int(row[1]), row[2]]
        return address_dict

# Class: Package - stores info related to the package
class Package(object):
    def __init__(self, package_list):
        self.package_id = int(package_list[0])
        self.address = package_list[1]
        self.city = package_list[2]
        self.state = package_list[3]
        self.zip = package_list[4]
        self.deadline = package_list[5]
        self.weight = package_list[6]
        self.special_notes = package_list[7]
        self.time_delivered = "00:00"
        self.status_of_package = "At the hub"
        self.start_time = "00:00:"

    #  function to print packaging id
    def package_id_interface(self):
        print("Package ID: %i" % self.package_id)

    #  function to print package address
    def address_interface(self):
        print("Address:  %s" % self.address)

    #  function to print city of address
    def city_interface(self):
        print("City: %s" % self.city)

    #  function to print state of address
    def state_interface(self):
        print("State: %s" % self.state)

    #  function to print zip of address
    def zip_interface(self):
        print("Zip: %s" % self.zip)

    #  function to print the time deadline for the delivery arrival
    def deadline_interface(self):
        print("Deadline: %s" % self.deadline)

    #  function to print the weight of the package
    def weight_interface(self):
        print("Weight: %s" % self.weight)

    #  function to print the special notes for the package
    def special_note_interface(self):
        print("Special Notes: %s" % self.special_notes)

    #  function to print the time the package is delivered
    def delivery_time_interface(self):
        print("Delivered at: %s" % self.time_delivered)

    # function to print the status of the package
    def status_interface(self):
        print("Status: %s" % self.status_of_package)

    def time_ui_output(self):
        print("Package ID: %i" % self.package_id, "Delivered at: %s" % self.time_delivered, "Status: %s" % self.status_of_package, "Address:  %s" % self.address)

    def time_ui_not_del(self):
        print("Package ID: %i" % self.package_id, "Status: %s" % self.status_of_package, "Address:  %s" % self.address)

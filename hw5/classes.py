import csv 

class Record:
    def __init__(self, phone_number, address=None):
        self.phone_number = phone_number  # this should be unique
        self.address = address

    def __str__(self):
        return f"{self.phone_number} {self.address}"

    @classmethod
    def from_csv(cls, fp):
        with open(fp, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                return cls(i["phone_number"], i["address"])


class Person(Record):
    def __init__(self, first_name, last_name, email, phone_number, address=None):
        super().__init__(phone_number, address)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email  # this should be unique

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.phone_number} {self.address}"

    @classmethod
    def from_csv(cls, fp):
        with open(fp, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                return cls(i["first_name"], 
                    i["last_name"],
                    i["email"],
                    i["phone_number"],
                    i["address"])


class Organization(Record):
    def __init__(self, name, category, phone_number, address):
        super().__init__(phone_number, address)
        self.name = name  # this should be unique
        self.category = category

    @classmethod
    def from_csv(cls,fp):
       with open(fp,newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                return cls(i["name"],i["category"],i["phone_number"],i["address"])

    def __str__(self):
        return f"{self.name} {self.category} {self.phone_number} {self.address}"


class AddressBook:
    def __init__(self, fp):
        self.fp = fp

    def validate_person(self,data):
        with open(self.fp,newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                if data["phone_number"] == int(i["phone_number"]):
                    raise ValueError("phone_number already exists")
                elif data["email"] == i["email"]:
                    raise ValueError("email already exists")
                else:
                    return "validation was successful"

    def validate_org(self, data):
        with open(self.fp,newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                if data["name"] == i["name"]:
                    raise ValueError("name already exists")
                else:
                    return "validation was successful"

    def add_record(self, type_, data):
        if type_ == "Person":
            self.validate_person(data)
        elif type_ == "Organization":
            self.validate_org(data)
        with open(self.fp, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow((type_,*data.values()))

    def find_record(self, type_, search_term):
        with open("address_book.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                if type_ == "all":
                    if search_term.lower() in i.values():
                        print(i)
                elif type_ == i["type"]:
                    if search_term.lower() in i.values():
                        print(i)


    def get_records(self, type_):
        with open("address_book.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                if type_ == "all":
                    print(i)
                elif type_ == i["type"]:
                    print(i)


#     # def import_from_csv(self, fp):
#     #     with open("address_book.csv",newline="") as csvfile:
#     #         reader = csv.DictReader(csvfile)
#     #         for i in reader:
#     #             self.fp = (i["type"],
#     #                 i["phone_number"],
#     #                 i["address"],
#     #                 i["name"],
#     #                 i["category"],
#     #                 i["first_name"],
#     #                 i["last_name"],
#     #                 i["email"])
#     #     return self.fp


# a1 = Organization("dima","aut","1556","45662")
# a2 = Organization.from_csv(["dima","aut","1556","45662"])
# print(a2)
# r1 = Record.from_csv(["fff","1556"])
# print(r1)

# p1 = Person("Misha","Pupkin","los@gmai.com",456)

# addbook = AddressBook(["leha","dio",42,"none"])
# # print(addbook)
# # print(addbook.validate_org({"name":"leha","phone_number":1234456,"email":"kroro@email@gmail.com"}))
# # addbook.add_record(addbook.__class__.__name__,{"type": f"{addbook.__class__.__name__}", "name":"leha","phone_number":1234456,"email":"kroro@email@gmail.com"})
# print(addbook.get_records("all"))
# print(addbook.find_record(addbook.__class__.__name__,"leha"))

# address_book = AddressBook('address_book.csv')
# a33 = Record.from_csv('address_book.csv')
# print(a33)
# a44 = Person.from_csv('address_book.csv')
# print(a44)
# a55 = Organization.from_csv('address_book.csv')
# print(a55)

# a66 = AddressBook('address_book.csv')
# # print(a66.validate_person({'type': 'AddressBook', 'name': 'leha', 'phone_number': '1234456', 'email': 'ii@aa.com'}))
# # a66.add_record(Organization.__name__,{'name': 'leha', 'phone_number': '1234456', 'email': 'ii@aa.com'})


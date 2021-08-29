bloodtypes = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
donorlist = []
recipientlist = []
adminlist = []

class BloodBank:
    bloodtypes = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

    def __init__(self, name, listhospital = None):
        self.name = name
        if listhospital == None:
            self.listhospital = []
        else:
            self.listhospital = listhospital
    
    def addHospital(self, hospname):
        hosp1 = Hospital.createhosp(hospname)
        self.listhospital.append(Hospital.createhosp(hospname))
        return hosp1

class Hospital:
    def __init__(self, name, donors = None, storage = None):
        self.name = name
        if donors == None:
            self.donors = []
        else:
            self.donors = donors
        self.storage = storage
    
    @classmethod
    def createhosp(cls, name):
        btdict = {i : 1 for i in bloodtypes}
        return Hospital(name, None, btdict)
    
    def addDonor(self, donor):
        self.donors.append(donor)

    def donatehosp(self, bloodtype, amount):
        self.storage[bloodtype] += amount
    
    def checkbloodhosp(self, bloodtype, amount):
        if self.storage[bloodtype] >= amount:
            return self
    
    def checkbloodbank(self, bloodtype, amount, bank):
        hospavail = []
        for i in bank.listhospital:
            if i.storage[bloodtype] >= amount:
                hospavail.append(i)
        return hospavail

    def storagedisp(self, bank):
        for i in range(len(bank.listhospital)):
            if self.name == bank.listhospital[i].name:
                idx = i
        print(f"Name: {bank.listhospital[idx].name}")
        print("Donors: ")
        for i in bank.listhospital[idx].donors:
            print(f"Name: {i.name} \t BloodType: {i.btype}")
        bloodavail = bank.listhospital[idx].storage
        for key, value in bloodavail.items():
            print(f"{key} -> {value}")

class Admin:

    def __init__(self, name):
        self.name = name

    @classmethod
    def createadmin(cls):
        name = input("Enter your name: ")
        return Admin(name)

    def hospstorage(self, hospname, bank):
        for i in range(len(bank.listhospital)):
            if hospname == bank.listhospital[i].name:
                idx = i
        print(f"Name: {bank.listhospital[idx].name}")
        print("Donors: ")
        for i in bank.listhospital[idx].donors:
            print(f"Name: {i.name} \t BloodType: {i.btype}")
        bloodavail = bank.listhospital[idx].storage
        for key, value in bloodavail.items():
            print(f"{key} -> {value}")       

    def bldbankstorage(self, bank):
        print(f"Blood Bank: {bank.name}")
        for i in bank.listhospital:
            print(150*"=")
            i.storagedisp(bank)
        print(150*"=")

    def donorinfo(self, donorname, donorlist):
        for i in range(len(donorlist)):
            if donorname == donorlist[i].name:
                idx = i
                break
        else:
            print("Donor Not Found")
            return
        donorlist[idx].donordetails()

    def recipientinfo(self, recname, recipientlist):
        for i in range(len(recipientlist)):
            if recname == recipientlist[i].name:
                idx = i
                break
        else:
            print("Recipient Not Found")
            return
        recipientlist[idx].recipientdetails()
        
    def requestbt(self, bloodtype, hospname):
        pass

    def getbloodtype(self, bloodtype, bank):
        print(f"Information on: {bloodtype}")
        for i in bank.listhospital:
            print(f"{i.name} -> {i.storage[bloodtype]}")

class Donor:

    def __init__(self, name, age, gender, btype, hosp):
        self.name = name
        self.age = age
        self.btype = btype
        self.gender = gender
        self.hosp = hosp
        hosp.addDonor(self)
        donorlist.append(self)
    
    @classmethod
    def createdonor(cls, bank):
        print(150*"=")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = input("Enter your gender: ")
        print(100*"/")
        for i in range(len(bloodtypes)):
            print(f"Enter {i} for {bloodtypes[i]}")
        print(100*"/")
        btype = bloodtypes[int(input("Enter the option: "))]
        print(100*"/")
        for i in range(len(bank.listhospital)):
            print(f"Enter {i} for {bank.listhospital[i].name}")
        print(100*"/")
        hospname = bank.listhospital[int(input("Enter the option: "))]
        return Donor(name, age, gender, btype, hospname)

    def donate(self, amount):
        self.hosp.donatehosp(self.btype, amount)
    
    def donordetails(self):
        print(150*"=")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"BloodType: {self.btype}")
        print(f"Hospital: {self.hosp.name}")

class Recipient:
    
    def __init__(self, name, age, gender, btype, hospname):
        self.name = name
        self.age = age
        self.btype = btype
        self.gender = gender
        self.hospname = hospname
        recipientlist.append(self)
    
    @classmethod
    def createRecipient(cls, bank):
        print(150*"=")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = input("Enter your gender: ")
        print(100*"/")
        for i in range(len(bloodtypes)):
            print(f"Enter {i} for {bloodtypes[i]}")
        print(100*"/")
        btype = bloodtypes[int(input("Enter the option: "))]
        print(100*"/")
        for i in range(len(bank.listhospital)):
            print(f"Enter {i} for {bank.listhospital[i].name}")
        print(100*"/")
        hospname = bank.listhospital[int(input("Enter the option: "))]
        return Recipient(name, age, gender, btype, hospname)
    
    def recipientdetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"BloodType: {self.btype}")
        print(f"Hospital: {self.hospname.name}")

    def takebloodhosp(self, amount):
        self.hospname.storage[self.btype] -= amount
    
    def takebloodbank(self, amount, hospname, bank):
        for i in range(len(bank.listhospital)):
            if hospname == bank.listhospital[i].name:
                idx = i
        i.storage[self.btype] -= amount

bank = BloodBank("OOP Bloodbank")
bank.addHospital("HospitalDefault")
choice1 = True
while choice1:
    choice1 = int(input("Enter choice\n1. Admin\n2. Donor\n3. Recipient\n0. To exit the Program"))
    if choice1 == 0:
        print("You have exited the program")
        break
    elif choice1 == 1:
        admin1 = Admin.createadmin()
        adminlist.append(admin1)
        while True:
            print("What would you like to do as an admin:\n0.Exit Admin\n1. Check Bank Details\n2. Check Hospital Storage\n3. Donor Details\n4. Recipient Details\n5. Get blood type specific Information\n6. Add Hospital\n7. Rare Blood Group Details\n Enter")
            choice2 = int(input("Enter the choice: "))
            if choice2 == 0:
                break
            elif choice2 == 1:
                admin1.bldbankstorage(bank)
            elif choice2 == 2:
                hname = input("Enter the hospital name you would like the information of: ")
                admin1.hospstorage(hname, bank)
            elif choice2 == 3:
                dname = input("Enter the donorname which you would like information of: ")
                admin1.donorinfo(dname, donorlist)
            elif choice2 == 4:
                rname = input("Enter the name of the recipient you would like information for: ")
                admin1.recipientinfo(rname, recipientlist)
            elif choice2 == 5:
                for i in range(len(bloodtypes)):
                    print(f"Enter {i} for {bloodtypes[i]}")
                btype = bloodtypes[int(input("Enter the option: "))]
                admin1.getbloodtype(btype, bank)
            elif choice2 == 6:
                haddname = input("Enter the hospital name which you want to add: ")
                bank.addHospital(haddname)
            elif choice2 == 7:
                admin1.getbloodtype("AB-", bank)
                admin1.getbloodtype("O-", bank)
                admin1.getbloodtype("AB+", bank)
            else:
                print("Enter an appropriate number")
                continue
    elif choice1 == 2:
        donor1 = Donor.createdonor(bank)
        quant = int(input("How much blood would you like to donate: "))
        donor1.donate(quant)
    elif choice1 == 3:
        recipient1 = Recipient.createRecipient(bank)
        quant = int(input("Enter the amount of blood you require: "))
        avail = recipient1.hospname.checkbloodhosp(recipient1.btype, quant)
        if avail == None:
            avail = recipient1.hospname.checkbloodbank(recipient1.btype, quant, bank)
            print(avail)
            if avail == []:
                print("Sorry we have no bloodbags available at any of the hospitals")
            else:
                print(f"Availibility of {recipient1.btype} in other hospitals is: ")
                count = 0
                for i in avail:
                    print(f"{count}. {i.name} -> {i.storage[recipient1.btype]}")
                    count += 1
                print("Which hospital would you like (Enter the index of the hospital) : ")
                recipient1.takebloodbank(quant, avail[count], bank)
        else:
            ask = int(input(f"Would you like {quant} bloodbags from Hospital: {recipient1.hospname.name}\n1. Yes\n2. No"))
            if ask == 1:
                print(f"You have recieved {quant} bloodbags, Thank you")
                recipient1.takebloodhosp(quant)
            else:
                print("Thank you")
    else:
        print("Enter an appropriate number")
        continue

















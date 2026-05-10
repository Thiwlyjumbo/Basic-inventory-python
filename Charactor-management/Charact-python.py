import json, os
class Mercenary:
    def __init__(self, name, rank, salary):
        self.name = name
        self.rank = rank
        self.salary = salary
    def show_info(self):
        print("show info".center(25, '-'))
        print(f"name : {self.name}")
        print(f"rank : {self.rank}")
        print(f"salary : {self.salary}")
        print("end".center(25, "-"))
    def promote(self):
        self.salary += (self.salary / 2)
        rank = ['E', 'D', 'C', 'B', 'A', 'S']
        if rank.index(self.rank) >= 4:
            self.rank = "S"
        else: self.rank = rank[(rank.index(self.rank)) + 1]
        return {'class':'Mercenary', 'name':self.name, 'rank':self.rank, 'salary':self.salary}

class Sniper(Mercenary):
    def __init__(self, name, rank, salary, distance):
        super().__init__(name, rank, salary)
        self.distance = distance
    def show_info(self):
        print("show info".center(25, '-'))
        print(f"name : {self.name}")
        print(f"rank : {self.rank}")
        print(f"salary : {self.salary}")
        print(f"distancce : {self.distance} km.")
        print("end".center(25, "-"))
    def promote(self):
        self.salary += (self.salary / 2)
        self.distance += (self.distance / 2)
        rank = ['E', 'D', 'C', 'B', 'A', 'S']
        if rank.index(self.rank) >= 4:
            self.rank = "S"
        else: self.rank = rank[(rank.index(self.rank)) + 1]
        return {'class':'Sniper', 'name':self.name, 'rank':self.rank, 'salary':self.salary, "distance":self.distance}
    
class Medic(Mercenary):
    def __init__(self, name, rank, salary, medicine):
        super().__init__(name, rank, salary)
        self.medicine = medicine
    def show_info(self):
        print("show info".center(25, '-'))
        print(f"name : {self.name}")
        print(f"rank : {self.rank}")
        print(f"salary : {self.salary}")
        print(f"medicine : {self.medicine} box.")
        print("end".center(25, "-"))
    def promote(self):
        self.salary += (self.salary / 2)
        self.medicine += 3
        rank = ['E', 'D', 'C', 'B', 'A', 'S']
        if rank.index(self.rank) >= 4:
            self.rank = "S"
        else: self.rank = rank[(rank.index(self.rank)) + 1]
        return {'class':'Medic', 'name':self.name, 'rank':self.rank, 'salary':self.salary, "medicine":self.medicine}

def Inventory():
    def load():
        if os.path.exists("inventory.json"):
            try: 
                with open("Charactor.json", 'r') as r:
                    return json.load(r)
            except: return []
        else: return []
    mercenary = load()
    def save(data):
        with open("Charactor.json", "w") as w:
            json.dump(data, w)
    def add():
        class_all = ['mc', 'sn', 'md']
        clas = input("Class : ").lower()
        if clas in class_all:
            name = input("Name : ")
            rank = input('Rank : ').upper()
            salary = input("Salary : ")
            try:
                salary = float(salary)
                match clas:
                    case "mc": 
                        mc = {'class':'Mercenary', 'name':name, 'rank':rank, 'salary':salary}
                        mercenary.append(mc)
                    case "sn": 
                        distance = input("Distance of sniper : ")
                        try:
                            distance = float(distance)
                            sn = {'class':'Sniper', 'name':name, 'rank':rank, 
                              'salary':salary, 'distance':distance}
                            mercenary.append(sn)
                        except: print("can'n add please try agian..")
                    case "md": 
                        medicine = input("Medicine of medic : ")
                        try:
                            medicine = int(medicine)
                            md = {'class':'Medic', 'name':name, 'rank':rank, 
                              'salary':salary, 'medicine':medicine}
                            mercenary.append(md)
                        except: print("can'n add please try agian..")
                save(mercenary)
            except ValueError: print("can'n add please try agian..")
        else: print(f"<{clas}> this class can't added..")
    def show():
        def show_i(i):
            match i["class"]:
                case "Mercenary":
                    mc = Mercenary(i['name'], i['rank'], i['salary'])
                    mc.show_info()
                case "Sniper":
                    sn = Sniper(i['name'], i['rank'], i['salary'], i['distance'])
                    sn.show_info()
                case "Medic":
                    md = Medic(i['name'], i['rank'], i['salary'], i['medicine'])
                    md.show_info()
        if mercenary:
            name_all = []
            for i in mercenary:
                print("".center(25, "="))
                print(f"{i['name']} - class {i['class']}")
                name_all.append(i['name'].lower())
                print("".center(25, "="))
            print('type <name> to show_info or type <all> to show_all...')
            m = list(map(str, input().lower().split()))
            if "all" in m:
                for i in mercenary:
                    show_i(i)
            elif any(x in name_all for x in m):
                for i in mercenary:
                    if i['name'].lower() in m:
                        show_i(i)
            else: print("data not found..")
        else: print("not data please add..")
    def remove():
        #verify mercenary
        if mercenary:
            #show mercenary-all
            name_all = []
            for i in mercenary:
                print("".center(25, "="))
                print(f"{i['name']} - class {i['class']}")
                name_all.append(i['name'].lower())
                print("".center(25, "="))
            print('type <name> to show_info or type <all> to show_all...')
            m = list(map(str, input().lower().split()))
            if "all" in m:
                confirm = input('remove all data (y/n)')
                if confirm in ['y', 'n']:
                    match confirm:
                        case 'y':
                            print("remove-all...")
                            mercenary.clear()
                            save(mercenary)
                        case 'n': print("don't remove..")
                else: print("not command")
            elif any(x in name_all for x in m):
                confirm = input('confirm to remove selected name(s)? (y/n)')
                if confirm in ['y', 'n']:
                    new_data = []
                    match confirm:
                        case 'y':
                            for i in mercenary:
                                if i['name'].lower() not in m:
                                    new_data.append(i)
                            mercenary[:] = new_data
                            save(mercenary)
                        case 'n': print("don't remove..")
                else: print("not command")
            else: print("data not found..")
        else: print("not data please add..")
    
    def promote():
        # verify mercenary-all
        if mercenary:
            #show mercenary-all
            name_all = []
            for i in mercenary:
                print("".center(25, "="))
                print(f"{i['name']} - class {i['class']}")
                name_all.append(i['name'].lower())
                print("".center(25, "="))
            print('type <name> to promote(name) or type <all> to promote-all...')
            # input
            m = list(map(str, input().lower().split()))
            # promote-all
            if "all" in m:
                confirm = input('promote all ? (y/n)')
                if confirm in ['y', 'n']:
                    match confirm:
                        case 'y':
                            new_data = []
                            for i in mercenary:
                                match i["class"]:
                                    case "Mercenary":
                                        mc = Mercenary(i['name'], i['rank'], i['salary'])
                                        new_data.append(mc.promote())
                                    case "Sniper":
                                        sn = Sniper(i['name'], i['rank'], i['salary'], i['distance'])
                                        new_data.append(sn.promote())
                                    case "Medic":
                                        md = Medic(i['name'], i['rank'], i['salary'], i['medicine'])
                                        new_data.append(md.promote())
                            mercenary[:] = new_data
                            save(mercenary)
                            print("promote-all...")
                        case 'n': print("don't promote..")
                else: print("not command")
            # promote-some-name
            elif any(x in name_all for x in m):
                confirm = input('confirm to promote selected name(s)? (y/n)')
                if confirm in ['y', 'n']:
                    match confirm:
                        case 'y':
                            new_data = []
                            for i in mercenary:
                                if i['name'].lower() in m:
                                    match i["class"]:
                                        case "Mercenary":
                                            mc = Mercenary(i['name'], i['rank'], i['salary'])
                                            new_data.append(mc.promote())
                                        case "Sniper":
                                            sn = Sniper(i['name'], i['rank'], i['salary'], i['distance'])
                                            new_data.append(sn.promote())
                                        case "Medic":
                                            md = Medic(i['name'], i['rank'], i['salary'], i['medicine'])
                                            new_data.append(md.promote())
                                else: new_data.append(i)
                            mercenary[:] = new_data
                            save(mercenary)
                        case 'n': print("don't promote..")
                else: print("not command")
            else: print("data not found..")
        else: print("not data please add..")
    exit = False
    while not exit:
        mode = ['add', 'show', 'remove', 'promote', 'exit']
        m = input('Mode : ').lower()
        if m in mode:
            match m:
                case "add": add()
                case "show": show()
                case "remove": remove()
                case "promote": promote()
                case "exit": exit = True
        else: print("not command..")
Inventory()

class Mercenary:
    def __init__(self, name, rank, salary):
        # Initialize basic mercenary attributes
        self.name = name
        self.rank = rank
        self.salary = salary
        self.weapon = None # Store Weapon object if equipped
    def show_info(self): 
        # Display general mercenary information
        print("show info".center(25, '-'))
        print(f"name : {self.name}")
        print(f"rank : {self.rank}")
        print(f"salary : {self.salary}")
        if self.weapon: print(f"weapon : {self.weapon.name} (DMG: {self.weapon.damage})")
        else: print('weapon none')
        print("end".center(25, "-"))
    def promote(self):
        # Calculate new salary and upgrade rank
        self.salary += (self.salary / 2)
        rank = ['E', 'D', 'C', 'B', 'A', 'S']
        # Upgrade to next rank, maxing out at 'S'
        if rank.index(self.rank) >= 4:
            self.rank = "S"
        else: self.rank = rank[(rank.index(self.rank)) + 1]
        # Prepare dictionary data for saving
        data =  {'class':'Mercenary', 'name':self.name, 'rank':self.rank, 'salary':self.salary}
        # Add weapon data to dictionary if it exists
        if self.weapon:
            data['weapon'] = self.weapon.to_dict()
        else: data['weapon'] = None
        return data

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
        if self.weapon: print(f"weapon : {self.weapon.name} (DMG: {self.weapon.damage})")
        else: print('weapon none')
        print("end".center(25, "-"))
    def promote(self):
        # Call parent promote logic and add sniper-specific upgrades
        data = super().promote()
        data["distance"] = self.distance + (self.distance / 2)
        data["class"] = 'Sniper'
        return data
    
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
        if self.weapon: print(f"weapon : {self.weapon.name} (DMG: {self.weapon.damage})")
        else: print('weapon none')
        print("end".center(25, "-"))
    def promote(self):
        # Call parent promote logic and add medic-specific upgrades
        data = super().promote()
        data["medicine"] = self.medicine + 3
        data["class"] = 'Medic'
        return data
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    def to_dict(self):
        return {'name':self.name, 'damage':self.damage}

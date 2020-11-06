#simple example oop and using of dictionaries
class Tank(object):
    def __init__(self,name):
        self.name = name
        self.ammo = 5
        self.armor = 60
    def __str__(self):
        if self.alive:
            return "%s(%i armor,%i shells)"
        else:
            return "%s(DEAD) "#%s means string

    def fire_at(self,enemy):
        if self.ammo >=1:
            self.ammo -=1
            print(self.name,"fires on",enemy.name)
        else:
            print(self.name,"has no shells!")
    def hit(self):
        self.armor -=20
        print(self.name,"is hit")
        if self.armor <= 0:
            self.explode()
    def explode(self):
        self.alive = False
        print(self.name,"explodes!")
def start():
    print("Who Does fires on ?")
    name_of_victim=input("Enter a name:")
    if name_of_victim == "Alice":
        firs_tank.explode()
    else:
        pass



tanks ={"a":Tank("Alice") ,"b":Tank("Bob"),"c":Tank("Carol")}
alive_tanks = len(tanks) #length of tanks
firs_tank=tanks["a"]
while alive_tanks >1:
    start()






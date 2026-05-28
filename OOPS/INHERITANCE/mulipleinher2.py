class TeamMember:
    def __init__(self,name,uid):
        self.name=name
        self.uid=uid
    def display(self):
        print(f"TeamMember:{self.name},UID:{self.uid}")
class Worker:
    def __init__(self,pay,jobtitle):
        self.pay=pay
        self.jobtitle=jobtitle
    def display(self):
        print(f"Worker:{self.jobtitle},Pay:{self.pay}")
        

class TeamLeader(TeamMember,Worker):
    def __init__(self, name, uid,pay,jobtitile,exp):
        self.exp=exp
        TeamMember.__init__(self,name,uid)
        Worker.__init__(self,pay,jobtitile)
    
    def display(self):
        TeamMember.display(self)
        Worker.display(self)
        print(f"Experience:{self.exp}")
        
TL=TeamLeader('Ram',10001,50000,'Scrum Master',5)
TL.display()
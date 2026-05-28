class Worker:

    def __init__(self, pay, jobtitle):

        self.pay = pay
        self.jobtitle = jobtitle


class TeamMember:

    def __init__(self, name, uid):

        self.name = name
        self.uid = uid


class TeamLeader(Worker, TeamMember):

    def __init__(self, name, uid, pay, jobtitle, exp):

        self.exp = exp

        TeamMember.__init__(self, name, uid)

        Worker.__init__(self, pay, jobtitle)

        print("Name : {} , Pay : {} , Exp : {}".format(
            self.name,
            self.pay,
            self.exp
        ))


TL = TeamLeader('jake', 10001, 250000, "s master", 5)

print(TeamLeader.mro())
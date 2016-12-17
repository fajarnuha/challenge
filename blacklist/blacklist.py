
class Blacklist:
    def __init__(self, text):
        f = open(text)
        self.data = f.read().splitlines()

    def check_blacklist(self, name, phone_number):
        search = name + " " + str(phone_number)
        print search in self.data

query = Blacklist('blist.txt')
query.check_blacklist('npmceb', 355146)

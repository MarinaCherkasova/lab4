class person():
    def wish(self):
        print('Человек захотел отправить (напишите кого) ')
        who = input()
        return who
    def place(self, who):
        print('Отправим на отдых ', who, ' в (напишите любую страну) ')
        where = input()
        return where
class booking_tickets():
    def request(self, who, where):
        print('Куплю билет для ', who, ' в ', where)
    def result(self):
        print('Ура отдых!')

a = person()
c = booking_tickets()
who = person.wish(a)
where = person.place(a, who)
when = person.time(a, who, where)
booking_tickets.request(c, who, where)
booking_tickets.result(c)

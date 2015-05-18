import collections

Point = collections.namedtuple('Point', ['x', 'y'])

class Student(object):
    def __init__(self, imie, nazwisko, ident):
        self.imie = imie 
        self.nazwisko = nazwisko
        self.ident = ident

    def __str__(self):
        return "Imie %s, Nazwisko %s" % (self.imie, self.nazwisko)

    def swap_names(self):
        self.imie, self.nazwisko = self.nazwisko, self.imie


if __name__ == "__main__":
    d = {}
    d['imie'] = 'Jeff'
    d['nazwisko'] = 'Bridges'
    d['ident'] = 0
    s = Student('Bartek', 'Antosik', 152814)
    dude = Student(**d)
    print s, dude
    s.swap_names()
    p = Point(4,5)
    t = (6, 4)
    o = Point(*t)
    print p
    if p.x < p.y:
        print "Druga wspolrzedna wieksza"
    print s

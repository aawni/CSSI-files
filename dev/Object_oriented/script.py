class Ninja(object):
    def __init__(self, name, level):
        self.name=name
        self.level=level
        self.outfit='black'
        self.rating=0

    def fight(self, other):
        if self.level > other.level:
            self.rating=self.rating+1
            other.rating=other.rating-1
            print "I win!!!!!!!!!! Wow I'm so great at this"
        elif self.level < other.level:
            self.rating=self.rating-1
            other.rating=other.rating+1
            print "I lose"
        else:
            print "We draw"

    def promote(self, other):
        if self.level>other.level:
            other.level=other.level+1

    def describe(self):
        return "I am Ninja " + self.name + " level " + str(self.level) + " and I wear " + self.outfit

        

class Monster(object):
    def __init__(self, name, has_teeth, breathes_fire):
        self.name=name
        self.has_teeth=has_teeth
        self.breathes_fire=breathes_fire


    def scare(self):
        if self.has_teeth:
            print "I'm going to eat you!!"
        elif self.breathes_fire:
            print " I'm going to roast you like a marshmellow"
        else:
            print "I'm going to tickle you"

    def fight(self, other):
        if self.breathes_fire and not other.breathes_fire:
            print self.name + " wins by fire!"
        elif self.breathes_fire and other.breathes_fire:
            print "Uh oh they melted each other"
        elif not self.breathes_fire and other.breathes_fire:
            print other.name + " wins by fire!"
        elif self.has_teeth and not other.has_teeth:
            print self.name + "won by biting " + other.name + "!"
        elif not self.has_teeth and other.has_teeth:
            print other.name + "won by biting " + self.name + "!"
        else:
            print "Oh no they torn each other to pieces!"

    def talk_to_ninja(self, other_ninja):
        print "hello ninja, I am " + self.name + ", who are you?  " + other_ninja.describe()


awesome_ninja=Ninja('Alia', 100)
strong_monster = Monster("Scary", True, True)
weak_monster=Monster("Kitten", False, False)

strong_monster.talk_to_ninja(awesome_ninja)
# crappy_ninja=Ninja('Manuel', -1)
# sensei=Ninja("Uh oh", 100000)
# awesome_ninja.fight(crappy_ninja)
# awesome_ninja.fight(crappy_ninja)
# awesome_ninja.fight(crappy_ninja)
# awesome_ninja.fight(crappy_ninja)
# awesome_ninja.fight(crappy_ninja)
# awesome_ninja.fight(crappy_ninja)
# awesome_ninja.fight(sensei)
# print awesome_ninja.rating
# print crappy_ninja.rating
# print sensei.rating

class Parent(object):        # define parent class
    parentAttr = 100
    def __init__(self):
        print "Calling parent constructor"

    def parentMethod(self):
        print 'Calling parent method'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "Parent attribute :", Parent.parentAttr

class Parent2(object):
    def parentMethod(self):
        print 'Calling parent method2'

class Child(Parent2, Parent): # define child class -- the inhertance matters!!!
    def __init__(self):
        print "Calling child constructor"

    def childMethod(self):
        print 'Calling child method'

    # def parentMethod(self):
    #     print "Override parent's method"

if __name__ == '__main__':
    c = Child()          # instance of child
    c.childMethod()      # child calls its method
    c.parentMethod()     # calls parent's method
    c.setAttr(200)       # again call parent's method
    c.getAttr()          # again call parent's method

    c.parentMethod()     # since Parent2 class comes first then Parent class, the child will inherit Parent2's parent method
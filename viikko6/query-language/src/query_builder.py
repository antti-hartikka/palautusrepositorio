from matchers import *

class QueryBuilder:
    def __init__(self, *args):
        if args:
            self._builder = args[0]
        else:
            self._builder = All()

    def playsIn(self, team):
        return self._stackify(PlaysIn(team))

    def hasAtLeast(self, value, attr):
        return self._stackify(HasAtLeast(value, attr))

    def hasFewerThan(self, value, attr):
        return self._stackify(HasFewerThan(value, attr))

    def oneOf(self, matcher1, matcher2):
        return QueryBuilder(Or(matcher1, matcher2))

    def _stackify(self, new_object):
        return QueryBuilder(And(self._builder, new_object))

    def build(self):
        return self._builder
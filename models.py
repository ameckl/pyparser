class Element(object):
    def __init__(self, name, terminal, augmented=False, isDot=False):
        self.name = name
        self.terminal = terminal
        self.augmented = augmented
        self.isDot = isDot

    def __str__(self):
        return '{}'.format(self.name)

    def __cmp__(self, other):
        if (self.name == other.name and self.terminal == other.terminal and self.augmented == other.augmented and
        self.isDot == other.isDot):
            return 0
        return -1


class Production(object):
    def __init__(self, rhs, lhs):
        self.rhs = rhs
        self.lhs = lhs

    def __str__(self):
        rhsmsg = ''
        for r in self.rhs:
            rhsmsg += str(r) + ' '
        return str(self.lhs) + ' --> ' + rhsmsg

    def __cmp__(self, other):
        if self.lhs != other.lhs:
            return -1
        elif len(self.rhs) != len(other.rhs):
            return -1
        else:
            for idx, val in enumerate(self.rhs):
                if val != other.rhs[idx]:
                    return -1
            return 0


class ProductionContainer(object):
    def __init__(self):
        self.productions = []

    def get_augmented(self):
        return [prod for prod in self.productions if prod.lhs.augmented]

    def add(self, production):
        if production not in self.productions:
            self.productions.append(production)


class Grammar(object):
    def __init__(self, starting_symbol, productions, elements):
        self.elements = elements
        self.productions = ProductionContainer()
        self.productions.productions = productions
        self.starting_symbol = starting_symbol
        self.augmented_starting = Element(name="S'", terminal=False, augmented=True)
        augmented_prod = Production(lhs=self.augmented_starting, rhs=[self.starting_symbol])
        self.productions.add(production=augmented_prod)

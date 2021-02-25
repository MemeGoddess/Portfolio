def Where(self, expression):
    return filter(expression, self)


def Select(self, expression):
    return map(expression, self)
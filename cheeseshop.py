
def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, '?'
    print "-- I'm sorry, we're all out of ", kind
    for arg in arguments: print arg
    print '-'*40
    keys = keywords.keys()
    keys.sort()
    for kw in keys: print kw, ':', keywords[kw]

cheeseshop('BlueCheese', "It's very smell, sir.",
           "It's really very, VERY smell, sir",
           client='John',
           shopkeeper='Michael',
           date='2016/5/13',
           place='Cheese shop')


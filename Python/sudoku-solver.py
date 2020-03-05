def cross(A, B):
    return [a+b for a in A for b in B] #Cross product of A and B

digits = '123456789'
rows = 'ABCDEFGHI'
columns = digits
squares = cross(rows, columns)
ulist = ([cross(rows, c) for c in columns]+ [cross(r, columns) for r in rows] + [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((i, [u for u in ulist if i in u]) for i in squares)
peers = dict((i, set(sum(units[i],[]))-set([i])) for i in squares)

def parse_grid(grid):
    value = dict((i, digits) for i in squares)
    for i,j in grid_values(grid).items():
        if j in digits and not assign(value, i, j):
            return False 
    return value

def grid_values(grid):
    chars = [i for i in grid if i in digits or i in '0.']
    assert len(chars) == 81
    return dict(zip(squares,chars))

def assign(value, s, d):
    other_values = value[s].replace(d,'')
    if all(eliminate(value, s, d2) for d2 in other_values):
        return value
    else:
        return False
def eliminate(value, s, d):
    if d not in value[s]:
        return value
    value[s] = value[s].replace(d,'')
    if len(value[s]) == 0:
        return False
    elif len(value[s]) == 1:
        d2 = value[s]
        if not all(eliminate(value, s2, d2) for s2 in peers[s]):
            return False

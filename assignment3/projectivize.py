# Projectivize trees in the CoNLL-X format using lifting
# Usage: python projectivize.py < CONLL > CONLL

# Bonus: Count the number of projective trees

def trees(fp):
    buffer = []
    for line in fp:
        line = line.rstrip() # strip off the trailing newline
        if not line.startswith('#'):
            if len(line) == 0:
                yield buffer
                buffer = []
            else:
                columns = line.split()
                if columns[0].isdigit(): # skip range tokens
                    buffer.append(columns)

def heads(rows):
    return [0] + [int(row[6]) for row in rows]

DN = +1
SH = 0
UP = -1

def traverse(heads):
    marked = [False] * len(heads)
    cursor = 0
    marked[cursor] = True
    for i in range(len(heads)):
        bend = i
        path = []
        while not marked[bend]:
            path.append(bend)
            bend = heads[bend]
        while cursor != bend:
            yield cursor, UP
            marked[cursor] = False
            cursor = heads[cursor]
        while len(path) > 0:
            cursor = path.pop()
            marked[cursor] = True
            yield cursor, DN
        yield cursor, SH
        assert cursor == i
    while cursor != 0:
        yield cursor, UP
        marked[cursor] = False
        cursor = heads[cursor]

def is_projective(heads):
    seen = [False] * len(heads)
    for cursor, d in traverse(heads):
        if d == DN:
            if seen[cursor]:
                return False
            else:
                seen[cursor] = True
    return True

def projectivize(heads):
    pheads = [0] * len(heads)
    dangling = [[] for _ in heads]
    head_blk = [False] * len(heads)
    for cursor, d in traverse(heads):
        if d == UP:
            if head_blk[heads[cursor]]:
                for node in dangling[cursor]:
                    pheads[node] = heads[cursor]
            else:
                dangling[heads[cursor]] += dangling[cursor]
            dangling[cursor] = []
            head_blk[cursor] = False
        if d == SH:
            head_blk[cursor] = True
            for node in dangling[cursor]:
                pheads[node] = cursor
            dangling[cursor] = [cursor]
    return pheads

def projectivized_trees(fp):
    for tree in trees(fp):
        pheads = projectivize(heads(tree))
        for i, row in enumerate(tree):
            row[6] = "%d" % pheads[i+1]
        yield tree

def emit(tree):
    for row in tree:
        print("\t".join(row))
    print()

def cmd_count_projective():
    import sys
    k = 0
    n = 0
    for tree in trees(sys.stdin):
        k += is_projective(heads(tree))
        n += 1
    print("{:.2%}".format(k / n))
    
def cmd_projectivize():
    import sys
    for ptree in projectivized_trees(sys.stdin):
        emit(ptree)

if __name__ == "__main__":
    #cmd_count_projective()
    cmd_projectivize()

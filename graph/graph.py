#trannsitive Closure pg 49

g = {}
v = {'a':False,'b':False,'c':False,'d':False,'e':False}

def DFS(s,e):
    v[s] = True

    if(s == e):
        return True

    for i in g[s]:
        a = v[i]
        if not v[i]:
            return DFS(i,e)

    return False

def TransitiveClosure():
    for i in g.keys():
        for j in g.keys():
            if i != j:
                if j not in g[i]:
                    if DFS(i,j):
                        g[i].append(j)
                    visit_reset()


def visit_reset():
    for key in g.keys():
        v[key] = False

if __name__ == "__main__":
    g['a'] = ['c']
    g['c'] = ['d']
    g['b'] = ['d','c']
    g['d'] = ['e']
    g['e'] = []

    # for i in g['c']:
    #     print(i)
    print(v)
    TransitiveClosure()
    print(g)






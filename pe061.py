CHECKLIST = {}


def get_polys(sides, lower, upper):
    res = []
    num = 0
    i = 0
    while num + (sides - 2) * i + 1 < upper:
        num += (sides - 2) * i + 1
        i += 1
        if num >= lower:
            res.append(num)
    for poly in res:
        if CHECKLIST.get(poly) is None:
            CHECKLIST[poly] = (sides,)
        else:
            CHECKLIST[poly] += (sides,)
    return res
        


polys3 = get_polys(3, 1000, 10000)
polys4 = get_polys(4, 1000, 10000)
polys5 = get_polys(5, 1000, 10000)
polys6 = get_polys(6, 1000, 10000)
polys7 = get_polys(7, 1000, 10000)
polys8 = get_polys(8, 1000, 10000)

polys = set(polys3 + polys4 + polys5 + polys6 + polys7 + polys8)

for poly in list(polys):
    if str(poly)[2] == '0':
        polys.remove(poly)


def check(res, types=[], i=0):
    for poly_type in CHECKLIST[res[i]]:
        if poly_type in types:
            continue
        if i == 5:
            print(sum(res))
            return
        check(res, types + [poly_type], i + 1)
    return


def find(res=[]):
    for poly in polys:
        if res == []:
            find([poly])
        else:
            if poly not in res and str(poly)[:2] == str(res[-1])[2:]:
                if len(res) != 5:
                    find(res + [poly])
                elif str(res[0])[:2] == str(poly)[2:]:
                    check(res + [poly])
                    

find()
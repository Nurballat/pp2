def solve(heads, legs):
    chik = (legs - 2 * heads) / 2
    rab = heads - chik
    print(chik)
    print(rab)

h = int(input("Heads:"))
l = int(input("Legs:"))
solve(h, l)

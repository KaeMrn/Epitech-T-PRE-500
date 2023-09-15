def inf_pi(its, ctr = 1):
    if its == 0:
        return 0
    else:
        x = ((2*ctr)-1)**2 / (6 + inf_pi(its - 1, ctr + 1))
        return  x + (3 if ctr == 1 else 0)

print(inf_pi(10))
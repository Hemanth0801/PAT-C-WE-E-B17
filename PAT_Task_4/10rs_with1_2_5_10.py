# total 10rs ,  possible ways with 1rs,2rs,5rs,10rs


for a in range(0, 11): #1rs  #for loop is udes to try evry possible numb of coins
    for b in range(0, 6):  #2rs
        for c in range(0, 3): #5rs
            for d in range(0, 2): #10rs
                total = a*1 + b*2 + c*5 + d*10
                if total == 10:
                    print("1Rs =", a,
                          "2Rs =", b,
                          "5Rs =", c,
                          "10Rs =", d)

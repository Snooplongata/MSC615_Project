def create_poss(sample):
    whatsLeft = list(range(1,31))
    res = []
    i = 0
    while True:
        if len(res) == 10:
            break
        if not whatsLeft:
            res.append(sample[i])
            i += 1
        else:
            res.append(sample[i])
            for j in sample[i]:
                if j in whatsLeft:
                    whatsLeft.remove(j)

            target = min(whatsLeft)
            indx = list(sampl[:,0]).index(target)
            
            if len(whatsLeft) <= 5:
                hold = sample[:]
                for k,ele in enumerate(whatsLeft):
                    hold = hold[hold[:,k] == ele]
                res.append(hold[0])

            i = indx

    return res
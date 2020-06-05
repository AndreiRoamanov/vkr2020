# ТОЧНОЕ ПОСТРОЕНИЕ ОБОБЩЁННЫХ ПОЛИНОМОВ МИНИМАЛЬНОЙ ДЛИНЫ ДЛЯ ВСЕХ БУЛЕВЫХ ФУНКЦИЙ ОТ N = 4 ПЕРЕМЕННЫХ.
# Для 3 переменных построение аналогичное.

# Программа каждый раз при увеличении длины выдаёт, сколько булевых функций невозможно представить обобщённым полиномом длины, меньше рассматриваемой

while (True):
    n = int(input())
    if n == 4:
        b = []
        sch1 = sch2 = sch3 = sch4 = sch5 = sch6 = 0
        counter = 65534
        pol = []
        znpol = []
        znlen = []
                                             
        for i in range (0, 2 ** (2 ** n)):
            pol.append(0)
            znpol.append(0)
            znlen.append(0)
        for i in range (0, 2 ** n):
            b.append(0)
        tabl = []
        for i in range (0, 2 ** (2 ** n)):
            tabl.append(-1)
        tablzn = []
        for i in range (0, 2 ** (2 ** n)):
            tablzn.append(-1)
        con = []
        res = []
        for j in range (0, 2 ** (2 ** n)):
            res.append(0)
        len = 1
        for j in range (0, 4000000):
            con.append(0)
        con[0] = 3
        z = 1
        for i in range (1, 3 ** n):
            con[z] = (i % 3 + (i // 3) % 3 * 10 + (i // 3) // 3 % 3 * 100 + ((i // 3) // 3) // 3 * 1000)
            z = z + 1
            ff = 0
            pol[0] = 1
            pol[2 ** 2 ** n - 1] = 1
            for k in range (0, 2 ** n):
                x = []
                for l in range (0, n):
                    x.append(-1)
                x[0] = k // 8
                x[1] = int(k // 4 == 1 or k // 4 == 3)
                x[2] = int(k % 4 == 2 or k % 4 == 3)
                x[3] = k % 2
                for l in range (0, len):
                    res[l] = 1
                func = con[z - 1]
                l = 0
                if (func == 0):
                    if b[k] == 0:
                        yes = 1
                        continue
                    else:
                        yes = 0
                        break
                while func > 0:
                    if func % 10 == 1:
                        res[l // n] = res[l // n] * x[l % n]
                    elif func % 10 == 2:
                        res[l // n] = res[l // n] * ((x[l % n] + 1) % 2)
                    l = l + 1
                    func = func // 10
                allres = 0
                for j in range(0, len):
                    allres += res[j]
                allres = allres % 2
                ff = ff + allres * 2 ** (15 - k) 
            if pol[ff] == 0:
                counter = counter - 1
                pol[ff] = 1
                znlen[ff] = len
                znpol[ff] = con[z - 1]
                sch1 = sch1 + 1
        print("len = ", len, " ended with counter = ", counter)
        l1 = z - 1
        con[z] = -1
        j = 0
        h = z
        pol[0] = 1
        znlen[0] = 0
        znpol[0] = 0
        t = 0
        bad = 0
        last = 0
        len = len + 1
        while (counter > 0):
            while con[t] != - 1 and last == 0:
                w = 0
                while con[w] != con[t] % 10000:
                    w = w + 1
                w = w + 1
                while con[w] <= 2222:
                    bad = 0
                    good = 0
                    zn1 = con[w]
                    bufzn1 = zn1
                    zn2 = con[t]
                    while zn2 != 0:
                        err = 0
                        retr = 0
                        dblotr = 0
                        pp = 0
                        otr = 0
                        flg = 0
                        situation1 = 0
                        situation2 = 0
                        situation3 = 0
                        situation4 = 0
                        situation5 = 0
                        situation6 = 0
                        prm = zn2 % 10000
                        while prm != 0 or zn1 != 0:
                            if prm == 3:
                                good = 7
                                break
                            if zn1 % 10 == prm % 10:
                                err = err + 1
                            if (prm % 10 == 0 and zn1 % 10 == 1):
                                retr = retr + 1
                                situation1 = situation1 + 1
                            if (prm % 10 == 1 and zn1 % 10 == 0):
                                retr = retr + 1
                                situation2 = situation2 + 1
                            if (prm % 10 == 0 and zn1 % 10 == 2):
                                retr = retr + 1
                                situation3 = situation3 + 1
                            if (prm % 10 == 2 and zn1 % 10 == 0):
                                retr = retr + 1
                                situation4 = situation4 + 1
                            if (prm % 10 == 1 and zn1 % 10 == 2):
                                retr = retr + 1
                                situation5 = situation5 + 1
                            if (prm % 10 == 2 and zn1 % 10 == 1):
                                retr = retr + 1
                                situation6 = situation6 + 1
                            zn1 = zn1 // 10
                            prm = prm // 10
                            pp = pp + 1
                        if good == 7:
                            good = 7
                        elif err == pp - 2 and situation1 == 2:
                            good = 1
                        elif err == pp - 2 and situation1 == 1 and situation3 == 1:
                            good = 2
                        elif err == pp - 2 and situation1 == 1 and situation2 == 1:
                            good = 3
                        elif err == pp - 2 and situation3 == 2: 
                            good = 4
                        elif err == pp - 2 and situation1 == 1 and situation5 == 1:
                            good = 5
                        elif err == pp - 2 and situation2 == 1 and situation3 == 1:
                            good = 6
                        elif err < pp - 2:
                            good = 8
                        else:
                            good = 0
                            break  
                        zn2 = zn2 // 10000
                        zn1 = bufzn1
                    if good > 0:
                        curfunc = 0
                        if con[t] // (10 ** ((len - 2) * 4)) == 3: # чтобы не было случаев 1 + x1; 1 + !x1 и тд
                            cccon = con[w]
                            zt = 0
                            while cccon > 0:
                                if cccon % 10 == 1 or cccon % 10 == 2:
                                    zt = zt + 1
                                cccon = cccon // 10
                            if zt == 1:
                                w = w + 1
                                continue
                            else:
                                curfunc = con[t] * 10 ** n + con[w]
                        else:
                            curfunc = con[t] * 10 ** n + con[w]
                    else:
                        w = w + 1
                        continue
                    ff = 0
                    for k in range (0, 2 ** n):
                        x = []
                        for l in range (0, n):
                            x.append(-1)
                        x[0] = k // 8
                        x[1] = int(k // 4 == 1 or k // 4 == 3)
                        x[2] = int(k % 4 == 2 or k % 4 == 3)
                        x[3] = k % 2
                        for l in range (0, len):
                            res[l] = 1
                        func = curfunc
                        if (func == 3):
                            if b[k] == 0:
                                yes = 1
                                continue
                            else:
                                yes = 0
                                break
                        l = 0
                        while func > 0:
                            if func % 10 == 1:
                                res[l // n] = res[l // n] * x[l % n]
                            elif func % 10 == 2:
                                res[l // n] = res[l // n] * ((x[l % n] + 1) % 2)
                            l = l + 1
                            func = func // 10
                        allres = 0
                        for s in range(0, len):
                            allres += res[s]
                        allres = allres % 2
                        ff = ff + allres * 2 ** (15 - k)
#                    if pol[ff] != 0:
                        # печать, показывающая, что полином реализует функцию, для которой уже построен полином
#                        print("Functions already were counter = ", counter, "   conh = ", curfunc, "   con[t] = ", con[t], "    con[w] = ", con[w], " t = ", t, " h+j = ", h+j, " ff = ", ff, " znpol[ff] = ", znpol[ff])
                    if pol[ff] == 0:
#                        # печать, показывающая, что полином реализует функцию, для которой ещё не построен полином
#                        print("First function with: counter = ", counter, "   conh = ", curfunc, "   con[t] = ", con[t], "    con[w] = ", con[w], " t = ", t, " h+j = ", h+j, " ff = ", ff)
                        counter = counter - 1
                        pol[ff] = 1
                        znpol[ff] = curfunc
                        znlen[ff] = len
                        con[h + j] = curfunc
                        if len == 1:
                            sch1 = sch1 + 1
                        if len == 2:
                            sch2 = sch2 + 1
                        if len == 3:
                            sch3 = sch3 + 1
                        if len == 4:
                            sch4 = sch4 + 1
                        if len == 5:
                            sch5 = sch5 + 1
                        if len == 6:
                            sch6 = sch6 + 1 
                        j = j + 1
                    w = w + 1
                    if counter == 0:
                        break
                if counter == 0:
                    break
                t = t + 1
                if con[t] > 4 * 10 ** (3 + 4 * (len - 2)): # это, чтобы показать, что данное con[t] более, чем любое возможное для данной длины. 400 > {300, ...., 222} и т.д.
                    len = len + 1
                    print(" change len, now len = ", len, " counter = ", counter, " t = ", t, "w = ", w)
            if counter == 0:
                break
            print("len = ", len)
            t = h
            h = h + j
            j = 0
            if last == 1:
                last = 0

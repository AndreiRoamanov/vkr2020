# ПОСТРОЕНИЕ ОБОБЩЁННЫХ ПОЛИНОМОВ ЧЕРЕЗ ПОЛИНОМ ЖЕГАЛКИНА СО СКЛЕИВАНИЕМ СМЕЖНЫХ - X1X2X3 + X1X2 = X1X2!X3

import random

while (True):
        n = int(input())
        if 1 == 1:
            len = 1
            c = []
            for ci in range (0, 2 ** n):
                c.append(0)
            d = []
            for di in range (0, 2 ** n - 1):
                d.append(0)
            znpasc = []
            pascal = []
            bufpascal = []
            for pi in range (0, 2 ** n):
                pascal.append(0)
                bufpascal.append(0)
            maslen = []
            for len in range (0, 4 ** n):
                maslen.append(0)
            for r in range (0, 65536):
                i = random.randint(0, 2 ** 2 ** n - 1)
                if r % 500 == 0:
                    print("i = ", i, " r = ", r)
                x = i
                doublex = x
                for ci in range (0, 2 ** n):
                    c.append(0)
                ci = 2 ** n - 1
                while ci >= 0:
                    c[ci] = doublex % 2
                    doublex = doublex // 2
                    ci = ci - 1
                for di in range (0, 2 ** n - 1):
                    d.append(0)
                znpasc = []
                for pi in range (0, 2 ** n):
                    pascal.append(0)
                    znpasc.append(0)
                pi = 0
                di = 0
                ci = 0
                buffunc = 0
                thislast = 0
                kraiwas = 1
                lastci = 2 ** n - 1
                pascal[pi] = c[ci]
                pi = pi + 1
                while (lastci > 0):
                    while (ci < lastci):
                        d[di] = (c[ci] + c[ci + 1]) % 2
                        ci = ci + 1
                        di = di + 1
                    pascal[pi] = d[0]
                    di = 0
                    pi = pi + 1
                    for ci in range (0, lastci):
                        c[ci] = d[ci]
                        d[ci] = 0
                    lastci = lastci - 1
                    ci = 0
                if pi == 0:
                    znpasc[pi] = 3
                for pi in range (1, 2 ** n):
                        bpi = pi
                        bzn = 0
                        k = 0
                        while (bpi > 0):
                            bzn = bzn + (bpi % 2) * 10 ** k
                            k = k + 1
                            bpi = bpi // 2
                        znpasc = bzn
                countcnt = 2 ** n - 1
                cnt = 0
                pascalv2c1 = []
                for r in range (0, n ** 2):
                    pascalv2c1.append(0)
                while (countcnt > 0):
                    uselessmass = []
                    for uu in range (0, n):
                        uselessmass.append(0)
                    uselessbuf = countcnt
                    us = 0
                    while (uselessbuf != 0):
                        if (uselessbuf % 2 == 0):
                            uselessmass[us] = 1
                        us = us + 1
                        uselessbuf = uselessbuf // 2
                             
                    for ww in range (0, n):
                        if uselessmass[ww] == 1:
                            continue
                        if pascal[countcnt] == 1 and pascal[countcnt - 2 ** ww] == 1:
                            pascal[countcnt] = pascal[countcnt - 2 ** ww] = 0
                            pascalv2c1[cnt] = 1 
                            cnt = cnt + 1
                            break
                    countcnt = countcnt - 1
                            
                len1 = 0
                for ww in range (0, 2 ** n):
                    if pascal[ww] == 1:
                        len1 = len1 + 1
                len1 = len1 + cnt
                maslen[len1] = maslen[len1] + 1
            for lenlen in range (0, 2 ** n):
                print("len = ", lenlen, " cnt = ", maslen[lenlen])

# ПОСТРОЕНИЕ ЧЕРЕЗ РАЗЛОЖЕНИЕ ШЕННОНА ДЛЯ N = 6, 7, 8

from random import randint

def funcfor5(z, mod, temp): # эта функция должна выдавать минимальный полином для данной f.
    bufitoglen = 2 ** 4
    if temp == 1:
        am = 0
        bm = 16
    elif temp == 2:
        am = 1
        bm = 8 
    elif temp == 3:
        am = 2
        bm = 4
    elif temp == 4:
        am = 3
        bm = 2
    elif temp == 5:
        am = 4
        bm = 1
    if 1 == 1:
        if mod == 0:
            newz = z
            nz1 = 0
            nz2 = 0
            scht = 1
            while newz != 0:
                nz1 = nz1 * 10 ** (2 ** (n - am)) + newz // 10 ** (2 ** (n + 1) - scht * bm)
                newz = newz % 10 ** (2 ** (n + 1) - scht * bm)
                scht = scht + 1
                nz2 = nz2 * 10 ** (2 ** (n - am)) + newz // 10 ** (2 ** (n + 1) - scht * bm)
                newz = newz % 10 ** (2 ** (n + 1) - scht * bm)
                scht = scht + 1
            bnz1 = nz1
            dz1 = 0
            rk = 0
            while (bnz1 != 0):
                dz1 = dz1 + 2 ** rk * (bnz1 % 10)
                rk = rk + 1
                bnz1 = bnz1 // 10
            pol1 = znpol[dz1]
            len1 = znlen[dz1]
            bnz2 = nz2
            dz2 = 0
            rk = 0
            while (bnz2 != 0):
                dz2 = dz2 + 2 ** rk * (bnz2 % 10)
                rk = rk + 1
                bnz2 = bnz2 // 10
            pol2 = znpol[dz2]
            len2 = znlen[dz2]
            wwpol1 = pol1
            eq = 0
            needpol = 0
            polwas = []
            for ppolss in range (0, len2):
                polwas.append(0)
            was = 0
            
            while (wwpol1 != 0):
                simplepol1 = wwpol1 % 10 ** n
                wwpol2 = pol2
                cct = 0
                while (wwpol2 != 0):
                    simplepol2 = wwpol2 % 10 ** n
                    if simplepol1 == simplepol2:
                        eq = eq + 1
                        needpol = needpol * 10 ** (n + 1) + 0 * 10 ** n + simplepol1
                        was = 1
                        polwas[cct] = 1
                        break
                    cct = cct + 1
                    wwpol2 = wwpol2 // 10 ** n
                if was == 0:
                    needpol = needpol * 10 ** (n + 1) + 2 * 10 ** n + simplepol1
                was = 0
                wwpol1 = wwpol1 //10 ** n
            cct = 0
            wwpol2 = pol2
            while (wwpol2 != 0):
                simplepol2 = wwpol2 % 10 ** n
                if polwas[cct] == 0:
                    needpol = needpol * 10 ** (n + 1) + 1 * 10 ** n + simplepol2
                cct = cct + 1
                wwpol2 = wwpol2 // 10 ** n 
            itoglen = len1 + len2 - eq
            return needpol

            if itoglen < bufitoglen:
                bufitoglen = itoglen
                bufneedpol = needpol


        elif mod == 1:
            newz = z
            nz1 = 0
            nz2 = 0
            scht = 1
            while newz != 0:
                nz1 = nz1 * 10 ** (2 ** (n - am)) + newz // 10 ** (2 ** (n + 1) - scht * bm)
                newz = newz % 10 ** (2 ** (n + 1) - scht * bm)
                scht = scht + 1
                nz2 = nz2 * 10 ** (2 ** (n - am)) + newz // 10 ** (2 ** (n + 1) - scht * bm)
                newz = newz % 10 ** (2 ** (n + 1) - scht * bm)
                scht = scht + 1
            bnz1 = nz1
            dz1 = 0
            rk = 0
            while (bnz1 != 0):
                dz1 = dz1 + 2 ** rk * (bnz1 % 10)
                rk = rk + 1
                bnz1 = bnz1 // 10
            pol1 = znpol[dz1]
            len1 = znlen[dz1]
#            print("dz1 = ", dz1 ,", pol1 = ", pol1)
            bnz2 = nz2
            dz2 = 0
            rk = 0
            while (bnz2 != 0):
                dz2 = dz2 + 2 ** rk * (bnz2 % 10)
                rk = rk + 1
                bnz2 = bnz2 // 10
            pol2 = znpol[dz2]
            len2 = znlen[dz2]
            hnum = dz1 ^ dz2 # функция h = f(0, x1 .. xn) + f(1, x1 .. xn) в представлении 2 и 3 - xh + g = f и !xh + g = f
            if (temp == 0):
                print("hnum = ", hnum)
            hpol = znpol[hnum]
            hlen = znlen[hnum]
            if (temp == 0):
                print("hpol = ", hpol, " pol1 = ", pol1, " pol2 = ", pol2)
            wwpol1 = hpol               
            eq = 0
            polwas = []
            for ppolss in range (0, max(len1, len2)):
                polwas.append(0)
            needpol = 0
            was = 0
            while (wwpol1 != 0):
                simplepol1 = wwpol1 % 10 ** n
                wwpol2 = pol1
                cct = 0
                while (wwpol2 != 0):
                    simplepol2 = wwpol2 % 10 ** n
                    if simplepol1 == simplepol2:
                        eq = eq + 1  # eq означает, количество одинаковых мономов, то есть то, что можно сократить. в дальнейшем, смотрим на eq - сколько сокращено. и len = lenmax - eq
                        needpol = needpol * 10 ** (n + 1) + 2 * 10 ** n + simplepol1
                        was = 1
                        polwas[cct] = 1
                        break
                    cct = cct + 1
                    wwpol2 = wwpol2 // 10 ** n
                if was == 0:
                    needpol = needpol * 10 ** (n + 1) + 1 * 10 ** n + simplepol1
                was = 0
                wwpol1 = wwpol1 //10 ** n
            cct = 0
            wwpol2 = pol2
            while (wwpol2 != 0):
                simplepol2 = wwpol2 % 10 ** n
                if polwas[cct] == 0:
                    needpol = needpol * 10 ** (n + 1) + 0 * 10 ** n + simplepol2
                cct = cct + 1
                wwpol2 = wwpol2 // 10 ** n 
            itoglen = len1 + hlen - eq
            if (temp == 0):
                print("needpol = ", needpol)
            return needpol
      
                
        elif mod == 2:
            newz = z
            nz1 = 0
            nz2 = 0
            scht = 1
            while newz != 0:
                nz1 = nz1 * 10 ** (2 ** (n - am)) + newz // 10 ** (2 ** (n + 1) - scht * bm)
                newz = newz % 10 ** (2 ** (n + 1) - scht * bm)
                scht = scht + 1
                nz2 = nz2 * 10 ** (2 ** (n - am)) + newz // 10 ** (2 ** (n + 1) - scht * bm)
                newz = newz % 10 ** (2 ** (n + 1) - scht * bm)
                scht = scht + 1
            bnz1 = nz1
            dz1 = 0
            rk = 0
            while (bnz1 != 0):
                dz1 = dz1 + 2 ** rk * (bnz1 % 10)
                rk = rk + 1
                bnz1 = bnz1 // 10
            pol1 = znpol[dz1]
            len1 = znlen[dz1]
            bnz2 = nz2
            dz2 = 0
            rk = 0
            while (bnz2 != 0):
                dz2 = dz2 + 2 ** rk * (bnz2 % 10)
                rk = rk + 1
                bnz2 = bnz2 // 10
            pol2 = znpol[dz2]
            len2 = znlen[dz2]
            hnum = dz1 ^ dz2 # функция h = f(0, x1 .. xn) + f(1, x1 .. xn) в представлении 2 и 3 - xh + g = f и !xh + g = f
            hpol = znpol[hnum]
            hlen = znlen[hnum]
            wwpol1 = hpol                    
            eq = 0
            polwas = []
            for ppolss in range (0, max(len1, len2)):
                polwas.append(0)
            needpol = 0
            was = 0
            while (wwpol1 != 0):
                simplepol1 = wwpol1 % 10 ** n
                wwpol2 = pol2
                cct = 0
                while (wwpol2 != 0):
                    simplepol2 = wwpol2 % 10 ** n
                    if simplepol1 == simplepol2:
                        eq = eq + 1  # eq означает, количество одинаковых мономов, то есть то, что можно сократить. в дальнейшем, смотрим на eq - сколько сокращено. и len = lenmax - eq
                        needpol = needpol * 10 ** (n + 1) + 1 * 10 ** n + simplepol1
                        was = 1
                        polwas[cct] = 1
                        break
                    cct = cct + 1
                    wwpol2 = wwpol2 // 10 ** n
                if was == 0:
                    needpol = needpol * 10 ** (n + 1) + 2 * 10 ** n + simplepol1
                was = 0
                wwpol1 = wwpol1 //10 ** n
            cct = 0
            wwpol2 = pol2
            while (wwpol2 != 0):
                simplepol2 = wwpol2 % 10 ** n
                if polwas[cct] == 0:
                    needpol = needpol * 10 ** (n + 1) + 0 * 10 ** n + simplepol2
                cct = cct + 1
                wwpol2 = wwpol2 // 10 ** n 
            itoglen = hlen + len2 - eq
            return needpol


    
def funcfor6(newpol1, newpol2, mod, temp):
    bufitoglennew = 2 ** n
    wwpol123 = newpol1
    l11 = 0
    forlnewpol1 = newpol1
    while (forlnewpol1 != 0):
        forlnewpol1 = forlnewpol1 // 10
        l11 = l11 + 1
    itoglen1 = l11 // (n + 1) + 1
    forlnewpol2 = newpol2
    l22 = 0
    while (forlnewpol2 != 0):
        forlnewpol2 = forlnewpol2 // 10
        l22 = l22 + 1
    itoglen2 = l22 // (n + 1) + 1
    eq = 0
    allpol = 0
    polwas = []
    for ppolss in range (0, max(itoglen2, itoglen1)):
        polwas.append(0)
    was = 0
    wwpol223 = newpol2
    while (wwpol123 != 0):
        simplepol123 = wwpol123 % 10 ** (n + 1)
        wwpol223 = newpol2
        cct = 0
        while (wwpol223 != 0):
            simplepol223 = wwpol223 % 10 ** (n + 1)
            if simplepol123 == simplepol223:
                eq = eq + 1  # eq означает, количество одинаковых мономов, то есть то, что можно сократить. в дальнейшем, смотрим на eq - сколько сокращено. и len = lenmax - eq
                allpol = allpol * 10 ** (n + 2) + simplepol123
                was = 1
                polwas[cct] = 1
                break
            cct = cct + 1
                    
            wwpol223 = wwpol223 // 10 ** (n + 1)
        if was == 0:
            allpol = allpol * 10 ** (n + 2) + 2 * 10 ** (n + 1) + simplepol123
        was = 0
        wwpol123 = wwpol123 // 10 ** (n + 1)
    cct = 0
    wwpol223 = newpol2
    while (wwpol223 != 0):
        simplepol223 = wwpol223 % 10 ** (n + 1)
        if polwas[cct] == 0:
            allpol = allpol * 10 ** (n + 2) + 10 ** (n + 1) + simplepol223
        cct = cct + 1
        wwpol223 = wwpol223 // 10 ** (n + 1) 
    itoglen = itoglen1 + itoglen2 - eq
    if itoglen < bufitoglennew: 
        bufitoglennew = itoglen
    return allpol


def funcfor7(newpol1, newpol2, mod, temp):
    newn = 7
    bufitoglennew = 2 ** newn
    wwpol123 = newpol1
    l11 = 0
    forlnewpol1 = newpol1
    while (forlnewpol1 != 0):
        forlnewpol1 = forlnewpol1 // 10
        l11 = l11 + 1
    itoglen1 = l11 // (newn - 1) + 1
    forlnewpol2 = newpol2
    l22 = 0
    while (forlnewpol2 != 0):
        forlnewpol2 = forlnewpol2 // 10
        l22 = l22 + 1
    itoglen2 = l22 // (newn - 1) + 1
    eq = 0
    allpol = 0
    polwas = []
    for ppolss in range (0, max(itoglen2, itoglen1)):
        polwas.append(0)
    was = 0
    wwpol223 = newpol2
    while (wwpol123 != 0):
        simplepol123 = wwpol123 % 10 ** (newn - 1)
        wwpol223 = newpol2
        cct = 0
        while (wwpol223 != 0):
            simplepol223 = wwpol223 % 10 ** (newn - 1)
            if simplepol123 == simplepol223:
                eq = eq + 1 
                allpol = allpol * 10 ** newn + simplepol123
                was = 1
                polwas[cct] = 1
                break
            cct = cct + 1
                    
            wwpol223 = wwpol223 // 10 ** (newn - 1)
        if was == 0:
            allpol = allpol * 10 ** newn + 2 * 10 ** (newn - 1) + simplepol123
        was = 0
        wwpol123 = wwpol123 // 10 ** (newn - 1)
    cct = 0
    wwpol223 = newpol2
    while (wwpol223 != 0):
        simplepol223 = wwpol223 % 10 ** (newn - 1)
        if polwas[cct] == 0:
            allpol = allpol * 10 ** newn + 10 ** (newn - 1) + simplepol223
        cct = cct + 1
        wwpol223 = wwpol223 // 10 ** (newn - 1) 
    itoglen = itoglen1 + itoglen2 - eq
    if itoglen < bufitoglennew: 
        bufitoglennew = itoglen
    return allpol


def funcfor8(newpol1, newpol2, mod, temp):
    newn = 8
    bufitoglennew = 2 ** newn
    wwpol123 = newpol1
    l11 = 0
    forlnewpol1 = newpol1
    while (forlnewpol1 != 0):
        forlnewpol1 = forlnewpol1 // 10
        l11 = l11 + 1
    itoglen1 = l11 // (newn - 1) + 1
    forlnewpol2 = newpol2
    l22 = 0
    while (forlnewpol2 != 0):
        forlnewpol2 = forlnewpol2 // 10
        l22 = l22 + 1
    itoglen2 = l22 // (newn - 1) + 1
    eq = 0
    allpol = 0
    polwas = []
    for ppolss in range (0, max(itoglen2, itoglen1)):
        polwas.append(0)
    was = 0
    wwpol223 = newpol2
    while (wwpol123 != 0):
        simplepol123 = wwpol123 % 10 ** (newn - 1)
        wwpol223 = newpol2
        cct = 0
        while (wwpol223 != 0):
            simplepol223 = wwpol223 % 10 ** (newn - 1)
            if simplepol123 == simplepol223:
                eq = eq + 1
                allpol = allpol * 10 ** newn + simplepol123
                was = 1
                polwas[cct] = 1
                break
            cct = cct + 1
                    
            wwpol223 = wwpol223 // 10 ** (newn - 1)
        if was == 0:
            allpol = allpol * 10 ** newn + 2 * 10 ** (newn - 1) + simplepol123
        was = 0
        wwpol123 = wwpol123 // 10 ** (newn - 1)
    cct = 0
    wwpol223 = newpol2
    while (wwpol223 != 0):
        simplepol223 = wwpol223 % 10 ** (newn - 1)
        if polwas[cct] == 0:
            allpol = allpol * 10 ** newn + 10 ** (newn - 1) + simplepol223
        cct = cct + 1
        wwpol223 = wwpol223 // 10 ** (newn - 1) 
    itoglen = itoglen1 + itoglen2 - eq
    if itoglen < bufitoglennew: 
        bufitoglennew = itoglen
    return allpol



def fncpol6(z, mod, temp):
    newn = 6
    bufitoglennew = 2 ** newn
    if temp == 1:
        am = 1
        bm = 32
    elif temp == 2:
        am = 2
        bm = 16 
    elif temp == 3:
        am = 3
        bm = 8
    elif temp == 4:
        am = 4
        bm = 4
    elif temp == 5: 
        am = 5
        bm = 2
    elif temp == 6: 
        am = 6
        bm = 1
    if True:
        for ccnnt in range (0, 1):
            bufitoglennew = 2 ** (n + 1)
            bufitoglen1 = 2 ** (n)
            bufitoglen2 = 2 ** (n)
            bufpol = 0
            newz = z
            nz1 = 0
            nz2 = 0
            scht = 1
            while newz != 0:
                nz1 = nz1 * 10 ** (2 ** (newn - am)) + newz // 10 ** (2 ** newn - scht * bm)
                newz = newz % 10 ** (2 ** newn - scht * bm)
                scht = scht + 1
                nz2 = nz2 * 10 ** (2 ** (newn - am)) + newz // 10 ** (2 ** newn - scht * bm)
                newz = newz % 10 ** (2 ** newn - scht * bm)
                scht = scht + 1
            bnz1 = nz1
            bnz2 = nz2
            for ai in range (0, 3):
                for aj in range (1, 6):
                    newpol1 = funcfor5(bnz1, ai, aj)
                    if temp == 0:
                        print(" 6 newpol1 = ", newpol1, " ai = ", ai, " aj = ", aj)
                    for ak in range (0, 3):
                        for az in range (1, 6):
                            newpol2 = funcfor5(bnz2, ak, az)
                            if temp == 0:
                                print(" 6 newpol2 = ", newpol2, " ak = ", ak, " az = ", az)
                            allpol = funcfor6(newpol1, newpol2, 0, 0)
                            if temp == 0:
                                print(" 6 allpol = ", allpol, " ai = ", ai, " aj = ", aj, " ak = ", ak, " az = ", az)
                            lenn = 0
                            forlallpol = allpol
                            while (forlallpol != 0):
                                forlallpol = forlallpol // 10
                                lenn = lenn + 1
                            itoglen = lenn // (n + 2) + 1
                            if itoglen < bufitoglennew:
                                bufitoglennew = itoglen
                                bufpol = allpol
            return bufpol





def fncpol7(z, mod, temp):
    newn = 7
    bufitoglennew = 2 ** newn
    if temp == 1:
        am = 1
        bm = 64
    elif temp == 2:
        am = 2
        bm = 32 
    elif temp == 3:
        am = 3
        bm = 16
    elif temp == 4:
        am = 4
        bm = 8
    elif temp == 5:
        am = 5
        bm = 4
    elif temp == 6:
        am = 6
        bm = 2
    elif temp == 7:
        am = 7
        bm = 1
    if True:
        if True:
            bufitoglennew = 2 ** (n + 2)
            bufitoglen1 = 2 ** (n + 2)
            bufitoglen2 = 2 ** (n + 2)
            bufpol = 0
            
            newz = z
            nz1 = 0
            nz2 = 0
            scht = 1
            while newz != 0:
                nz1 = nz1 * 10 ** (2 ** (newn - am)) + newz // 10 ** (2 ** newn - scht * bm)
                newz = newz % 10 ** (2 ** newn - scht * bm)
                scht = scht + 1
                nz2 = nz2 * 10 ** (2 ** (newn - am)) + newz // 10 ** (2 ** newn - scht * bm)
                newz = newz % 10 ** (2 ** newn - scht * bm) 
                scht = scht + 1
            bnz1 = nz1
            bnz2 = nz2
            for bi in range (0, 1):
                for bj in range (1, 7):
                    newpol1 = fncpol6(bnz1, bi, bj)
                    for bk in range (0, 1):
                        for bz in range (1, 7):
                            newpol2 = fncpol6(bnz2, bk, bz)
                            allpol = funcfor7(newpol1, newpol2, 0, 0) 
                            lenn = 0
                            forlallpol = allpol
                            while (forlallpol != 0):
                                forlallpol = forlallpol // 10
                                lenn = lenn + 1
                            itoglen = lenn // newn + 1
                            if itoglen < bufitoglennew:
                                bufitoglennew = itoglen
                                bufpol = allpol
            return bufpol


                                

def fncpol8(z, mod, temp):
    newn = 8
    bufitoglennew = 2 ** newn
    if temp == 1:
        am = 1
        bm = 128
    elif temp == 2:
        am = 2
        bm = 64
    elif temp == 3:
        am = 3
        bm = 32
    elif temp == 4:
        am = 4
        bm = 16
    elif temp == 5:
        am = 5
        bm = 8
    elif temp == 6:
        am = 6
        bm = 4
    elif temp == 7:
        am = 7
        bm = 2
    elif temp == 8:
        am = 8
        bm = 1
    if True:
        if True:
            bufitoglennew = 2 ** (n + 3)
            bufitoglen1 = 2 ** (n + 1)
            bufitoglen2 = 2 ** (n + 1)
            bufpol = 0            
            newz = z
            nz1 = 0
            nz2 = 0
            scht = 1
            while newz != 0:
                nz1 = nz1 * 10 ** (2 ** (newn - am)) + newz // 10 ** (2 ** newn - scht * bm)
                newz = newz % 10 ** (2 ** newn - scht * bm)
                scht = scht + 1
                nz2 = nz2 * 10 ** (2 ** (newn - am)) + newz // 10 ** (2 ** newn - scht * bm)
                newz = newz % 10 ** (2 ** newn - scht * bm)
                scht = scht + 1
            bnz1 = nz1
            bnz2 = nz2
            for bi in range (0, 1): 
                for bj in range (1, 8):    
                    newpol1 = fncpol7(bnz1, bi, bj)
                    for bk in range (0, 1):
                        for bz in range (1, 8):
                            newpol2 = fncpol7(bnz2, bk, bz)
                            allpol = funcfor8(newpol1, newpol2, 0, 0)
                            lenn = 0
                            forlallpol = allpol
                            while (forlallpol != 0):
                                forlallpol = forlallpol // 10
                                lenn = lenn + 1
                            itoglen = lenn // newn + 1
                            if itoglen < bufitoglennew:
                                bufitoglennew = itoglen
                                bufpol = allpol
            return bufpol                                





while (True):
#    n = int(input())
    n = 4
    if 1 == 1:
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
#            print(con[z])
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
                    if pol[ff] == 0:
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
                
        print("next work")
        print(funcfor5(10100011101001000101001101010001, 0, 1))
        print(funcfor5(10100011101001000101001101010001, 0, 2))
        print(funcfor5(10100011101001000101001101010001, 0, 3))
        print(funcfor5(10100011101001000101001101010001, 0, 4))
        print(funcfor5(10100011101001000101001101010001, 0, 5))
        print(funcfor5(10100011101001000101001101010001, 1, 1))
        print(funcfor5(10100011101001000101001101010001, 1, 2))
        print(funcfor5(10100011101001000101001101010001, 1, 3))
        print(funcfor5(10100011101001000101001101010001, 1, 4))
        print(funcfor5(10100011101001000101001101010001, 1, 5))
        print(funcfor5(10100011101001000101001101010001, 2, 1))
        print(funcfor5(10100011101001000101001101010001, 2, 2))
        print(funcfor5(10100011101001000101001101010001, 2, 3))
        print(funcfor5(10100011101001000101001101010001, 2, 4))
        print(funcfor5(10100011101001000101001101010001, 2, 5)) 
        print("next n = 6")
        inpcnt = 1
        newn = 6
        itoglennew6 = []
        for iteritog in range (0, 2 ** (n + 2)):
            itoglennew6.append(0)
        for rancnt in range (0, inpcnt):
            bufitoglennew = 2 ** newn
            itoglen = 0
            allpol = 0
            bufpol = 0
            if rancnt % 1000 == 0:
                print("rancnt = ", rancnt)
            newzn = randint(0, 2 ** 2 ** 6)
            if rancnt % 1000 == 0:
                print("6 newzn = ", newzn)
            bufitoglennew = 2 ** (n + 1)
            bufitoglen1 = 2 ** (n)
            bufitoglen2 = 2 ** (n)
            bufpol = 0        
            decz = newzn
            z = 0
            rk = 0
            while decz > 0:
                z = z + (decz % 2) * 10 ** rk
                decz = decz // 2
                rk = rk + 1
            for w in range (1, 7):
                allpol = fncpol6(z, 0, w)
                if rancnt % 1000 == 0:
                    print("here 6 allpol = ", allpol)
                lenn = 0
                forlallpol = allpol
                while (forlallpol != 0):
                    forlallpol = forlallpol // 10
                    lenn = lenn + 1
                itoglen = (lenn - 1) // newn + 1
                if itoglen < bufitoglennew:
                    bufitoglennew = itoglen
                    bufpol = allpol
            if rancnt % 1000 == 0:
                print("final 6 bufpol = ", bufpol)
                print("final 6 bufitoglennew = ", bufitoglennew)

            itoglennew6[bufitoglennew] = itoglennew6[bufitoglennew] + 1
        for iteritog in range (0, 2 ** (n + 1)):
            print("iter = ", iteritog, " = ", itoglennew6[iteritog])





# далее от 7 переменных
    if 1 == 1:
        print("next n = 7")
        newn = 7
        itoglen = 0
        inpcnt = 1
        itoglennew7 = []
        for iteritog in range (0, 2 ** (n + 3)):
            itoglennew7.append(0)
        for rancnt in range (0, inpcnt):
            bufitoglennew = 2 ** newn
            itoglen = 0
            allpol = 0
            bufpol = 0
            if rancnt % 100 == 0:
                print("rancnt = ", rancnt)
            newzn = randint(0, 2 ** 2 ** 7)
            if rancnt % 100 == 0:
                print("newzn = ",newzn)
            bufitoglennew = 2 ** (n + 2)
            bufitoglen1 = 2 ** (n + 1)
            bufitoglen2 = 2 ** (n + 1)
            bufpol = 0       
            decz = newzn
            z = 0
            rk = 0
            while decz > 0:
                z = z + (decz % 2) * 10 ** rk
                decz = decz // 2
                rk = rk + 1
            for w in range (1, 8):
                allpol = fncpol7(z, 0, w)
                lenn = 0
                forlallpol = allpol
                while (forlallpol != 0):
                    forlallpol = forlallpol // 10
                    lenn = lenn + 1
                itoglen = (lenn - 1) // newn + 1
                if itoglen < bufitoglennew:
                    bufitoglennew = itoglen
                    bufpol = allpol
            if rancnt % 100 == 0:
                print("final 7 bufpol = ", bufpol)
                print("final 7 bufitoglennew = ", bufitoglennew)
            if rancnt % 100 == 0:
                for iteritog in range (0, 2 ** (n + 1)):
                    print("iter = ", iteritog, " = ", itoglennew7[iteritog])
                    print("-----------")
            itoglennew7[bufitoglennew] = itoglennew7[bufitoglennew] + 1
        for iteritog in range (0, 2 ** (n + 1)):
            print("iter = ", iteritog, " = ", itoglennew7[iteritog])
        
            
                    






            


# далее от 8 переменных
    if 1 == 1:
        print("next n = 8")
        inpcnt = 200
        itoglennew8 = []
        newn = 8
        for iteritog in range (0, 2 ** (n + 4)):
            itoglennew8.append(0)
        for rancnt in range (0, inpcnt):
            bufitoglennew = 2 ** newn
            allpol = 0
            bufpol = 0
            if rancnt % 5 == 0:
                print("rancnt = ", rancnt)
            newzn = randint(0, 2 ** 2 ** 8)
            decz = newzn
            z = 0
            rk = 0
            while decz > 0:
                z = z + (decz % 2) * 10 ** rk
                decz = decz // 2
                rk = rk + 1
            if rancnt % 5 == 0:
                print("newzn = ",newzn)
            for w in range (1, 9):
                allpol = fncpol8(z, 0, w)
                print("here 8 allpol = ", allpol) # полином минимальной длины для данной функции
                lenn = 0
                forlallpol = allpol
                while (forlallpol != 0):
                    forlallpol = forlallpol // 10
                    lenn = lenn + 1
                itoglen = (lenn - 1) // newn + 1
                if itoglen < bufitoglennew:
                    bufitoglennew = itoglen
                    bufpol = allpol
            if rancnt % 10 == 0:
                print("8 bufpol = ", bufpol) # полином минимальной длины для данной функции
                print("8 bufitoglennew = ", bufitoglennew)
            itoglennew8[bufitoglennew] = itoglennew8[bufitoglennew] + 1
            if rancnt % 25 == 0:
                print("now rancnt: ", rancnt)
                for iteritog in range (0, 2 ** (n + 2)):
                    print("iter = ", iteritog, " = ", itoglennew8[iteritog])
        for iteritog in range (0, 2 ** (n + 2)):
            print("iter = ", iteritog, " = ", itoglennew8[iteritog])

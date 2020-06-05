# ОПРЕДЕЛЕНИЕ СООТНОШЕНИЯ ЧИСЛА МИНИМАЛЬНЫХ ОБОБЩЁННЫХ ПОЛИНОМОВ ДЛЯ СЛУЧАЙНО ЗАДАННЫХ ФУНКЦИЙ, ПОСТРОЕННОЕ ПРИ ПОМОЩИ SAT-РЕШАТЕЛЯ
# ЧЕРЕЗ АЛГОРИТМ 2

#!/usr/bin/python
import os
import subprocess
import shlex
import commands
from random import randint

while(True):
    n = int(input())
    maslen = []
    for i in range (0, 2 ** (n - 1)):
        maslen.append(0)
    cnt = int(input())
    for ranf in range (0, cnt):
        b = []
        z = []
        for i in range (0, 2 ** n):
            b.append(0)
        a = randint(0, 2 ** 2 ** n)
        bufk = a
        print bufk
        l = 2 ** n - 1
        s = l
        while bufk > 0:
            b[s] = bufk % 2
            bufk = bufk // 2
            s = s - 1
        k = 1
        j = 0
        pol = []
        for i in range (0, 2 * n * k):
            pol.append(0)
        f = open('a.in', 'w')
        f.close()
        flnew = 0
        while (True):
            if flnew == 1:
                flnew = 0
            r = 2 ** n
            f = open('a.in', 'a')
            ff1 = 2 * k * n + k * r
            ff2 = r * (n * k + k + 2 ** (k - 1))
            newz = 0
            satted = 0
            flag = 0
            u = -1
            for i in range (1, n * k + 1):
                f.write(str(-i) + " " + str(-(i + n * k)) + " 0" + '\n')
            while (u < r - 1):
                u = u + 1
                if flag == 1:
                    flag = 0
                    u = 0
                vec = []
                for i in range (0, n):
                    vec.append(0)
                bufu = u
                for z in range (0, n): 
                    vec[n - z - 1] = bufu % 2
                    bufu = bufu // 2
                    z = z + 1
                z = 0
                znpol = 0
                for l in range (0, k):
                    znmon = 1
                    for z in range (0, n):
                        if ((vec[z] == 1 and pol[k * n + z + l * n] == 1) or (vec[z] == 0 and pol[z + l * n] == 1)):
                            znmon = 0
                    znpol = znpol + znmon
                if znpol % 2 == b[u]:
                    continue                               

                z = 0
                f = open('a.in', 'a')
                par1 = 1
                for i in range (0, k):
                    for j in range(0, n):
                        if vec[j] == 0:  
                            f.write(str(-(2 * k * n + 1 + z + newz)) + " " + str(-par1) + " 0" + '\n')
                        else:
                            f.write(str(-(2 * k * n + 1 + z + newz)) + " " + str(-(k * n + par1)) + " 0" + '\n')
                        par1 = par1 + 1
                    z = z + 1
                par1 = 1
                z = 0
                for i in range (0, k):
                    f.write(str(2 * k * n + 1 + z + newz) + " ")
                    for j in range(0, n):
                        if vec[j] == 0:  
                            f.write(str(par1) + " ")
                        else:
                            f.write(str(k * n + par1) + " ")
                        par1 = par1 + 1
                    f.write("0" + '\n')
                    z = z + 1
                if 1 == 1:  
                    if k == 1:
                    	if b[u] == 1:
                            f.write(str(2 * k * n + 1 + newz) + " 0" + '\n')
                        else:
                            f.write(str(-(2 * k * n + 1 + newz)) + " 0" + '\n')
                    if k == 2:
                    	if b[u] == 1:
                            f.write(str(2 * k * n + 1 + newz) + " " + str(2 * k * n + 2 + newz) + " 0" + '\n')
                            f.write(str(-(2 * k * n + 1 + newz)) + " " + str(-(2 * k * n + 2 + newz)) + " 0" + '\n')
                        else:
                            f.write(str(-(2 * k * n + 1 + newz)) + " " + str((2 * k * n + 2 + newz)) + " 0" + '\n')
                            f.write(str((2 * k * n + 1 + newz)) + " " + str(-(2 * k * n + 2 + newz)) + " 0" + '\n')
                    else:
                        zpor = 0
                        f1 = 2 * k * n + 1 + newz + zpor
                        f2 = 2 * k * n + 2 + newz + zpor
                        if k != 3:
                            f3 = 2 * k * n + k + 1 + newz + zpor
                        else:
                            if b[u] == 1:
                                f3 = -(2 * k * n + k + newz)
                            else:
                                f3 = 2 * k * n + k + newz
                        for e in range (0, k - 2):
                           f.write(str(f1) + " " + str(f2) + " " + str(-f3) + " 0" + '\n')
                           f.write(str(-f1) + " " + str(-f2) + " " + str(-f3) + " 0" + '\n') 
                           f.write(str(f1) + " " + str(-f2) + " " + str(f3) + " 0" + '\n') 
                           f.write(str(-f1) + " " + str(f2) + " " + str(f3) + " 0" + '\n')
                           f1 = f3
                           f2 = f2 + 1
                           if e != k - 4:
                               f3 = f3 + 1
                           else:
                               if b[u] == 1:
                                   f3 = -(2 * k * n + k + newz)
                               else:
                                   f3 = 2 * k * n + k + newz
                if k > 3:
                    newz = newz + k + k - 3 
                else:
                    newz = newz + k
                f.close()
                os.system('/home/andrei/minisat/simp/minisat_static a.in b.out')
                ff = open('b.out')
                print("u = ", u)
                print("cnt = ", ranf)
                if ff.read(3) == "SAT":
                    print("len = ", k)
                    pol = []                            
                    for i in range (0, 2 * n * k): 
                        pol.append(0) 
                    ff.read(1)
                    for at in range (0, 2 * n * k):
                        rd = ff.read(1)
                        if rd != '-':
                            pol[at] = 1
                        else:
                            rd = ff.read(1)
                            pol[at] = 0
                        if at > 8:
                            rd = ff.read(1)
                        if at > 98:
                            rd = ff.read(1)
                        if at > 998:
                            rd = ff.read(1)                       
                        rd = ff.read(1)
                    u = 0
                    flag = 1
                    continue
                else: 
                    k = k + 1
                    print("now new k = ", k )
                    for cda in range (0, 5):
                        print("###################")
                        print("###################")
                    if k > 2 ** (n - 1):
                        break
                    if k > 6 and n > 5:
                        maslen[2 ** (n - 1) - 1] = maslen[2 ** (n - 1) - 1] + 1
                        break
                    pol = []
                    for i in range (0, 2 * n * k):
                        pol.append(0)
                    f = open('a.in', 'w')  
                    f.close()
                    flnew = 1
                    print("flnew")
                    break
            print("END, K = ", k)
            if flnew != 1:
                break
        maslen[k - 1] = maslen[k - 1] + 1
        print "now cnt = ", ranf
    print "####################################"
    print "####################################"
    print "####################################"
    print "####################################"
    print "####################################"
    for i in range (0, 2 ** (n - 1)):
        print "pols with k = ", i + 1, " is ", maslen[i]

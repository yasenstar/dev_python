# -*- coding: utf-8 -*-
"""
Find minimum LOSS
"""

repo = [0, 0, 1, 1, 1]

nbv3 = [341206.36, 341206.36, 348371.62, 348371.62, 348371.62]

vat = [0, 0, 0, 0, 0]

cost = [0, 0, 0, 37735.85, 3492.66]

fmv = [int(nbv3[0]), int(nbv3[1]), int(nbv3[2]), int(nbv3[3]), int(nbv3[4])]

loss = [0, 0, 0, 0, 0]

total_loss = 0
total_fmv = 0

# for i in range(len(repo)):
#     vat[i] = fmv[i]/1.03*0.02*1.12
#     loss[i] = nbv3[i]+cost[i]+vat[i]-fmv[i]
#     total_loss += loss[i]
#     total_fmv += fmv[i]
#     i += 1

set_total_fmv = 1350000

target_loss = set_total_fmv

fmv0 = fmv[0]
fmv1 = fmv[1]
fmv2 = fmv[2]
fmv3 = fmv[3]
fmv4 = fmv[4]

for i in range(fmv0):
    for j in range(fmv1):
        for x in range(fmv2):
            for y in range(fmv3):
                for z in range(fmv4):
                    for a in range(len(repo)):
                        vat[a] = fmv[a]/1.03*0.02*1.12
                        loss[a] = nbv3[a]+cost[a]+vat[a]-fmv[a]
                        total_fmv += fmv[a]
                        total_loss += loss[a]
                        if total_fmv == set_total_fmv:
                            if total_loss < target_loss:
                                target_loss = total_loss
                        a += 1
                    z += 1
                y += 1
            x += 1
        j += 1
    i += 1

print("fmv: ", fmv)
print("total minimum loss = ", total_loss)
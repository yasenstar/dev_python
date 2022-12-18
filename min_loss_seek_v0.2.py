# -*- coding: utf-8 -*-
"""
Find minimum LOSS

"""

repo = [0, 0, 1, 1, 1]

nbv3 = [341206.36, 341206.36, 348371.62, 348371.62, 348371.62]

vat = [0, 0, 0, 0, 0]

cost = [0, 0, 0, 37735.85, 3492.66]

fmv = [0, 0, 0, 0, 0]

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

# fmv[4] = set_total_fmv - fmv[0] - fmv[1] - fmv[2] - fmv[3]

target_loss = set_total_fmv

print("starting_fmv: ", fmv)



for i in range(int(nbv3[0]), 0, -5000):
    fmv[0] = i
    for j in range(int(nbv3[1]), 0, -5000):
        fmv[1] = j
        for x in range(0, int(nbv3[2]), 5000):
            fmv[2] = x
            for y in range(0, int(nbv3[3]), 5000):
                fmv[3] = y
                fmv[4] = set_total_fmv - fmv[0] - fmv[1] - fmv[2] - fmv[3]
                # print("fmv before: ", fmv)
                if fmv[4] <= nbv3[4]:
                    total_loss = 0
                    total_fmv = 0
                    # print(i, j, x, y)
                    for a in range(5):                    
                        vat[a] = fmv[a]/1.03*0.02*1.12*repo[a]
                        loss[a] = nbv3[a]+cost[a]+vat[a]-fmv[a]
                        total_fmv += fmv[a]
                        total_loss += loss[a]
                        a += 1
                    if total_loss <= target_loss:
                        target_loss = total_loss
                        check = "false"
                        print("fmv: ", fmv, "total loss=", total_loss)
                    else:
                        check = "true"     
    #             y += 1
    #         x += 1
    #     j += 1
    # i += 1

# print("fmv: ", fmv)
# print("total minimum loss = ", total_loss)

# v0.2:
#     - limit fmv[4] to have linkage to 1350000
# v0.1: due to too large loop, cannot complete calculating
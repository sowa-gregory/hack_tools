ALP1 = "ACD"
ALP2=  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for i in list(ALP1):
    for j in list(ALP2):
        for k in list (ALP2):
            print("$%s$%s$%s"%(i,j,k))

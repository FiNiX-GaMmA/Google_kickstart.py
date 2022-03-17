def candies(n,m,num):
    sum_ca = 0
    for i in num:
        sum_ca += int(i)
    div = sum_ca//int(m)
    leftcan = sum_ca-(int(m)*div)
    return int(leftcan)

test = int(input())
total_ans = []
for i in range(0,test):
    nandm_raw = input()
    nandm = nandm_raw.strip().split(" ")
    n = nandm[0]
    m = nandm[1]
    candies_raw = input()
    num_list = candies_raw.strip().split(" ")
    #print(num_list)
    #print(i)
    total_ans.append(candies(n,m,num_list))
for index,val in enumerate(total_ans):
    print("Case #{}: {}".format(index+1,str(val)))
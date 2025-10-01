in1 = input()
in2 = in1.split()
in3 = []
in3.append(int(in2[0]))
in3.append(int(in2[1]))

first = input()

ops = []
nums = []

for h in range (len(first)):
    if (h%2 == 0):
        nums.append(first[h])
    else:
        ops.append(first[h])


# evaluate first & print
res = int(eval(first))
print(res%1000000007)


# loop through inputs

for i in range (in3[1]):
    inn = input()
    if (len(ops) > 0):
        if (inn[0] == 's'):
            # swap two
            a = int(inn[2])
            b = int(inn[4])

            hold = nums[a-1]
            nums[a-1] = nums[b-1]
            nums[b-1] =  hold

        elif (inn[0] == 'f'):
            # flip one

            a = int(inn[2])
            if (ops[a-1] == '+'):
                ops[a-1] = '*'
            elif (ops[a-1] == '*'):
                ops[a-1] = '+'
        else:
            # flip all
            for c in range (len(ops)):
                if (ops[c] == '+'):
                    ops[c] = '*'
                elif (ops[c] == '*'):
                    ops[c] = '+'
 
    
    # evaluate 
    aa = len(ops) + len(nums)
    onN = 0
    onO = 0

    exp = ""
    for v in range (aa):
        if (v%2 == 0):
            exp = exp+nums[onN]
            onN+=1
        else:
            exp = exp+ops[onO]
            onO+=1
        
    res2 = int(eval(exp))
    print(res2%1000000007)
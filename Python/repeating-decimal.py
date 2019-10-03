## Given a fraction return the answer. If there are repeating decimals, they will be encapsulated in brackets
""" Idea: 
Check if den is 0
Check if num is 0 
Check if remainder is 0
Check if num if den is neg. 
Concatanate the remainder after a decimal place
"""


def finding_remainder(num, den):
    output = ""
    if den == 0:
        return 'Undefined'
    if num == 0:
        return '0'
    neg = False
    if (num * den) < 0:
        neg = True 
    if (num % den) == 0:
        return str(num/den)

    numerator = abs(num)
    denominator = abs(den)
    if neg == True: 
        output += "-"+str(numerator // denominator)
    else:
        output += str(numerator // denominator)
    output += "."
    num_q = []
    while True:
        remain = numerator % denominator
        if remain == 0: 
            for element in num_q:
                output += str(element[-1])
            break 
        numerator = 10 * remain 
        q = numerator // denominator

        if [numerator, q] not in num_q:
            num_q.append([numerator, q])
        elif [numerator,q] in num_q:
            inde = num_q.index([numerator, q])
            for element in num_q[:inde]:
                output += str(element[-1])

            output += "["
            for element in num_q[inde:]:
                output += str(element[-1])
            output += "]"
            break
    print(output)


finding_remainder(2,5)
finding_remainder(10,5)
finding_remainder(-67,5)
finding_remainder(1,3)
finding_remainder(22,7)

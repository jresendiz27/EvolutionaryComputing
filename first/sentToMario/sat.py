""" 3CV3
Boolean Satisfiability Problem (SAT)
Created on August 17th, 2014
Lopez Garduno Blanca Azucena
Resendiz Arteaga Juan Alberto
"""
def readFile():
    v = 0
    results = open('solutions.txt','w', encoding="utf-8")
    while True:
        file = open("expression.txt", "r", encoding="utf-8")
        vars = int(file.readline().strip())
        maxiterms = int(file.readline().strip())
        expression = ''
        variables = int2bin(v,vars)
        for i in range(maxiterms):
            expression += file.readline().strip().replace(' ',' and ').replace('0','not 1')
            list = expression.split(sep='1')
            exp = ''
            for j in range(0,len(list)-1):
                exp += variables[j%vars] + list[j+1]
            if((i+1) < maxiterms):
                expression += ' or '
        expression = exp.replace('and -1','').replace('and -0','')
        if(eval(expression) == 1):
            print("Values:",int2bin(v,vars)," F(x) = ",expression," = True")
            results = open('solutions.txt','a+', encoding="utf-8")
            results.write("Values:"+int2bin(v,vars)+" F(x) = "+expression+" = True\n")
        v += 1
        if(v >= (2** vars)):
            break
    
def int2bin(n, count):
    """returns the binary of integer n, using count number of digits"""
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])
    
readFile()
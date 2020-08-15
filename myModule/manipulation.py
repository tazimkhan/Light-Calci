response=['welcome the smart calculator','My name is light calci','thanks','sorry',"it's beyond my limit",'a is divisible by b','a is not divisible by b']
def extract_num_from_string(text):
    l=[]
    for x in text.split(' '):
        try:
            l.append(float(x))
        except:
            pass
    return l
def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def modula(a,b):
    return a%b
def square(a):
    return a**2
def cube(a):
    return a**3
def underroot(a):
    return a**0.5
def undercube(a):
    return a**0.33
def divisible():
    if a%b==0:
        return response[5]
    else:
        return response[6]
def lcm(a,b):
    z=a if a>b else b
    while z!=a*b:
        if z%a==0 and z%b==0:
            return z
            break
        z+=1
def hcf(a,b):
    z=a if a<b else b
    while z!=0:
        if a%z==0 and b%z==0:
            return z
            break
        z-=1
def end():
    print(response[2])
    print("please enter a key")
    exit()
def myname():
    print(reponse[1])
def sorry():
    print(response[3])
operation={'PLUS':add,'ADD':add,'SUM':add,'SUBMISSION':add,'ADDITION':add,'SUB':minus,'MINUS':minus,'SUBTRACTION':minus,'DIVIDE':divide,'DIVISION':divide,'DIVIDED':divide,
           'DIVISIBLITY':modula,'MODULE':modula,'MODULATION':modula,'REMAINDER':modula,'REMAIN':modula,'LCM':lcm,'LARGEST_COMMON_MULTIPLE':lcm,
           'HCF':hcf,'HIGHEST_COMMON_FACTOR':hcf,'GCD':hcf,'GRATEST_COMMON_DIVISION':hcf,'MULTIPLY':multiply,'MULTIPLICATION':multiply,'MUL':multiply,
           'CUBE':cube,'SQUARE':square,'UNDERROOT':underroot,'UNDERCUDE':undercube,'DIVISIBLE':divisible,'DIVISIBLITY_BY':divisible}
commands={'NAME':myname,'END':end,'EXIT':end,'CLOSE':end}

import sys 
sys.path.append('/myModule/')
import myModule
from myModule.manipulation import *
print(response[0])
print(response[1])
while True:
    print()
    text=input("enter the query")
    for word in text.split(' '):
        if word.upper() in operation.keys():
            try:
                l=extract_num_from_string(text)
                r=operation[word.upper()](l[0],l[1])
                print(r)
            except:
                print("something is wrong plz try again")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()

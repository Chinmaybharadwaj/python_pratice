"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Steps:
[X]:Taking user input
[X]:Filtering out the pair parantheses(filter-1)
[X]:Filtering phase two
[X]:Checking the validity of the expression
[X]:showing the result to user
""" 
main_list=[]

#function taking user input
def input_list_con():
    user_intput=input("Enter the string")
    for x in range(len(user_intput)):
        main_list.append(user_intput[x])

#fuction remove the pair values
def remove_pair():
    loop_boolean=True
    if main_list[0]==')':
        print("Invalid")
        loop_boolean=False
    while(loop_boolean):        
        for x in range(len(main_list)):
            if(len(main_list)<=0):
                loop_boolean=False
                print("list is empty")
                break
            if main_list[x]=='(':
                symbol_1_placeholder=x
                symbol_1_count=1           
            if main_list[x]==')' and symbol_1_count==1:
                symbol_2_placeholder=x
                if symbol_2_placeholder>symbol_1_placeholder:
                    del main_list[symbol_2_placeholder]
                    del main_list[symbol_1_placeholder]
                    symbol_1_count=0
                    if (len(main_list)==0):
                        print("Valid")
                        loop_boolean=False
                        break
                    break
            if x==len(main_list)-1:
                loop_boolean=False
#funtion to check the leftovers form the function 1
def second_filter():
    loop_boolean=True
    if len(main_list)>0 and main_list[0]==')':
        print("Invalid Expression")
        loop_boolean=False
    while(loop_boolean):
        symbol_12_count=0
        symbol_star_count=0
        symbol_12_placeholder=0
        symbol_star_placeholder=0
        if len(main_list)==0:
            print("valid")
            loop_boolean=False
            break
        for x in range(len(main_list)):
            if main_list[x]=='(' or main_list[x]==')':
                symbol_12_count=1
                symbol_12_placeholder=x
            if main_list[x]=='*':
                symbol_star_placeholder=x
                symbol_star_count=1
            if symbol_12_count==1 and symbol_star_count==1:
                if main_list[symbol_12_placeholder]=='(':
                    if symbol_star_placeholder > symbol_12_placeholder:
                        del main_list[symbol_star_placeholder]
                        del main_list[symbol_12_placeholder]
                        break
                if main_list[symbol_12_placeholder]==')':
                    if symbol_star_placeholder < symbol_12_placeholder:
                        del main_list[symbol_12_placeholder]
                        del main_list[symbol_star_placeholder]
                        break
            if x==len(main_list)-1:
                loop_boolean=False
def validate_list():
    if '(' in main_list or ')' in main_list:
        print("final validation failed not in the given format")   
    else:
        print("Entered expression is valid")                
            

#the program starts here       
input_list_con()
print("-----check-1-----") 
remove_pair()
print("-----check-2-----")
second_filter()
print("-----check-3-----")
print(main_list)
validate_list()
#End
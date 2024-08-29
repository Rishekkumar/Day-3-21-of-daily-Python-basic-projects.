import random
import time

operators=["+","-","*"]
min_value=2
max_value=12

while True:
    total_questions=input("enter how many question you want: ")
    
    if total_questions.isdigit():
        total_questions=int(total_questions)   
        if total_questions>0:
            break
        else:
            print("please enter a number above 0")
        
            
    else:
        print("please enter a number")
        continue
        
def generate_questions():
    left= random.randint(min_value,max_value)
    right= random.randint(min_value,max_value)
    operator= random.choice(operators)
    
    question= str(left)+" "+operator+" "+str(right)
    answer= eval(question)
    return question, answer
wrong=0
input("press enter to start: ")
print("--------------------------")
print("when you want to quit enter 'q'..\n")
print("--------------------------\n")
start_time= time.time()
for i in range(total_questions):
    question,answer=generate_questions()
    while True:
        user_input= input(f"#({i+1}).|  {question} = ")
        if user_input=="q"or "Q":
            print("quiting.....")
            quit()
        elif user_input== str(answer):
            break
        wrong+=1
end_time= time.time()
total_time= round(end_time-start_time,2)
right_ans=total_questions-wrong
print("--------------------------")

print(f"you got {right_ans} right in first attempt")  
print(f"you completed {total_questions} questions in {total_time} seconds..")

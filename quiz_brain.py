class QuizBrain:
    def __init__(self,q_list):
        self.question_no = 0
        self.question_list=q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.question_list)
    
    

    def next_question(self):
        self.question_no+=1
        current_question = self.question_list[self.question_no-1]
        user_ans = input(f"Q.{self.question_no}: {current_question.text} True/False ").lower()
        self.check_answer(user_ans,current_question.answer)


    def check_answer(self,user_answer,current_ans):
        if user_answer.lower() == current_ans.lower():
            print("Correct")
            self.score += 1
            
        
        else:
            print("Incorrect")
        
        print(f"your score is {self.score}/{self.question_no}")
        print(f"The correct answer is {current_ans}")
        print("\n"*2)

        



    

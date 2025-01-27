from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank=[]
for i in question_data:
    question_text=i["text"]
    question_answer=i["answer"]
    question = Question(question_text,question_answer)
    question_bank.append(question)
    


quizBrain = QuizBrain(question_bank)
while quizBrain.still_has_questions():
    quizBrain.next_question()

print("You have completed the quiz!!")
print(f"your final score: {quizBrain.score}/{quizBrain.question_no}")

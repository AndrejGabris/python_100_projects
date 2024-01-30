from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
from trivia_data import question_data

question_bank = []
for question in question_data:
    qeustion_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=qeustion_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

still_questions_in_databank = True
while still_questions_in_databank:
    quiz.next_question()
    still_questions_in_databank = quiz.still_has_question()

print("You have completed the quiz. No more questions in databank.")
print(f"Your final score was: {quiz.current_score}/{quiz.question_number}")

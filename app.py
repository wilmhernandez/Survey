from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

app.config["SECRET_KEY"] = "Let's GO"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

responses = []


@app.route('/')
def home():
    """Directs user to Homepage"""
    responses.clear()
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)

@app.route('/questions/<ques>')
def question(ques):
    """Directs user to questions of the questionnaire"""
    total_ques = len(satisfaction_survey.questions)
    display_num = int(ques) + 1
    ques = int(ques)
    q3_list = satisfaction_survey.questions[2].choices
    if int(ques) >= total_ques:
        return f"Please send request with and interger less than {total_ques} "
    else:
        question = satisfaction_survey.questions[ques].question
    return render_template('questions.html', display=display_num, question=question, ques=ques, list=q3_list)



# @app.route(f'/qustions/<ques>')
# def questions(ques):
#     if (responses == None):
#         return redirect("/")
    
#     if (len(responses) == len(satisfaction_survey.questions)):
#         return redirect("/thankyou")
    
#     if (len(responses) != ques):
#         flash('Please answer all questions in order')
#         redirect(f'/qustions/{len(responses)}')
        
#     question = satisfaction_survey.questions[ques].question
#     display_num = int(ques) + 1
#     q3_list = satisfaction_survey.questions[2].choices
#     return render_template('questions.html', display=display_num, question=question, ques=ques, list=q3_list)
    

@app.route("/answer", methods=["POST"])
def add_answer():
    """Adds user answer to responses list"""
    answer = request.form["option"]
    responses.append(answer)
    next_question_num = len(responses)
    if next_question_num < len(satisfaction_survey.questions):
        return redirect(f"/questions/{next_question_num}")
    else:
        return redirect("/thankyou")
    
    
@app.route("/thankyou")
def thank_you():
    """Thanks the user after completing the survey"""
    return render_template('thank_you.html', responses=responses)
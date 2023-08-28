from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

app.config["SECRET_KEY"] = "Let's GO"

debug = DebugToolbarExtension(app)

responses = []


@app.route('/')
def home():
    """Directs user to Homepage"""
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
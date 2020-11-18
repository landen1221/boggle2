from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, jsonify, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretKey"

boggle_game = Boggle()
word_dict = boggle_game.read_dict('words.txt')
words_found = []
tries = 0
score = 0
high_score = 0


@app.route('/')
def home_page():
    global high_score
    if tries == 0:
        setup_game()
    if session['score'] > high_score:
        session['high-score'] = session['score']
        high_score = session['score']
    print(session)
    return render_template('index.html', curr_game=session['curr_game'])


### Likely 
@app.route('/word-check', methods=['POST'])
def check_word_validity():
    curr_word = request.form['word']
    global tries
    tries += 1

    result = boggle_game.check_valid_word(session['curr_game'], curr_word)
    print(f'result pre-if statement {result}')
    if curr_word in words_found:
        flash("You've already found that word")

    elif result == 'ok':
        words_found.append(curr_word)
        session['found_words'] = words_found
        session['score'] += len(curr_word)
        print(f'result = {result}')
        print(f'length = {len(result)}')
        
    elif result == "not-on-board":
        flash("Your word is not in the board")
    
    elif result == "not-word":
        flash("Your word is not a valid word")
    else:
        flash("nothing entered")
    
    print(session)
    return redirect('/')

@app.route('/restart')
def restart_game():
    global tries, score, words_found
    tries = 0
    score = 0
    words_found = []
    
    return redirect('/')

def setup_game():
    curr_game = boggle_game.make_board()
    session['curr_game'] = curr_game
    words_found = []
    session['found_words'] = words_found
    session['score'] = score
    session['high-score'] = high_score
    
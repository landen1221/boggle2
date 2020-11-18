from boggle import Boggle
import json
from flask import Flask, request, render_template, redirect, flash, jsonify, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretKey"

boggle_game = Boggle()
word_dict = boggle_game.read_dict('words.txt')
words_found = []



@app.route('/')
def home_page():
    curr_game = boggle_game.make_board()
    session['curr_game'] = curr_game
    words_found = []
    session['found_words'] = words_found
    session['score'] = 0
   
        
    print(session)
    return render_template('index.html', curr_game=session['curr_game'])


### Likely 

@app.route('/check-word', methods=['POST'])
def check_word_validity():
    curr_word = request.json['word']

    result = boggle_game.check_valid_word(session['curr_game'], curr_word)
    
    if curr_word in words_found:
        session['message'] = "You've already found this word"
        result = 'not ok'

    elif result == 'ok':
        words_found.append(curr_word)
        session['found_words'] = words_found
        session['score'] += len(curr_word)
        session['message'] = 'Well Done!'
        print(f'result = {result}')
        print(f'length = {len(result)}')
        
    elif result == "not-on-board":
        # jsonify({'flash': "your "})
        session['message'] = "Your word is not in the board"
    
    elif result == "not-word":
        session['message'] = "Your word is not a valid word"
   
    if session['score'] > session['high-score']:
        session['high-score'] = session['score']
        

    print(session)
    return jsonify(result=result, message=session['message'], score=session['score'], highScore=session['high-score'])

@app.route('/restart')
def restart_game():
    global words_found
    words_found = []
    return redirect('/')

    
   
    
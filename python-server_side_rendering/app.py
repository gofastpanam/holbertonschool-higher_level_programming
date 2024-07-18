from flask import Flask, render_template
import json

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    data = read_json('items.json')
    items = data.get('items', [])
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)

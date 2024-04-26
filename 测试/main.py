from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# 读取敏感词文件
def load_sensitive_words():
    with open('1.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

sensitive_words = load_sensitive_words()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    text = request.form['text']
    found_words = [word for word in sensitive_words if word in text]
    return jsonify(found_words)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
from detector import analyze

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    reasons = []

    if request.method == 'POST':
        url = request.form['url']
        result, reasons = analyze(url)

    return render_template('index.html', result=result, reasons=reasons)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
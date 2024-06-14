from flask import Flask, render_template

app = Flask(__name__,static_url_path='/static')
@app.route('/about')
def home():
    return render_template('home.html')

@app.route('/recept')
def second():
    return render_template('second.html')

@app.route('/')
def go():
    return render_template('go.html')


if __name__ == '__main__':
    app.run(debug=True)
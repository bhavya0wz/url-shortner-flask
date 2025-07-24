from flask import Flask, request, render_template
import pyshorteners

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        long_url = request.form['long_url']
        try:
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(long_url)
        except Exception as e:
            short_url = f"Error: {e}"
    return render_template('index.html', short_url=short_url)

if __name__ == '__main__':
    app.run(debug=True)

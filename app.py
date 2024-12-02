from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize content with default text
content = "Welcome to the billboard!"

@app.route('/', methods=['GET', 'POST'])
def index():
    global content
    if request.method == 'POST':
        # Update the content with the text from the editor
        content = request.form.get('editor')
    return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)

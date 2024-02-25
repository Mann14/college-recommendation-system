from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_recommendation():
    # Logic to predict branch goes here
    branch = "cs"  # Example branch prediction
    return branch
@app.route('/graph')
def graph():
    return render_template('graph.html') 
@app.route('/')
def index():
    return redirect(url_for('show_form'))

@app.route('/form', methods=['GET', 'POST'])
def show_form():
    if request.method == 'POST':
        # Process form submission here
        # For now, let's just print the form data
        print(request.form)
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Process form data
    # Redirect to loading.html
    branch = get_recommendation()
    # Render HTML template based on branch recommendation
    template_path = f'recommends/{branch.lower()}.html'
    return render_template(template_path)


@app.route('/output')
def output():
    return render_template('recommends/cs.html')

if __name__ == '__main__':
    app.run(debug=True)


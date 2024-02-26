from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
app = Flask(__name__)
# mongo = PyMongo(app)
client= MongoClient("mongodb://127.0.0.1:27017/")
db = client['college_recommendation_system']
collection = db['registered_data']

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

def submit():
    if request.method == 'POST':
        # Extract form data
        full_name = request.form['Full_name']
        email = request.form['Email']
        family_income = int(request.form['Family_income'])
        higher_edu = request.form['higher_edu']
        branch = request.form.get('12th_branch') if '12th_branch' in request.form else None
        per_12 = int(request.form.get('per_12', 0))
        diploma_branch = request.form.get('diploma_branch') if 'diploma_branch' in request.form else None
        diploma_per = int(request.form.get('diploma_per', 0))
        jee_rank = int(request.form['jee_rank'])
        state = request.form['State']
        city = request.form['City']
        interests = request.form.getlist('interest')  # Get list of selected interests

        # Create a document to insert into MongoDB
        student_data = {
            'full_name': full_name,
            'email': email,
            'family_income': family_income,
            'higher_edu': higher_edu,
            'branch': branch,
            'per_12': per_12,
            'diploma_branch': diploma_branch,
            'diploma_per': diploma_per,
            'jee_rank': jee_rank,
            'state': state,
            'city': city,
            'interests': interests
        }

        # Insert the document into MongoDB
        collection.insert_one(student_data)

        print('Form data submitted successfully!')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Process form data
    # Redirect to loading.html
    submit()
    branch = get_recommendation()
    # Render HTML template based on branch recommendation
    template_path = f'recommends/{branch.lower()}.html'
    return render_template(template_path)


@app.route('/output')
def output():
    return render_template('recommends/cs.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, jsonify
from model import get_recommendation
from pymongo import MongoClient

app = Flask(__name__)
# mongo = PyMongo(app)
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client['college_recommendation_system']
collection = db['registered_data']

#def submit():
 #   if request.method == 'POST':
  #      #database
   #     print('Form data submitted successfully!')
    #    #user_interest = "string of interests"
     #   #user_rank
      #  #family_income
       # data = ["NLP, Big Data, App Development", 6789 , 100000]
        #return data
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Process form data
    rank = int(request.form.get('jee_rank'))
    income = float(request.form.get('Family_income'))
    interests = request.form.get('selected_interests')
    #course = request.form.get('interest')
    print(interests)
    selected_interests = interests if interests else ""
    print(selected_interests, rank, income)
    b1, b2, b3 = get_recommendation(selected_interests, rank, income)
    print(b1, b2, b3)
    b1 = b1.lower()

    template_path = f"recommends/{b1.lower()}.html"

    # Render HTML template based on branch recommendation
    return render_template(template_path, b1=b1, b2=b2, b3=b3)

# Call the function from model.py to predict top unique branches
@app.route('/submit_form_alternate', methods=['POST'])
def submit_form_alternate():
    selected_interests = request.form.getlist('interest')
    # Print the selected interests
    print("selected interests:", selected_interests)
    return selected_interests

#@app.route('/graph')
#def graph():
#    return render_template('graph.html') 

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

@app.route('/roadmap')
def roadmap():
    # Logic to fetch and process roadmap data
    # For example:
    branch = request.args.get('branch')
    roadmap_data = {
        'field': 'NLP',  # Example field
        'roadmap': 'Here is the roadmap for NLP...'  # Example roadmap content
    }
    return render_template(f'roadmaps/{branch}roadmap.html', roadmap_data=roadmap_data)
@app.route('/output')
def output():
    return render_template('recommends/cs.html')

@app.route('/agriculture')
def agriculture_page():
    return render_template('course_interests/agriculture.html')

@app.route('/administration')
def administration_page():
    return render_template('course_interests/administration.html')

@app.route('/computer_app')
def computer_app_page():
    return render_template('course_interests/computer_app.html')

@app.route('/finance')
def finance_page():
    return render_template('course_interests/finance.html')

@app.route('/pharmacology')
def pharmacology_page():
    return render_template('course_interests/pharmacology.html')

@app.route('/technology')
def technology_page():
    return render_template('course_interests/technology.html')

if __name__ == '__main__':
    app.run(debug=True)

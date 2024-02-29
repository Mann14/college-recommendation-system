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
    rank = int(request.form.get('jee_rank')) # type: ignore
    income = float(request.form.get('Family_income')) # type: ignore
    binterests = request.form.get('selected_interests')
    course = request.form.get('interests')
    print(binterests)
    selected_interests = binterests if binterests else ""
    print(selected_interests, rank, income)
    b1, b2, b3 = get_recommendation(selected_interests, rank, course)
    print(b1, b2, b3)
    b1 = b1.lower()

    template_path = f"recommends/{b1.lower()}.html"

    # Render HTML template based on branch recommendation
    return render_template('main.html', b1 = b1.upper(), b2 = b2.upper(), b3 = b3.upper())

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


@app.route('/display_content/<selected_branch>')
def display_content(selected_branch):
    return render_template('main.html', selected_branch=selected_branch)

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
# def submit():
#     if request.method == 'POST':
#         # Extract form data
#         full_name = request.form['Full_name']
#         email = request.form['Email']
#         family_income = int(request.form['Family_income'])
#         # higher_edu = request.form['higher_edu']
#         branch = request.form.get('branch_12') 
#         per_12 = request.form.get('per_12', 0)
#         try:
#             per_12_int = int(per_12)
#         except:
#             per_12_int = 0
#         # diploma_branch = request.form.get('diploma_branch') 
#         # diploma_per = request.form.get('diploma_per',0)
#         # try:
#         #     diploma_per_int = int(diploma_per)
#         # except:
#         #     diploma_per_int  = 0
#         jee_rank = request.form.get('jee_rank',0)
#         try:
#             jee_rank_int = int(jee_rank)
#         except:
#             jee_rank_int = 0
#         state = request.form['State']
#         city = request.form['City']
#         interests = request.form.getlist('interest')

#         # Create a document to insert into MongoDB
#         student_data = {
#             'full_name': full_name,
#             'email': email,
#             'family_income': family_income,
#             # 'higher_edu': higher_edu,
#             'branch': branch,
#             'per_12': per_12_int,
#             # 'diploma_branch': diploma_branch,
#             # 'diploma_per': diploma_per_int,
#             'jee_rank': jee_rank_int,
#             'state': state,
#             'city': city,
#             'interests': interests
#         }

#         # Insert the document into MongoDB
#         collection.insert_one(student_data)

#         print('Form data submitted successfully!')
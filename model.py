import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the data and train the model
data = pd.read_csv("static/BTech.csv")
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(data['Interest'])
X = data[["Interest", "Institute Name"]]
y = data["Branch"]
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_tfidf, y)
data['Closing Rank'] = pd.to_numeric(data['Closing Rank'], errors='coerce')

# Function to predict top unique branches
def predict_top_unique_branches(user_interest, user_rank, family_income, top_n=3):
    try:
        # Predict branch probabilities
        user_input_tfidf = tfidf_vectorizer.transform([user_interest])
        branch_probs = model.predict_proba(user_input_tfidf)

        # Get branch names and corresponding probabilities
        branch_names = model.classes_
        branch_probabilities = branch_probs[0]

        # Create a DataFrame for easy sorting
        result_df = pd.DataFrame({'Branch': branch_names, 'Probability': branch_probabilities})

        # Sort by probabilities in descending order
        result_df = result_df.sort_values(by='Probability', ascending=False)

        # Extract the predicted branch
        predicted_branch = result_df.iloc[0]['Branch']

        # Filter branches based on closing rank and family income
        closing_rank = data[data["Branch"] == predicted_branch]["Closing Rank"].values[0]
        rank_check = user_rank <= closing_rank

        result_df = result_df.merge(data[['Branch', 'Institute Name', 'Closing Rank', 'Fee Structure']], on='Branch')
        result_df = result_df[rank_check & (result_df['Fee Structure'] <= family_income)]

        # Get top N unique branches
        top_unique_branches = result_df['Branch'].unique()[:top_n]

        # Move 'CSE' to the last position if present
        if 'CSE' in top_unique_branches:
            top_unique_branches = [branch for branch in top_unique_branches if branch != 'CSE'] + ['CSE']

        return top_unique_branches
    except Exception as e:
        print("Error occurred during prediction:", str(e))
        return None

# Function to save the trained model
def save_model(model, filename):
    try:
        joblib.dump(model, filename)
        print("Model saved successfully as", filename)
    except Exception as e:
        print("Error occurred while saving the model:", str(e))

# Save the trained model
save_model(model, "rf_model.pkl")

# Function to load the saved model
def load_model(filename):
    try:
        loaded_model = joblib.load(filename)
        print("Model loaded successfully from", filename)
        return loaded_model
    except Exception as e:
        print("Error occurred while loading the model:", str(e))
        return None

# Load the saved model
loaded_model = load_model("rf_model.pkl")

# Function to get recommendation based on user input
def get_recommendation(user_interest, user_rank, family_income):
    print(user_interest, user_rank, family_income)    
    top_unique_branches = predict_top_unique_branches(user_interest, user_rank, family_income)
    return top_unique_branches

# Function to take user input and provide recommendation
#def user_input_and_recommendation():
    # Take user input
#    user_interest = str(input("Enter your area of interest: "))
#    user_rank = int(input("Enter your JEE rank: "))
#    family_income = int(input("Enter your family income: "))

    # Call get_recommendation function with user input
#    get_recommendation(loaded_model, user_interest, user_rank, family_income)

# Call the user_input_and_recommendation function
# user_input_and_recommendation()

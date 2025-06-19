PulsePro – Cardiovascular Risk Checker ��

PulsePro is a Python-based web application that evaluates cardiovascular health risk based on key vital signs and health indicators provided by the user. It provides a quick and easy way to check your cardiovascular risk level (Low, Medium, or High) through a web interface.

🔗 Project URL

GitHub Repository: https://github.com/YAJNAS-05/pulsepro-cv-risk

🔧 Tech Stack

Python 3

Flask – Backend web framework

HTML/CSS – Frontend UI

Pandas – Data manipulation

NumPy – Numerical operations

scikit-learn (optional) – For future ML integration

✅ Features

Accepts user input for vital signs and basic health data

Determines cardiovascular risk category

Web interface for user interaction

Easily extendable with ML models or more features

📁 Project Structure

pulsepro-cv-risk/
├── app.py                          # Main Flask application
├── Cardiovascular Health Checker.py   # Risk logic (to be modularized)
├── templates/
│   └── index.html                 # HTML user interface
├── static/                        # Optional static files (CSS/images)
└── requirements.txt               # Python dependencies

⚙️ Setup Instructions

1. Clone the Repository

git clone https://github.com/YAJNAS-05/pulsepro-cv-risk.git
cd pulsepro-cv-risk

2. Create a Virtual Environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

If requirements.txt is missing, generate it using:

pip freeze > requirements.txt

4. Run the Application

python app.py

Open your browser and go to:

http://127.0.0.1:5000/

🔮 Example Input

Enter values like:

Age: 45

Blood Pressure: 140

Cholesterol: 220

Blood Sugar: 1 (high)

Heart Rate: 85

Expected Output: Medium Risk (varies based on logic)

🔎 Usage Notes

Logic currently based on threshold-based conditions

Can be enhanced using ML models (Logistic Regression, Decision Trees)

Input validation and error handling recommended for production


⚠️ Disclaimer

This tool is for educational and prototyping purposes only. It does not provide medical diagnosis. Always consult with a licensed healthcare provider.

👨‍💼 Author

Maintained by YAJNAS-05

Feel free to fork, contribute, or open issues to improve the project! ✨


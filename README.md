# churn_prediction

---
##📊 Production-Ready Customer Churn Prediction System
An enterprise-grade, end-to-end machine learning application designed to predict telecom customer churn based on account usage, payment setups, and contract patterns. This system utilizes a unified scikit-learn pipeline deployed via a high-performance Flask REST API and served through an executive-level Streamlit SaaS Dashboard.
---

##🎯 Core System Goals & Objectives
The primary objective of this project is to bridge the gap between sandbox data science and production-level software engineering.

Prevent Train-Test Skew: Implement a completely unified machine learning pipeline (ColumnTransformer + RandomForestClassifier) ensuring that data preprocessing, handling of missing values, encoding, and scaling are applied identically during training and inference phases.

Provide Actionable Risk Intelligence: Deliver real-time, interpretable prediction metrics coupled with automated retention strategy triggers rather than raw binary data outputs.

Modular Component Isolation: Separate the project cleanly into structural layers: Data/Model Layer, Core Prediction Engine (Backend API), and Interactive Presentation Layer (Frontend UI).

---

##📈 Machine Learning Workflow (What We Have Done)

Robust Feature Selection & Extraction: Filtered the dense Telco dataset down to 6 highly interpretable features across continuous usage metrics (tenure, MonthlyCharges, TotalCharges) and operational structural components (Contract, InternetService, PaymentMethod).

Defensive Pipeline Engineering:

Numerical Pipeline: Handled missing/blank string data in TotalCharges dynamically via a statistical median SimpleImputer before mapping weights with a StandardScaler.

Categorical Pipeline: Used a structural OneHotEncoder configured with handle_unknown='ignore' to safely handle unexpected or unseen categories at inference time without breaking backend tasks.

Model Construction & Serialization: Trained a structured RandomForestClassifier (max depth constrained to 10 to optimize generalization capacity). Evaluated metrics via Confusion Matrices and Classification Reports before serializing the entire ecosystem into a single operational binary churn_pipeline.pkl.

---

##💼 Business Use Cases & Real-World Application

This customer intelligence infrastructure can be instantly adapted across consumer subscription operations:

Telecom & ISP Operations: Flag high-risk, contract-free fiber-optic subscribers to deploy automated promotional loyalty bundles before their monthly billing cycle ends.

SaaS B2B Enterprises: Monitor account tracking health metrics by substituting MonthlyCharges with platform licensing spends to gauge client health.

Fintech & Banking: Predict credit card or account abandonment rates by feeding customer interaction metrics through the Flask endpoint API.

---

##📂 Source Dataset Link

The system is trained using the industry-standard Kaggle Telco Customer Churn Dataset (IBM Analytics).

Dataset Download URL: IBM Telco Customer Churn Dataset via Kaggle

---

##💻 Technical Requirements

Ensure you are utilizing Python 3.9+ or Python 3.10+. The system relies on fixed structural versions to guarantee execution stability:

Plaintext
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.5.0
flask==3.0.3
streamlit==1.35.0
requests==2.32.3
joblib==1.4.2
🚀 Execution & Running Instructions
Follow these steps exactly to execute the full architecture locally. Ensure your dataset is saved to your absolute path I:\amzon-project\churn_prediction_2\data\churn.csv.

Step 1: Project Environment Setup
Open your terminal inside the project root folder (churn-project/) and install the necessary dependencies:

Bash
pip install -r requirements.txt
Step 2: Compile & Train the Machine Learning Pipeline
Run the compiled training matrix to run feature cleaning, validate metrics, and save the serialized model pipeline:

Bash
python model/train.py
Expected Outcome: You will see the Confusion Matrix and Classification Report logged to the terminal, and a new churn_pipeline.pkl generated within the model/ subdirectory.

Step 3: Launch the Core Prediction Engine (Flask API)
Spin up the backend REST API to start listening for inbound JSON customer data payloads:

Bash
python api/app.py
Expected Outcome: The console will notify you that the microservice is running and actively listening on port 5000 (http://127.0.0.1:5000). Keep this terminal open.
---

Step 4: Boot up the Executive SaaS Interface (Streamlit)
Open a new, separate terminal window or tab, navigate back to your project directory, and start the frontend layout:

Bash
streamlit run frontend/ui.py
Expected Outcome: Your system will automatically open a local web browser window at http://localhost:8501, displaying your live operational Customer Churn Analytics Dashboard. Adjust fields and click evaluate to trace production pipeline predictions instantly.

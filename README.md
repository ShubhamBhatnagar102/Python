# Python
->run these commands before running code to install these dependencies
    pip install streamlit genai
    pip install -U google-genai
->to run the app
  open the terminal in the directory containing the app
command : streamlit run app.py


Description : the apps allows you upload a .csv file. and also a query in plain english abt the data.
the app uses gemini-3.8-flash model and client.interactions free tier api to generate plaintext responses.
Due to constrainst in using free api, the code automatically reduces the no of rows of .csv file to a maximun of 500 rows selected randomly.
Also the code drops any rows with any NULL values.
The app uses streamlit to create a minimal frontend.

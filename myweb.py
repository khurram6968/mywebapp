import streamlit as st
from PIL import Image

# Sidebar Configuration
st.sidebar.title("Navigation")
options = ["Home", "Experience", "Education", "Skills", "Projects"]
selection = st.sidebar.radio("Go to", options)

# Home Section
if selection == "Home":
    st.title("Mohd Khurram - Data Analyst")
    st.write(""" 
    Experienced Data Analyst with expertise in statistical analysis, machine learning, and data visualization.
    Proficient in Python, R, SQL, and Power BI, with a strong academic background in statistics.
    """)
    
    st.write("Contact Information:")
    st.write("- **Email:** khurramdocument@gmail.com")
    st.write("- **Phone:** +91-8439723802")
    st.write("- **Location:** Bulandshahr, India")

# Experience Section
elif selection == "Experience":
    st.title("Experience")
    st.subheader("Data Science Intern | Oasis Infobyte")
    st.write("**October 2024 - October 2024 | Remote**")
    st.write("- Enhanced spam mail filtering systems using NLP techniques in Python.")
    st.write("- Improved car sales prediction accuracy with random forest models.")
    st.write("- Visualized unemployment trends during the lockdown using Power BI.")
    st.write("- Forecasted sales with advanced data analysis techniques.")

    st.subheader("Data Analytics Intern | MedTourEasy")
    st.write("**October 2024 - October 2024 | Remote**")
    st.write("- Developed analytical tools and methodologies under mentorship.")
    st.write("- Analyzed age differences between right-handers and left-handers using Python.")

    st.subheader("Subject Matter Expert | DGx Creators")
    st.write("**October 2024 - Present | Remote**")
    st.write("- Provided solutions using statistical methods such as Linear Regression and Hypothesis Testing.")
    st.write("- Delivered data analysis using Python, R, SPSS, and Minitab.")

    st.subheader("Other Roles")
    st.write("- **Subject Matter Expert | Trivium Education Services (September 2023 - October 2024)**")
    st.write("- **Subject Matter Expert | Chegg India (September 2019 - December 2022)**")

# Education Section
elif selection == "Education":
    st.title("Education")
    st.subheader("M.Sc in Statistics")
    st.write("**Aligarh Muslim University | August 2019**")
    
    st.subheader("B.Sc in Statistics")
    st.write("**Aligarh Muslim University | August 2017**")

# Skills Section
elif selection == "Skills":
    st.title("Skills")
    st.write("### Technical Skills")
    st.write("- **Programming:** Python, R, SQL")
    st.write("- **Tools:** Power BI, SPSS, Minitab")
    st.write("- **Machine Learning:** Statistical Analysis, NLP, Random Forest Models")
    st.write("- **Data Visualization:** Creating interactive dashboards and visualizations")

    st.write("### Soft Skills")
    st.write("- Analytical Thinking")
    st.write("- Time Management")
    st.write("- Attention to Detail")
    st.write("- Problem Solving")

# Projects Section
elif selection == "Projects":
    st.title("Projects")
    st.subheader("Spam Filtering System")
    st.write("- Enhanced spam mail filtering using NLP techniques in Python.")

    st.subheader("Car Sales Prediction")
    st.write("- Improved predictive accuracy using Random Forest algorithms.")

    st.subheader("Unemployment Trend Analysis")
    st.write("- Visualized unemployment trends during the lockdown period using Power BI.")

    st.subheader("Age Difference Analysis")
    st.write("- Analyzed death age differences between right-handers and left-handers using Python.")

st.sidebar.info("Created by Khurram")

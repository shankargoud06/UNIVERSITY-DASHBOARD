import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data_path = "university_student_dashboard_data.csv"
data = pd.read_csv(data_path)

# Create derived columns
data['Year-Term'] = data['Year'].astype(str) + ' ' + data['Term']
data['Admission Rate (%)'] = (data['Admitted'] / data['Applications']) * 100
data['Enrollment Rate (%)'] = (data['Enrolled'] / data['Admitted']) * 100

# Streamlit app
st.set_page_config(layout="wide", page_title="University Admissions Dashboard")
st.title("📊 University Admissions & Student Satisfaction Dashboard")

# Metrics overview
st.subheader("Overall Admissions Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Applications", data["Applications"].sum())
col2.metric("Total Admitted", data["Admitted"].sum())
col3.metric("Total Enrolled", data["Enrolled"].sum())

# Retention rate trends
st.subheader("📈 Retention Rate Trends Over Time")
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(x='Year-Term', y='Retention Rate (%)', data=data, marker='o', color='purple')
plt.xticks(rotation=45)
plt.ylabel("Retention Rate (%)")
plt.xlabel("Year-Term")
plt.grid(True)
st.pyplot(fig)

# Student satisfaction trends
st.subheader("😊 Student Satisfaction Over the Years")
fig, ax = plt.subplots(figsize=(12, 5))
sns.barplot(x='Year-Term', y='Student Satisfaction (%)', data=data, palette='Greens')
plt.xticks(rotation=45)
plt.ylabel("Satisfaction (%)")
st.pyplot(fig)

# Enrollment by department
st.subheader("🏛️ Enrollment Trends by Department")
data_melted = data.melt(id_vars='Year-Term', value_vars=['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled'], var_name='Department', value_name='Enrollment')
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(x='Year-Term', y='Enrollment', hue='Department', data=data_melted, marker='o')
plt.xticks(rotation=45)
st.pyplot(fig)

# Spring vs. Fall Enrollment Comparison
st.subheader("🍂📅 Spring vs. Fall Enrollment Trends")
spring_data = data[data['Term'] == 'Spring']
fall_data = data[data['Term'] == 'Fall']
fig, ax = plt.subplots(figsize=(12, 5))
plt.plot(spring_data['Year'], spring_data['Enrolled'], label='Spring Enrollment', marker='o')
plt.plot(fall_data['Year'], fall_data['Enrolled'], label='Fall Enrollment', marker='s')
plt.legend()
plt.xlabel("Year")
plt.ylabel("Enrolled Students")
st.pyplot(fig)

st.write("### Key Insights:")
st.markdown("- **Retention Rates**: Monitoring the trend helps in identifying areas for student support.")
st.markdown("- **Student Satisfaction**: A key indicator of the university's academic and social environment.")
st.markdown("- **Department Enrollment Trends**: Helps in understanding which programs attract more students.")
st.markdown("- **Spring vs. Fall Comparison**: Shows which term is more popular for admissions.")


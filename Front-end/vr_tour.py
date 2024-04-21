import streamlit as st
import pandas as pd
import io
import base64
import matplotlib.pyplot as plt

# Define a function to create a fitness measurement dashboard
def show():
    st.title('VR Tour')

    iframe_code = """
       <iframe width="100%" height="400" src="https://sketchfab.com/models/e086183da4854416a606dc4f3bbea3ae/embed" frameborder="0" allow="autoplay; fullscreen; mixer; vr" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
     """

    st.markdown(iframe_code, unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")




    import random
    import time
    import plotly.express as px

# Set up the Streamlit app
    st.subheader("Heart Rate Visibility Dashboard")

# Create a random dataset
    factors = ['HRV', 'Frequency Assisted Therapy', 'Oligofactory Senses and Input', 'Blood Pressure and Oxygen Monitoring', 'Pulse vs HRV Stress Levels']
    data = {'Date': [], 'HRV': [], 'Frequency Assisted Therapy': [], 'Oligofactory Senses and Input': [], 'Blood Pressure and Oxygen Monitoring': [], 'Pulse vs HRV Stress Levels': []}
    for i in range(100):
        data['Date'].append(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
        data['HRV'].append(random.randint(0, 100))
        data['Frequency Assisted Therapy'].append(random.randint(0, 100))
        data['Oligofactory Senses and Input'].append(random.randint(0, 100))
        data['Blood Pressure and Oxygen Monitoring'].append(random.randint(0, 100))
        data['Pulse vs HRV Stress Levels'].append(random.randint(0, 100))
    df = pd.DataFrame(data)

# Display the graph
    fig = px.line(df, x='Date', y=factors)
    fig.update_layout(
        title='Heart Rate Visibility Dashboard',
        xaxis_title='Date',
        yaxis_title='Value',
        legend_title='Factors'
)
   
    fitness_data = {
        'Measurement': [
            'HRV (Heart Rate Visibility)',
            'Frequency Assisted Therapy',
            'Oligofactory Senses and Input',
            'Blood Pressure',
            'Oxygen Monitoring',
            'Pulse vs HRV Stress Levels'
        ],
        'Before': [70, 2, 1, '130/85', 95, 5],
        'After': [75, 3, 2, '120/80', 98, 4]
    }

    # Calculate improvements
    fitness_data['Improvement'] = [
        fitness_data['After'][i] - fitness_data['Before'][i]
        if isinstance(fitness_data['Before'][i], int) else 0
        for i in range(len(fitness_data['Measurement']))
    ]

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(fitness_data)

    # Function to apply color coding to improvements
    def color_improvement(value):
        if isinstance(value, int) and value > 0:
            return "color: green; font-weight: bold; font-size: 1.1em;"
        elif isinstance(value, int) and value < 0:
            return "color: red; font-weight: bold; font-size: 1.1em;"
        else:
            return "color: black;"

    # Create a downloadable Excel file
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Fitness Measurements', index=False)
    writer.save()
    output.seek(0)

    # Function to create a download link for the Excel file
    def get_download_link(file):
        href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{base64.b64encode(file.read()).decode()}" download="fitness_measurements.xlsx">Download Excel file</a>'
        return href

    # Divide the page into two columns
    col1, col2 = st.columns(2)

    # Display the DataFrame as a table with color-coded improvements in the left column
    with col1:
        st.dataframe(df.style.applymap(color_improvement, subset=['Improvement']))

    # Add a download button for the Excel file and a graph of improvements in the right column
    with col2:
        st.markdown(get_download_link(output), unsafe_allow_html=True)

        # Plot the improvements graph
        fig, ax = plt.subplots()
        ax.bar(df['Measurement'], df['Improvement'], color=['green' if x > 0 else 'red' for x in df['Improvement']])
        plt.xticks(rotation=45, ha='right')
        plt.ylabel('Improvement')
        plt.title('Improvements in Fitness Measurements')
        st.pyplot(fig)




    
   
import streamlit 

streamlit.title('MY NEW DIET PLAN')

streamlit.header('🥣 🥗 🐔 🥑🍞')
streamlit.text('MILLET')
streamlit.text('VEGETABLES & FRUITS')
streamlit.text('CERELS & PULSES ')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)









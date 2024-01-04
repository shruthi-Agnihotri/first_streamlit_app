import streamlit 

streamlit.title('MY NEW DIET PLAN')

streamlit.header('🥣 🥗 🐔 🥑🍞')
streamlit.text('MILLET')
streamlit.text('VEGETABLES & FRUITS')
streamlit.text('CERELS & PULSES ')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.


streamlit.multiselect("Pick some fruits:", list(my_fruit_list.Fruit))

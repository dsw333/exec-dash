# dashboard_generator.py

print("-----------------------")
print("MONTH: April 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("PLEASE BE PATIENT")

print("-----------------------")
print("THIS WILL SHOW TOP SELLING PRODUCTS")
print(" IF YOU GET AN ERROR TRY YOUR CSV FILE")


print("-----------------------")
print("VISUALIZING THE DATA...")


#Total monthly sales for the business, equivalent to the sum of total monthly sales for each product, formatted as USD with a dollar sign and two decimal places 
#A list of the top selling products, and total monthly sales for each, formatted as USD with a dollar sign and two decimal places
#At least one chart or graph depicting this or related information to support the project objectives. Chart titles should include a human-friendly textual representation of the selected month and year 



import pandas as pd
url = 'https://raw.githubusercontent.com/dsw333/exec-dash/master/sales-201904.csv'
df = pd.read_csv(url, error_bad_lines=False)
import plotly.express as px
#df = pd.read_csv("sales-201904.csv")
fig = px.bar(df, x = 'sales price', y = 'product', labels = {'sales price':'Sales (USD)'} , orientation = 'h', title = "Top Selling Products April 19")
fig.update_traces(texttemplate = 'sales price', textposition = 'outside')
fig.show()



#Include Total Amount
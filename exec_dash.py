# dashboard_generator.py

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

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
fig = px.bar(df, x = 'sales price', y = 'product', orientation = 'h', title = "Top Selling Products April 19")

fig.show()


#Make horizontal
#Add title
#Capitalize axis
#Include Total Amount
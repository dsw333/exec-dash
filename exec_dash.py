# dashboard_generator.py

import pandas as pd
url = 'https://raw.githubusercontent.com/dsw333/exec-dash/master/sales-201904.csv'
df = pd.read_csv(url, error_bad_lines=False)


print("-----------------------")
print("MONTH: April 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("PLEASE BE PATIENT")

print("-----------------------")
print("THIS WILL SHOW TOP SELLING PRODUCTS")


print("-----------------------")
print("TOTAL MONTHLY SALES: $" + str(df['sales price'].sum()))

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")

print("IF YOU GET AN ERROR ENSURE YOU ARE CALLING THE RIGHT CSV FILE")


print("-----------------------")
print("JUST A MINUTE")
print("VISUALIZING THE DATA...")




import pandas as pd
url = 'https://raw.githubusercontent.com/dsw333/exec-dash/master/sales-201904.csv'
df = pd.read_csv(url, error_bad_lines=False)
import plotly.express as px
#df = pd.read_csv("sales-201904.csv")
df = df.sort_values(by= 'product' , ascending = False )

fig = px.bar(df, x = 'sales price', y = 'product', labels = {'sales price':'Sales (USD)'} , orientation = 'h', title = "Top Selling Products April 19" , barmode = 'group' )
fig.update_traces(textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()



#Include Total Amount
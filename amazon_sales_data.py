import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("amazon_sales_data 2025.csv")

def pay_method():
    print("When you close the tab for the first graph then another will pop up. ")
    df = pd.read_csv("amazon_sales_data 2025.csv")

    pay = df.groupby("Payment Method")["Total Sales"].sum()
    pay.plot(kind="bar", title = "Payment methods", xlabel = "Payment types", ylabel = "amount")
    plt.show()

    pay.plot(kind="pie", title="Payment methods income", xlabel = "Payment types", ylabel = "", autopct="%1.1f%%")
    plt.show()
    menu()



def product():
    print("When you close the tab for the first graph then another will pop up. ")
    df = pd.read_csv("amazon_sales_data 2025.csv")
    product_sales = df.groupby("Product")["Total Sales"].sum()
    product_sales.plot(kind="pie", title = "Product sales data", xlabel = "product", ylabel = "", autopct="%1.1f%%" )
    plt.show()

    product_sales.plot(kind="bar", title = "Product sales data", xlabel = "product", ylabel = "" )
    plt.show()
    menu()

def category():
    print("When you close the tab for the first graph then another will pop up. ")
    df = pd.read_csv("amazon_sales_data 2025.csv")
    category_sales = df.groupby("Category")["Total Sales"].sum()
    category_sales.plot(kind="pie", title = "Category sales data", xlabel = "Category", ylabel = "", autopct="%1.1f%%" )
    plt.show()

    category_sales.plot(kind="bar", title = "Category sales data", xlabel = "Category", ylabel = "" )
    plt.show()
    menu()

def income():
    df = pd.read_csv("amazon_sales_data 2025.csv")
    sales = df.groupby("Date")["Total Sales"].sum()
    sales.plot(kind="line", title = "Total sales data", xlabel = "Sales", ylabel = "" )
    plt.show()
    menu()

    


def menu():
    choice = input("Would you like to view:\na. Pay method data\nb. Product sales data\nc. Category sales data\nd. Total income by sales\ne. Exit ")
    if choice == "a":
        pay_method()

    elif choice == "b":
        product()

    elif choice == "c":
        category()

    elif choice == "d":
        income()

    elif choice == "e":
        print("Goodbye")

    else:
        print("Invalid, try again")
        while True:
            choice = input("Would you like to view:\na. Pay method data\nb. Product sales data\nc. Category sales data\nd. Total income by sales\ne. Exit ")

        
menu()
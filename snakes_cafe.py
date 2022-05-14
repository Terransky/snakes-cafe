
menu = ["Wings", "Cookies", "Spring Rolls",
        "Salmon", "Steak", "Meat Tornado", "A Literal Garden",
        "Ice Cream", "Cake", "Pie",
        "Coffee", "Tea", "Unicorn Tears"]

print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type 'quit' **
**************************************""")

print(f"""\n
Appetizers
----------
{menu[0]}
{menu[1]}
{menu[2]}""")

print(f"""\n
Entrees
----------
{menu[3]}
{menu[4]}
{menu[5]}
{menu[6]}""")

print(f"""\n
Desserts
----------
{menu[7]}
{menu[8]}
{menu[9]}""")

print(f"""\n
Drinks
----------
{menu[10]}
{menu[11]}
{menu[12]}""")

print("""\n
***********************************
** What would you like to order? **
***********************************""")

customer_order = []


def ordering():
    order = ""

    while order != "Quit":
        order = input("> ").title()

        if order in menu:
            customer_order.append(order)
            print(f"** {customer_order.count(order)} order of {order} have been added to your meal **")

        else:
            print("** Please select something from the menu or type: 'quit' **")


ordering()

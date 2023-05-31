from flask import render_template
from app import app
from models.Game_shop import orders

@app.route("/")
def index():
    return render_template("index.html", title="Game Shop")

@app.route("/orders")
def order_list():
    return render_template("index.html", orders=orders)

@app.route("/orders/<index>")
def single_order(index):
    selected_order = orders[int(index)]

    return render_template("order.html", order=selected_order)



# # @app.route("/orders/<order>")
# # def show_task(order):
# #     return render_template("order.html", item=orders[int(order)])

# @app.route("/orders/<order>")
# def show_task(order):
#     return render_template("order.html", item=orders[int(order)])
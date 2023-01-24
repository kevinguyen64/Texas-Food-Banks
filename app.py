from cs50 import SQL
from flask import Flask, render_template, request, flash
from flask_session import Session

app = Flask(__name__)

db = SQL("sqlite:///food_bank.db")

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/bank", methods=["GET", "POST"])
def bank():
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")

    food_bank = db.execute("SELECT * FROM food_banks WHERE id = ?", id)
    name = food_bank[0]['name']
    image = food_bank[0]['image']
    about = food_bank[0]['about']
    address = food_bank[0]['address']
    phone_number = food_bank[0]['phone_number']
    website = food_bank[0]['website']
    counties = db.execute("SELECT * FROM counties WHERE food_bank_id = ?", id)

    return render_template("bank.html", name=name, image=image, about=about, address=address, phone_number=phone_number, website=website, counties=counties)


@app.route("/search")
def search():
    search_bank = request.args.get("search1")

    if search_bank == "":
        return render_template("failure.html", search_bank=search_bank)

    food_bank = db.execute("SELECT * FROM food_banks WHERE name LIKE ?", '%' + search_bank + '%')

    if food_bank:
        name = food_bank[0]['name']
        image = food_bank[0]['image']
        about = food_bank[0]['about']
        address = food_bank[0]['address']
        phone_number = food_bank[0]['phone_number']
        website = food_bank[0]['website']
        counties = db.execute("SELECT * FROM counties WHERE food_bank_id IN (SELECT id FROM food_banks WHERE name = ?)", food_bank[0]['name'])
    else:
        return render_template("failure.html", search_bank=search_bank)

    return render_template("bank.html", name=name, image=image, about=about, address=address, phone_number=phone_number, website=website, counties=counties)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        message = request.form.get('message')

        with open("message.csv", "a") as file:
            file.write(f"{message}\n\n")

        flash("Message sent!")

        return render_template("contact.html")
    else:
        return render_template("contact.html")


if __name__ == "__main__":
    app.run()
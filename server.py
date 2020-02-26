from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/")
def display():
  with open("restaurants.txt", "r") as f:
      content = f.read()
  return render_template("index.html", content=content)

if __name__ == "__main__":
  app.run(debug=True)
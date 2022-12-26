from flask import Flask,render_template

app=Flask(__name__)

days=["monday","tuesday","wednesday","thursday","friday","saturday"]

@app.route('/')
def hello_world():
    return render_template("index.html",data=days)

if __name__=='__main__':
    app.run(debug=True)









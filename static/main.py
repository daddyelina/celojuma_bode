from flask import Flask, render_template



app = Flask('app')

@app.route('/')
def Index_page():
    return render_template('amen.html')



if __name__ ==  '__main__':
    app.run(threaded = True, port=5000)  
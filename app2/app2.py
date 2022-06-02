#!/usr/bin/env python3


from flask import Flask, render_template, request

app = Flask(__name__)

farbe = "000000"


@app.route('/', methods=['GET', 'POST'])
def main():
    print(farbe)
    if request.method == 'POST':
        data = request.form
        print(data)
        print(request.form['farbe'])

    return render_template('test.html', farbe = farbe)




 
@app.route('/')
def main2():
    data = request.form
    print(data)
    print(request.form['farbe'])
    return render_template('test.html')
    





if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')





from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)

#home page
@app.route('/')
def home():
    return render_template ('index.html' )

#about page
@app.route('/about', methods =['POST', 'GET']) 
def about():
    return render_template ('about.html' )
       
#servuces page
@app.route('/services', methods = ['GET', 'POST']) 
def services():
    return render_template('services.html')
 
#gallery page 
@app.route('/gallery') 
def gallery():
    return render_template ('gallery.html' )
       
#contact page
@app.route('/contact', methods = ['GET', 'POST']) 
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
   
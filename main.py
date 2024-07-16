### Integrate HTML with flask
### HTTP verb get and post


### Jinja2 template
'''
{%...%} for statements.conditions, forloops
{{}} expressions to print output
{#...#} this is for comments
'''

from flask import Flask, redirect,url_for, render_template, request

# create my Flask application
app=Flask(__name__) 

# msg='welcome to my youtube channel '
# print(msg)
# print('please subscribe')

@app.route('/')
def welcome():
    return render_template('index.html') # every time we create a route, we must return


@app.route('/success/<int:score>') # pass a score along with an url, by default its str
def success(score):
    if score>=50:
        res='PASS'
    else: res='FAIL' 
    exp={'score':score,'res':res}
    return render_template('results.html',result=exp) # parameter name must be the same as the one in HMTL

@app.route('/fail/<int:score>') # pass a score along with an url, by default its str
def fail(score):
    return " the person has failed with score is " +str(score)


#result checker
@app.route('/results/<int:marks>') # pass a score ,redirect to other url
def results(marks):
    result=''
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

#Resultchecker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science']) #name in html, by default it is str
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4.0
    res=''
    if total_score>=50:
        res='success'
    else:
        res='fail'
    return redirect(url_for('success',score=total_score))
    
    
if __name__=='__main__': #starting point of program execution. 
    app.run(debug=True)
    
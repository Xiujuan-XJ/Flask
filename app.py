from flask import Flask,redirect,url_for
app=Flask(__name__) # create my app name

# msg='welcome to my youtube channel '
# print(msg)
# print('please subscribe')

@app.route('/')
def welcome():
    return 'welcome to my youtube channel, \nplease subscribe it, '

@app.route('/members')
def welcome_members():
    return 'welcome to my youtube channel for members '


@app.route('/success/<int:score>') # pass a score along with an url, by default its str
def success(score):
    return " the person has passed with score is " +str(score)

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
    

if __name__=='__main__': #starting point of program execution. 
    app.run(debug=True)
    
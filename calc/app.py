# Put your app in here.
from flask inport Flask, request
@app.route('/add')
def add_num():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    result= add(a,b)
    result=str(result)
    return result
@app.route('/sub')
def sub_num():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    result= sub(a,b)
    result=str(result)
    return result
@app.route('/mult')
def mult_num():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    result= mult(a,b)
    result=str(result)
    return result
@app.route('/div')
def div_num():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    result= div(a,b)
    result=str(result)
    return result
@app.route('/math/<operation>')
def do_cal(operation):
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    if operation == 'add':
        result =add(a,b)
    elif operation == 'sub':
        result=sub(a,b) 
    elif operation == 'mult':
        result=mult(a,b)
    elif operation == 'div':
        result=div(a,b)
    return str(result) 

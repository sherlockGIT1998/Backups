from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/metric/<stud_name>')
def SSC(stud_name):
    
    print(f'Calling {stud_name}')
    return f'Calling {stud_name}'

@app.route('/postmatrid/<Standard>')
def HSSC(Standard):
    
    print(f'Welcome guest : {Standard}')
    return f'Welcome guest : {Standard}'

@app.route('/user/<name>')
def user(name):
    
    if name == 'SSC':   
        print('Calling SSC function')
        return redirect(url_for('SSC',stud_name = name))
    
    else:
        print('Calling HSSC Function')
        return redirect(url_for('HSSC',Standard = name))
        
    
if __name__ == '__main__':
    app.run(host='127.0.0.1' , port = 5000 ,debug = True)
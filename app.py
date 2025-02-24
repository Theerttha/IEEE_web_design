from flask import Flask, render_template, url_for, request, redirect,session
app = Flask(__name__)
def request_func(nav):
    if(nav=="1"):
        return redirect(url_for('index'))
    elif nav=="2":
        return redirect(url_for('list_team'))
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        nav=request.form['nav']
        return request_func(nav)
        
@app.route('/members', methods=['POST', 'GET'])
def members(ind):

    if request.method == 'GET':
        return 2
    if request.method == 'POST':
        nav=request.form.get('nav')
        return request_func(nav)
@app.route('/list_members', methods=['POST', 'GET'])
def list_team():
    if request.method == 'GET':
        members=[["Irin Maria","Chairperson","3","ECE"],["K Srihari","Secretary","2","EEE"]]
        return render_template('list_members.html',members=members)
    if request.method == 'POST':
        nav=request.form.get('nav')
        if nav is not None:
            return request_func(nav)
        table=request.form.get('members')
        if(table is not None):
            ind=int(table)
            member_data=[["Irin Maria","Chairperson","3rd Year","ECE","Field of interest","linkedin link","img_link.webp"],["K Srihari","Secretary","2nd Year","EEE","Field of interest","linkedin link","img_link.webp"]]
            return render_template('members.html',member=member_data[ind-1],img=member_data[ind-1][-1])
        
            
if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, url_for, request, redirect,session
from flask_session import Session
app = Flask(__name__)
app.config['SECRET KEY']="IEEE"
app.config['SESSION_TYPE'] = 'filesystem'
sess = Session()
sess.init_app(app)
def request_func(nav):
    if(nav=="1"):
        return redirect(url_for('index'))
    elif nav=="2":
        return redirect(url_for('list_team'))
    elif nav=="3":
        session['year']=[]
        return redirect(url_for('events_list'))
    elif nav=="4":
        return redirect(url_for('about'))
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        notifications=[["Notification 1,content"],["Notification 2,content"],["Notification 3,content"]]
        img_notification=["img_notification.jpg","img_notification.jpg","img_notification.jpg"]
        return render_template('index.html',notifications=notifications[:-1],img_notification=img_notification[-1])
    if request.method == 'POST':
        nav=request.form.get("nav")
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
            return render_template('members.html',member=member_data[ind-1][:-1],img=member_data[ind-1][-1])
        
@app.route('/events_list', methods=['POST', 'GET'])      
def events_list():
    d={2025:[],2024:["ELECTRIFY","CIRCUITEX 2.0"],2023:[], 2022:[]}
    if request.method=="GET":
        if 'year' not in session:
            session['year']=[]
        
        return render_template("events_list.html",year=session['year'],data=d) 
    if request.method=="POST":
        nav=request.form.get('nav')
        if nav is not None:
            return request_func(nav)
        events_list=request.form.get('events_list')
        if events_list is not None:
            events_list=int(events_list)
            year=session['year']
            session.pop('year')
            if events_list not in year:
                year.append((events_list))
            else:
                year.remove((events_list))
            session['year']=year
            return render_template("events_list.html",year=session['year'],data=d)
        event_data=request.form.get('event_data')
        if event_data is not None:
            html=""
            for i in event_data:
                if i==",":
                    html+="_"
                else:
                    html+=i
            html+=".html"
            return render_template(html)
@app.route('/about', methods=['POST', 'GET'])
def about():
    if request.method == 'GET':
        return render_template('about.html')
    if request.method == 'POST':
        nav=request.form.get('nav')
        return request_func(nav)
if __name__ == "__main__":
    print("main")
    print("func")
    app.run(debug=True)


from flask import Flask, render_template,request,session,redirect,url_for
from werkzeug.utils import secure_filename
import pandas as pd
import os
from flask_mail import *

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="farmers",
    charset='utf8',
    port = 3306

)
cur=mydb.cursor()
UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

mycursor = mydb.cursor()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'the random string'
mail = Mail(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')


@app.route("/viewrequest")
def viewrequest():
    sql = "select id,name,email,shopename,address from reg where request='pending'"
    data = pd.read_sql_query(sql,mydb)
    print(data)
    return render_template('viewrequest.html',cols=data.columns.values,rows=data.values.tolist())

@app.route("/fmr/<id>")
def fmr(id=0):
    sql="update request set status='accepted' where id='%s'"%(id)
    cur.execute(sql)
    mydb.commit()
    return redirect(url_for('farmermachineryrequest'))

@app.route("/adminviewimage/<id>")
def adminviewimage(id=0):
    print(id)
    sql = "select image from request where id='%s'"%(id)
    cur.execute(sql)
    data=cur.fetchall()[0]
    print(data)
    return render_template('adminviewimage.html',imagename=data)


@app.route("/machinerequest")
def machinerequest():
    sql="select * from request where status='pending' and semail ='%s' " %(session['spemail'])
    data=pd.read_sql_query(sql,mydb)
    print(data)
    return render_template("machinerequest.html",cols=data.columns.values,rows=data.values.tolist())

@app.route("/spviewimage/<id>")
def spviewimage(id=0):
    print(id)
    sql = "select image from request where id='%s'"%(id)
    cur.execute(sql)
    data=cur.fetchall()[0]
    print(data)
    return render_template('spviewimage.html',imagename=data)

@app.route("/aspr/<id>")
def aspr(id=0):
    print(id)
    sql="update reg set request='accepted' where id='%s'"%(id)
    cur.execute(sql)
    mydb.commit()
    return redirect(url_for('viewrequest'))

    


@app.route("/sp")
def sp():
    return render_template('sp.html')

@app.route("/splog",methods=["POST","GET"])
def splog():
    if request.method == "POST":
        email = request.form['email']
        session['spemail'] = email
        password = request.form['pwd']
        sql = "select * from reg where email='%s' and password='%s' and request='accepted'" % (email, password)
        mycursor.execute(sql)
        results = mycursor.fetchall()
        session['email'] = email
        if len(results) > 0:
            return render_template('sphome.html',msg="Login successfull")
        else:
            return render_template('sp.html',msg="Login failed")
    return render_template('sp.html')

@app.route("/spreg",methods=["POST","GET"])
def spreg():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['pwd']
        contact = request.form['contact']
        shopename = request.form['shopename']
        address = request.form['address']
        print(name,email,password,shopename,address)
        sql = "insert into reg(name,email,password,contact,shopename,address)values(%s,%s,%s,%s,%s,%s)"
        val = (name,email,password,contact,shopename,address)
        mycursor.execute(sql,val)
        mydb.commit()
        return render_template('sp.html')
    return render_template('spreg.html',msg="Registred successfull")

# @app.route("/farmermachineryrequest")
# def farmermachineryrequest():
#     sql="select * from request where status='pending'"
#     data=pd.read_sql_query(sql,mydb)
#     return render_template("farmermachineryrequest.html",cols=data.columns.values,rows=data.values.tolist(),image=data)

@app.route("/adminlog",methods=["POST","GET"])
def adminlog():
    if request.method ==  "POST":
        username = request.form['email']
        password = request.form['pwd']
        if username == 'admin@gmail.com' and password == 'admin':
            return render_template('adminhome.html',msg="Login successfull")
        else:
            return render_template('admin.html',msg="Login Failed!!")
    return render_template('admin.html')

@app.route("/addmachinery",methods=["POST","GET"])
def addmachinery():
    if request.method == "POST":
        machineryname = request.form['machineryname']
        costwithdriver = request.form['costwithdriver']
        costwithoutdriver = request.form['costwithoutdriver']
        purpose = request.form['purpose']
        image = request.files['image']
        filena = image.filename
        sql = "insert into machinery(machineryname,costwithdriver,costwithoutdriver,purpose,image,semail)values(%s,%s,%s,%s,%s,%s)"
        val = (machineryname, costwithdriver, costwithoutdriver, purpose, filena, session['email'])
        mycursor.execute(sql,val)
        mydb.commit()
        image.save(os.path.join("static/projectimages/", filena))
        return redirect(url_for('addmachinery'))
    return render_template('addmachinery.html',msg="Details added successfully")


@app.route("/viewmachinery")
def viewmachinery():
    sql = "select * from machinery where semail='" + session['email'] + "'"
    data = pd.read_sql_query(sql, mydb)
    data = pd.read_sql_query(sql,mydb)
    print(data)
    return render_template("/viewmachinery.html",cols=data.columns.values,rows=data.values.tolist())

@app.route("/viewsendrequest/<id>")
def viewsendrequest(id=0):
    print(id)
    sql = "insert into machinery where id='%s'"%(id)
    cur.execute(sql)
    dc = cur.fetchall()
    print(dc)
    return render_template('/viewsendrequest.html')

@app.route("/farmer",methods=["POST","GET"])
def farmer():
    if request.method=="POST":
        email = request.form['email']
        password = request.form['pwd']
        sql="select * from farmerreg where email='%s' and password='%s' and status='accepted'"%(email,password)
        cur.execute(sql)
        dc = cur.fetchall()
        session['farmer_email'] = email
        if dc==[]:
            return render_template('farmerlogin.html')
        else:
            session['farmer_email'] = email
            return render_template('farmer.html')

    return render_template('farmerlogin.html')



@app.route("/farmerlogreq")
def farmerlogreq():
    sql="select * from farmerreg where status='pending'"
    data=pd.read_sql_query(sql,mydb)
    return render_template("farmerlogreq.html",cols=data.columns.values,rows=data.values.tolist())

@app.route("/afrl/<id>")
def afrl(id=0):
    print(id)
    sql="update farmerreg set status='accepted' where id='%s'"%(id)
    cur.execute(sql)
    mydb.commit()
    return redirect(url_for('farmerlogreq'))

@app.route("/aforl/<id>")
def aforl(id=0):
    print(id)
    sql="update request set status='accepted' where id='%s'"%(id)
    cur.execute(sql)
    mydb.commit()
    return redirect(url_for('machinerequest'))


@app.route("/farmerreg",methods=["POST","GET"])
def farmerreg():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        pwd1 = request.form['pwd1']
        pwd2 = request.form['pwd2']
        fcontact = request.form['fcontact']
        address = request.form['address']
        if pwd1 == pwd2:
            sql="select * from farmerreg where email='%s' and password='%s'"%(email,pwd1)
            cur.execute(sql)
            dc = cur.fetchall()
            if dc ==[]:
                sql="insert into farmerreg(name,email,password,fcontact,address) values(%s,%s,%s,%s,%s)"
                val = (name,email,pwd1,fcontact,address)
                cur.execute(sql,val)
                mydb.commit()
                return render_template("farmerlogin.html")
            else:
                return render_template("farmerreg.html")
        else:
            return render_template("farmerreg.html",msg="Password and Confirm Password not matched")

    return render_template("farmerreg.html")

@app.route("/viewfmachinery/<spmail>")
def viewfmachinery(spmail=''):
    session['sp'] = spmail
    sql = "select * from machinery where semail='" + spmail + "'"
    data = pd.read_sql_query(sql, mydb)
    print(data)
    return render_template('viewfmachinery.html',cols=data.columns.values,rows=data.values.tolist())

@app.route('/price/<id>')
def price(id=" "):
    print(id)
    return render_template('price.html',a=id)

@app.route('/priceback',methods=['POST'])
def priceback():
    if request.method =="POST":
        name = request.form['name']
        Email = request.form['Email']
        smail = request.form['smail']
        amount = request.form['amount']
        cardname = request.form['cardname']
        cardnumber = request.form['cardnumber']
        expmonth = request.form['expmonth']
        cvv = request.form['cvv']
        sql = "insert into payment(name,Email,smail,amount,cardname,cardnumber,expmonth,cvv)values(%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (name,Email,smail,amount,cardname,cardnumber,expmonth,cvv)
        cur.execute(sql,val)
        mydb.commit()
        return render_template('price.html')

@app.route("/sppayment")
def sppayment():
    
    sql = "select id,name,Email,smail,amount,cardname from payment where status='pending' and smail='%s'"%(session['spemail'])
    data = pd.read_sql_query(sql,mydb)
    print(data)
    return render_template("sppayment.html",cols=data.columns.values,rows=data.values.tolist())

@app.route('/newsp')
def newsp():
    sql ="select distinct semail from machinery"
    data = pd.read_sql_query(sql,mydb)
    print(data)
    return render_template('newsp.html',cols=data.columns.values,rows=data.values.tolist())



@app.route("/sendtoadmin/<id>",methods=["POST","GET"])
def sendtoadmin(id=0):
    print(id)
    print(session['sp'])

    sql="select * from machinery where id='%s'"%(id)
    cur.execute(sql)
    dc = cur.fetchall()
    print(dc)
    mname = dc[0][1]
    withdriver = dc[0][2]
    withoutdriver =dc[0][3]
    purpose = dc[0][4]
    image = dc[0][5]
    semail = session['sp']
    email = session['farmer_email']
    print("==============================")
    print(mname,withdriver,withoutdriver,purpose,image,semail,email)
    print("==============================")
    sql = "insert into request(mname,withdriver,withoutdriver,purpose,image,semail,f_email) values(%s,%s,%s,%s,%s,%s,%s)"
    val = (mname,withdriver,withoutdriver,purpose,image,semail,email)
    cur.execute(sql,val)
    mydb.commit()
    print(dc)
    return render_template("sended.html",msg="Request send successfully")

        

@app.route("/sendrequest")
def sendrequest():
    return  render_template('sendrequest.html')

@app.route("/viewresponse")
def viewresponse():
    sql="select * from request where status='accepted' and f_email ='%s'"%(session['farmer_email'])
    data=pd.read_sql_query(sql,mydb)
    return render_template('viewresponse.html',cols=data.columns.values,rows=data.values.tolist(),msg="Request accepted successfully")

@app.route("/viewimage/<id>")
def viewimage(id=0):
    print(id)
    sql = "select image from request where id='%s'"%(id)
    cur.execute(sql)
    data=cur.fetchall()[0]
    print(data)
    return render_template('viewimage.html',imagename=data)




if __name__ == "__main__":
    app.run(debug=True)

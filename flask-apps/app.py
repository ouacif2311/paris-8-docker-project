from flask import Flask, request,render_template
import psycopg2

def connect(database="database",user="kmeans_project_user",password="kmeans_project_user_password", host="db",port="5432"):
    try: 
        conn = psycopg2.connect(database=database, user=user, password=password, host=host,port=port)
        print("connected")
    except:
        print ("I am unable to connect to the database")

    mycursor = conn.cursor()

    return mycursor

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iris_data_page/')
def iris_data_page():
    mycursor = connect()
    mycursor.execute("SELECT * FROM iris")
    data = mycursor.fetchall()
    #return render_template('kmeansOutputPage.html')
    return render_template('irisDataPage.html', data=data)

@app.route('/kmeans_output_page/')
def kmeans_output_page():
    mycursor = connect()
    mycursor.execute("SELECT * FROM output")
    data = mycursor.fetchall()
    #return render_template('kmeansOutputPage.html')
    return render_template('kmeansOutputPage.html', data=data)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
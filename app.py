from flask import Flask
from connection import Connection
from database import Database
from authorization import auth
from datetime import datetime

app = Flask(__name__)


conn = Connection()
_mongo_uri = conn.create_mongo_uri()
db = Database(_mongo_uri)

# db = Database('mongodb+srv://muskan24100:Password@123456@cluster0.sn1iybl.mongodb.net/')

@app.route('/create_user', methods=['POST'])
@auth.login_required
def create_user():

    password = auth.current_user()[1]

    # if(auth.username() == )
    
    _,cursor_files = db.get_db_connection(coll_name='user_data')
    post = {'datetime': datetime.now(),'username':auth.username(),'password':password}
    # print(post)
    cursor_files.insert_one(post)

    return 'Success'

#main function
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
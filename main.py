from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import certifi

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://parvjoshi20:sxdFe2ccFjI22Qf2@cluster0.ytrm8ze.mongodb.net/ChatSplash"
mongo = PyMongo(app)

@app.route('/')
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("main.html", myChats = myChats)

@app.route('/light_mode')
def light_mode():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template('light_mode.html',myChats = myChats)

@app.route('/dark_mode')
def dark_mode():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template('dark_mode.html',myChats = myChats)

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat=mongo.db.chats.find_one({'question':question})
        print(chat)
    
        if chat:
            data = {"result": f"{chat['answer']}"}
            return jsonify(data)
        else:
            data = {"result": f"Answer of{question}"}
            mongo.db.chats.insert_one({'question':question,"answer":f"Answer from open ai for{question}"})
            return jsonify(data)
    data = {"result": "Thank you! I'm drizzle!"}
    return jsonify(data)
        
app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name__)
import json #Forgot to add this in for, like, a minute. Then I wondered how the json.load bit wasn't working...

@app.route('/') #Home Page
def index():
    return render_template('index.html')

@app.route('/GeneralInfo') #General Info Page
def GeneralInfo():
    return render_template('GeneralInfo.html')

@app.route("/Notes") #Notes From Me Page
def Notes():
    return render_template('Notes.html')

@app.route("/Leaderboard") #Untuned Leaderboard Page
def MainLeaderboard():
    with open('JSON/MainLeaderboard.json', 'r') as f1:
        data1 = json.load(f1)
    return render_template('Leaderboard.html', data=data1)

@app.route("/MindBenderLeaderboard") #Mind Bender Leaderboard Page
def MBLeaderboard():
    with open('JSON/MindBenderLeaderboard.json', 'r') as f2:
        data2 = json.load(f2)
    return render_template('MindBenderLeaderboard.html', data=data2)

@app.route("/E60Leaderboard") #E60 Leaderboard Page
def E60Leaderboard():
    with open('JSON/E60Leaderboard.json', 'r') as f3:
        data3 = json.load(f3)
    return render_template('E60Leaderboard.html', data=data3)

@app.route("/TunedLeaderboard") #Tuned Leaderboard Page
def TunedMainLeaderboard():
    with open('JSON/TunedMainLeaderboard.json', 'r') as f4:
        data4 = json.load(f4)
    return render_template('TunedLeaderboard.html', data=data4)

@app.route("/NBloxLeaderboard") #N-Blox Leaderboard Page
def NBloxLeaderboard():
    with open('JSON/NBloxLeaderboard.json', 'r') as f5:
        data5 = json.load(f5)
    return render_template('NBloxLeaderboard.html', data=data5)

@app.route("/Leaderboard15m") #Untuned Leaderboard < 2m Score Page
def LeaderboardSub2m():
    with open('JSON/Leaderboard15m.json', 'r') as f6:
        data6 = json.load(f6)
    return render_template('Leaderboard15m.html', data=data6)

@app.route("/Leaderboard2m") #Untuned Leaderboard 2m > && < 3m Page
def LeaderboardSub3m():
    with open('JSON/Leaderboard2m.json', 'r') as f7:
        data7 = json.load(f7)
    return render_template('Leaderboard2m.html', data=data7)

@app.route("/Leaderboard3m") #Untuned Leaderboard 3m > Page
def Leaderboard3m():
    with open('JSON/Leaderboard3m.json', 'r') as f8:
        data8 = json.load(f8)
    return render_template('Leaderboard3m.html', data=data8)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
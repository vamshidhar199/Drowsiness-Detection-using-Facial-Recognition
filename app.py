from flask import Flask, redirect, url_for, render_template, request
import os

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index3.html')


@app.route('/index2', methods=['POST', 'GET'])
def index2():
    # index2 = request.form
    # return render_template('index2.html')
    os.system('dir')
    os.system('python3 drowsy.py -p 68_face_landmarks.dat -a alarm.wav')
    #v = functions.val()
    # assert isinstance(v, str)
    lines = []
    values=[]
    labels=[]
    closed=0
    opened=0
    v=[0,0]
    alcount=0
    colors=['red','blue']
    w = open('week.txt', 'a')
    #legend = 'Monthly Data'
    with open("text.txt") as file:
        for line in file:
            line = line.strip()  # or some other preprocessing
            lines.append(line)
            if float(line)<0.3:
                closed=closed+1
            else:
                opened=opened+1
            # storing everything in memory!
            values.append(float(line))
            #values = values[1:50]
            l = len(values)
            k=0
            for i in range(10):
                labels.append(k)

    with open("alcount.txt") as al:
        for l in al:
            if l.startswith("on"):
                alcount=alcount+1
            #s="\n".join(lines)
    w.write(str(alcount)+"\n")
    #w.write("\n")
    v[0]=closed
    v[1]=opened
    labe=['closed','opened']
    #return render_template('piechart.html',f=lines,title='Sleepy chart', max=0.01,set=zip(values, labels,colors))
    return render_template('charts.html', f=lines, title='Sleepy chart', set=zip(v,labe,colors),max=0.01, values=values, labels=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','...'],closed=closed,opened=opened,alcount=alcount)

@app.route('/index4', methods=['POST', 'GET'])
def index4():
    week=[]
    wlables=[]
    count=0
    with open("week.txt") as w:
        for i in w:
            week.append(i)
            count=count+1
    for j in range(0,count):
        wlables.append(j)

    return render_template('hello.html',f=week,max=0.1,values=week,labels=wlables)
@app.route('/image',methods=['POST','GET'])
def image():
    week = []
    count=0
    with open("week.txt") as ww:
        for i in ww:
            week.append(i)
        week=week[::-1]
        for i in range(0,7):
            count=count+int(week[i])

    return render_template('image.html',count=count)
if __name__ == "__main__":
    app.run(host='0.0.0.0')

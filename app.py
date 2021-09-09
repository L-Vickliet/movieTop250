from flask import Flask, render_template
import sqlite3
import re



app = Flask(__name__)


@app.route('/index')
def index():
    infos = []
    con = sqlite3.connect("douban250.db")
    cur = con.cursor()
    sql = "select * from movie limit 0, 10"
    data = cur.execute(sql)
    
    for item in data:
        infos.append(item)


    years = []
    num = []
    sql = "select 上映年份, count(上映年份) from movie group by 上映年份"
    data1 = cur.execute(sql)
    
    for item in data1:
        years.append(re.sub('\D', "",  item[0]))   #将非数字字符替换成空字符
        num.append(item[1])
    
    
    datalist = []
    sql = "select 评分,sum(评价数) from movie group by 评分"
    data2 = cur.execute(sql)

    for item in data2:
        datalist.append([item[0], item[1]])


    cur.close()
    con.close()

    return render_template("index.html", infos=infos, years=years, num=num, datalist=datalist)


if __name__=='__main__':
    app.run()
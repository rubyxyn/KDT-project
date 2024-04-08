
# 모듈 불러오기
from flask import Flask, render_template, request
import os

from cosine import find_sofa, find_tvdesk, find_table, find_sidetable
from cosine import find_bed, find_nightstand, find_mirror, find_drawer
from cosine import find_diningtb, find_chair, find_ovenst, find_cab



app = Flask(__name__)
template_dir = os.path.join(os.path.dirname(__file__),'templates')

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/lr.html')
def livingRoom():
    return render_template('lr.html')

@app.route('/br.html')
def bedRoom():
    return render_template('br.html')

@app.route('/kit.html')
def kitchen():
    return render_template('kit.html')

@app.route('/process1', methods=['GET','POST'])
def process1():
    sofa = request.form.get('sofa')
    tv_desk = request.form.get('tv_desk')
    table = request.form.get('table')
    side_table = request.form.get('side_table')
    print(sofa, tv_desk, table, side_table)
    print("처리")

    _sofa = find_sofa(sofa)
    _tvdesk = find_tvdesk(tv_desk)
    _table = find_table(table)
    _sidetable = find_sidetable(side_table)
    print(_sofa)
    print(_tvdesk)
    print(_table)
    print(_sidetable)

    # 딕셔너리 형태가 아닌 "start" = _start 형식으로 입력해야 함 
    return render_template('result_lr.html',**{"sofa":_sofa,
                                                "tvdesk":_tvdesk,
                                                "table":_table,
                                                "sidetable":_sidetable,})


@app.route('/process2', methods=['GET','POST'])
def process2():
    bed = request.form.get('bed')
    night_stand = request.form.get('night_stand')
    mirror = request.form.get('mirror')
    drawer = request.form.get('drawer')
    print(bed, night_stand, mirror, drawer)
    print("처리")

    _bed = find_bed(bed)
    _nightst = find_nightstand(night_stand)
    _mirror = find_mirror(mirror)
    _drawer = find_drawer(drawer)

    print(_bed)
    print(_nightst)
    print(_mirror)
    print(_drawer)

    # 딕셔너리 형태가 아닌 "start" = _start 형식으로 입력해야 함 
    return render_template('result_br.html',**{"bed":_bed,
                                                "nightst":_nightst,
                                                "mirror":_mirror,
                                                "drawer":_drawer,})


@app.route('/process3', methods=['GET','POST'])
def process3():
    table = request.form.get('table')
    chair = request.form.get('chair')
    oven_stand = request.form.get('oven_stand')
    cabinet = request.form.get('cabinet')
    print(table, chair, oven_stand, cabinet)
    print("처리")

    _table = find_diningtb(table)
    _chair = find_chair(chair)
    _ovenst = find_ovenst(oven_stand)
    _cabinet = find_cab(cabinet)
    
    print(_table)
    print(_chair)
    print(_ovenst)
    print(_cabinet)

    # 딕셔너리 형태가 아닌 "start" = _start 형식으로 입력해야 함 
    return render_template('result_kit.html',**{"table":_table,
                                                "chair":_chair,
                                                "ovenst":_ovenst,
                                                "cabinet":_cabinet,})




if __name__ == '__main__':
    app.run(debug=True)


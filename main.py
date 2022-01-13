import datetime
import json
import uuid

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user, logout_user

from . import db
from .models import Post, Post_Label, Label, Accesor_Label, Post_Assessment, Accesor

main = Blueprint('main', __name__)


@main.route('/')
def index():
    logout_user()

    # qry = Post.query.filter(Post.created_at.between('2021-10-01', '2021-11-23')).limit(20).all()
    # for i in qry:
    #     if i.text is not None:
    #         insert_post_as = Post_Assessment(id=i.id)
    #         db.session.add(insert_post_as)
    #         db.session.commit()
    return render_template('login.html')


def post(current_user):
    # rand = random.randrange(0,Post.query.filter(Post.text!=None).count())
    post_query = Post_Assessment.query.all()
    if current_user.val == len(post_query):
        text = 'Оценка постов закончена!'
        id = 'end'
        return id, text, current_user.val - 1, len(post_query)
    else:
        get_post = Post.query.filter(Post.id == post_query[current_user.val].id).first()
        return get_post.id, get_post.text, current_user.val, len(post_query)


@main.route('/profile')
@login_required
def profile():
    res_post = post(current_user)
    name = current_user.first_name + ' ' + current_user.last_name
    start = datetime.datetime.now()
    return render_template('profile.html', name=name, id_post=res_post[0], text_post=res_post[1],
                           curr_post=res_post[2], all_post=res_post[3],
                           name_id=current_user.id, start_time=start.strftime("%H:%M:%S"))


@main.route('/postmethod', methods=['POST'])
def get_post_javascript_data():
    jsdata = request.form
    end_time = datetime.datetime.now()
    data = json.loads(jsdata.to_dict()['data'])
    start_time = datetime.datetime.strptime(data['start_time'], '%H:%M:%S')
    result_time = end_time - start_time
    result_time = datetime.timedelta(seconds=result_time.seconds)
    dt_res = datetime.datetime.strptime(str(result_time), "%H:%M:%S")

    label_id = uuid.uuid4()
    insert_labels = Label(id=label_id,
                          objectivity=int(data['objectivity']),
                          perspective=int(data['perspective']),
                          doubts=int(data['doubts']),
                          doubts_success=int(data['doubts_success']),
                          meeting_needs=int(data['meeting_needs']))
    db.session.add(insert_labels)
    db.session.commit()

    id_label = uuid.uuid4()

    insert_accessor_label = Accesor_Label(id=id_label,
                                          id_accesor=data['id_name'],
                                          id_label=label_id,
                                          create_time=end_time)

    db.session.add(insert_accessor_label)
    db.session.commit()

    insert_post_label = Post_Label(id=uuid.uuid4(),
                                   id_post=data['id_post'],
                                   id_label=id_label,
                                   elapsed_time=dt_res)

    db.session.add(insert_post_label)
    db.session.commit()

    update_accesor_val = Accesor(id=current_user.id,
                                 first_name=current_user.first_name,
                                 last_name=current_user.last_name,
                                 val=current_user.val + 1,
                                 role=current_user.role)
    db.session.merge(update_accesor_val)
    db.session.commit()

    res_post = post(current_user)
    name = current_user.first_name + ' ' + current_user.last_name
    start = datetime.datetime.now()
    return render_template('profile.html', name=name, id_post=res_post[0], text_post=res_post[1],
                           curr_post=res_post[2], all_post=res_post[3],
                           name_id=current_user.id, start_time=start.strftime("%H:%M:%S"))

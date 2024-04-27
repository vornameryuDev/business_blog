from datetime import datetime
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app import db
from forms.answer_form import AnswerCreateForm, AnswerUpdateForm
from models.answer_model import Answer
from models.question_model import Question


bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/delete/<int:answer_id>')
def delete(answer_id):    
    answer = Answer.query.get_or_404(answer_id)
    question_id = answer.question.id
    if current_user.nickname != answer.user.nickname:
        return jsonify(grant=False)
    db.session.delete(answer)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))


@bp.route('/update/<int:answer_id>', methods=["GET", "POST"])
def update(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    form = AnswerUpdateForm(obj=answer) #원래 내용 가져오기
    #post and validate
    if request.method == 'POST' and form.validate_on_submit():
        form.populate_obj(answer)
        db.session.commit() #db저장
        return redirect(url_for('question.detail', question_id=answer.question.id))
    #get
    if current_user.nickname != answer.user.nickname: #권한있는 사람만 url로 접근가능
        return jsonify(grant=False)
    return render_template('answer/update.html', form=form)


@bp.route('/create/<int:question_id>', methods=["POST"])
@login_required
def create(question_id):
    form = AnswerCreateForm()
    question = Question.query.get(question_id)        
    if request.method == "POST" and form.validate_on_submit():
        answer = Answer(
            content = form.content.data,
            user = current_user,
            created_at = datetime.now()
        ) #answer정의
        question.answer_set.append(answer) #답변저장
        db.session.commit() #커밋
        return redirect(url_for('question.detail', question_id=question_id))
    #get접근
    return jsonify(grant=False)
    
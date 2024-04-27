const backQuestionListBtn = document.querySelector('.question-detail-btn-box .list');
const updateQuestionBtn = document.querySelector('.question-detail-btn-box .update');
const deleteQuestionBtn = document.querySelector('.question-detail-btn-box .delete');
const recommendQuestionBtn = document.querySelector('.question-detail-btn-box .recommend');


function backToQuestionList() {
    location.href = this.dataset.uri;
}
function updateQuestion() {
        location.href = this.dataset.uri;    
}
function deleteQuestion() {
    if (confirm('정말 삭제하시겠습니까?')) {
        location.href = this.dataset.uri;
    }
}
function recommendQuestion() {
    if (confirm('추천하시겠습니까?')) {
        location.href = this.dataset.uri;
    }
}


backQuestionListBtn.addEventListener('click', backToQuestionList);
recommendQuestionBtn.addEventListener('click', recommendQuestion);
updateQuestionBtn.addEventListener('click', updateQuestion);
deleteQuestionBtn.addEventListener('click', deleteQuestion);

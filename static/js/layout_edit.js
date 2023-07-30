function toggleEditForm(commentId) {
    var commentText = document.getElementById("comment_text_" + commentId);
    var editForm = document.getElementById("edit_comment_" + commentId);
    var editButton = document.getElementById("edit_msg_" + commentId);

    if (commentText.style.display === "none") {
        commentText.style.display = "block";
        editForm.style.display = "none";
        editButton.innerHTML = "Editar";
    } else {
        commentText.style.display = "none";
        editForm.style.display = "block";
        editButton.innerHTML = "Cancelar";
    }
};
function showForm() {
    var groupInfo = document.getElementById('group-info');
    var editForm = document.getElementById('edit-form');
    var editButton = document.getElementById('edit-button');

    if (groupInfo.style.display === 'none') {
        groupInfo.style.display = 'block';
        editForm.style.display = 'none';
        editButton.innerText = 'Editar';
    } else {
        groupInfo.style.display = 'none';
        editForm.style.display = 'block';
        editButton.innerText = 'Cancelar';
    }
}

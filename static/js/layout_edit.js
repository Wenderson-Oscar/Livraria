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
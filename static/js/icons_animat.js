document.getElementById('favoriteBtn').addEventListener('click', function() {
    if (this.classList.contains('far')) {
        this.classList.remove('far');
        this.classList.add('fas');
        this.classList.add('text-warning');
    } else {
        this.classList.remove('fas');
        this.classList.add('far');
        this.classList.remove('text-warning');
    }
});
document.getElementById('likeBtn').addEventListener('click', function() {
    if (this.classList.contains('far')) {
        this.classList.remove('far');
        this.classList.add('fas');
        this.classList.add('text-primary');
    } else {
        this.classList.remove('fas');
        this.classList.add('far');
        this.classList.remove('text-primary');
    }
});
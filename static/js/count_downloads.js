var downloads = document.getElementById('downloads');
    downloads.addEventListener('click', function() {
    window.location.href = "{% url 'count_downl' pk=book.pk %}";
});
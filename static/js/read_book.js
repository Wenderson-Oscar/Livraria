PDFJS.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.9.359/pdf.worker.min.js';
var url = '{{book.book.url}}';
PDFJS.getDocument(url).promise.then(function(pdf) {
    var pageNumber = 1;
    pdf.getPage(pageNumber).then(function(page) {
        var scale = 1.5;
        var viewport = page.getViewport({ scale: scale });

        var canvas = document.createElement('canvas');
        var context = canvas.getContext('2d');
        canvas.height = viewport.height;
        canvas.width = viewport.width;

        var container = document.createElement('div');
        container.appendChild(canvas);
        document.body.appendChild(container);

        var renderContext = {
            canvasContext: context,
            viewport: viewport
        };
        page.render(renderContext);
    });
});

function generatePDF() {
    var element = document.getElementById("pdfContent");
    html2pdf().from(element).save();
};
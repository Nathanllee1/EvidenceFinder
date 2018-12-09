

var quill = new Quill('#editor', {
    theme: 'bubble'
});

setInterval(function() {
  if (change.length() > 0) {
    console.log('Sent for ml', change);
    /*
    Send entire document
    $.post('/your-endpoint', {
      doc: JSON.stringify(quill.getContents())
    });
    */
    change = new Delta();
  }
}, 5*1000);
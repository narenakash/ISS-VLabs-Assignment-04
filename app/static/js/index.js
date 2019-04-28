console.log("hi ammar , it is linked u idiot")
$(document).ready(function() {
    $('form').on('submit', function(event) {
      $.ajax({
         data : {
            firstName: "helo",
            lastName: "whatever",
                },
            type : 'POST',
            url : '/'
           })
     });
});
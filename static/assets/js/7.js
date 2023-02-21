$('#save_customer').on('click', function(){
    const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    $(document).ajaxSend(function(){
      $('spinner-grow').fadeIn(500);
      var loading = ` <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>`;
      $("#save_customer").html(loading);
    });
    
    $.ajax({
      type: 'POST',
      url: '/staff/save_customer/',
      
      
      data: {
        'csrfmiddlewaretoken': csrf,
        'username': $('#username').val(),
        'first_name': $('#first_name').val(),
        'last_name': $('#last_name').val(),
        'email': $('#email').val(),
        'password1': $('#password1').val(),
        'password2': $('#password2').val(),
        
      },
      dataType: 'json',
      before: function(){
        
      },
      success: function(res){
        console.log(res.data)
      }
    })
  })
  
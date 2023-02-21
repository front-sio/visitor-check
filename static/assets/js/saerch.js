
  const url = window.location.href;
  const checkBtn = document.querySelector('#check_btn');
  const hide_search_form = document.querySelector('#hide_search_form');
  // const save_visitor_form = document.querySelector('#save_visitor_form');
  const searchForm = document.querySelector('#search-form');
  const resultBox = document.querySelector('#result-box');
  // const verifyBtn = document.getElementById('#verify-cont');

  const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;



$("#check_btn").on('click', function(){
  $(document).ajaxSend(function(){
    $('spinner-grow').fadeIn(500);
    var loading = ` <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"> </span> Verifying wait...`;
    $("#check_btn").html(loading);
  });
  
  $.ajax({
    type: 'POST',
    url: '/customers/check/',
    data: {
      'csrfmiddlewaretoken': csrf,
      id_number: $('#id_number').val(),
    },
    success: (res)=>{
       const search_input = $('#id_number')
       const data = res.data 
       console.log(data)
       if (Array.isArray(data)){
        $("#modal-form").modal("show");
        data.forEach(data => {
          resultBox.innerHTML +=`

        <div class="mb-3">
         <input type="text" class="form-control" hidden name="id_number" id="id_number" disabled value="${data.NIN}">
       </div>
          <div class="mb-3">
              <label>First name</label>
               <input type="text" class="form-control" name="first_name" id="first_name" disabled value="${data.FirstName}">
            </div>

            <div class="mb-3">
            <label>Middle name</label>
             <input type="text" class="form-control" name="middle_name" id="middle_name" disabled value="${data.MiddleName}">
            </div>

            <div class="mb-3">
            <label>Last name</label>
             <input type="text" class="form-control" name="last_name" id="last_name" disabled value="${data.LastName}">
            </div>

            <div class="mb-3">
            <label>Date of birth</label>
             <input type="text" class="form-control" name="date_of_birth" id="date_of_birth" disabled value="${data.DateofBirth}">
            </div>

            <div class="mb-3">
            <label>Gender</label>
             <input type="text" class="form-control" name="gender" id="gender" disabled value="${data.Sex}" >
            </div>

            <div class="mb-3">
            <label>On behalf (optional)</label>
             <input type="text" class="form-control" name="on_behalf" id="on_behalf">
            </div>

            <div class="" id="verify-cont">
              <button id="verify_bt" class="btn bg-gradient-info w-100 mt-4 mb-0">Verify</button>
            </div> 


           
            `
        });
        
       }else{
        $("#modal-form").modal("show");
        if (data == 'No data match!'){
          resultBox.innerHTML = `<b>${data}</b>`
          // alert(data)
        }
       }
       


      checkBtn.classList.add('not-visible')
      hide_search_form.classList.add('not-visible')

      if(resultBox.classList.contains('not-visible')){
        resultBox.classList.remove('not-visible')
      }

      // if(save_visitor_form.classList.contains('not-visible')){
      //   save_visitor_form.classList.remove('not-visible')
      // }

    
      
      


  
     
    },
    error: (err)=>{
      console.log(err)
    },
  }).done(function(){
    setTimeout(function(){
      $('.spinner-grow').fadeOut(500);
    }, 700);

});

});





$('#verify_btn').on('click', function(){
  $(document).ajaxSend(function(){
    $('spinner-grow').fadeIn(500);
    var loading = ` <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>  Thank you`;
    $("#verify_btn").html(loading);
  });

  $.ajax({
    type: 'POST',
    url: '/customers/visitors/save/',
    data: {
      id_number: $('#id_number').val(),
      first_name: $('#first_name').val(),
      middle_name: $('#middle_name').val(),
      last_name: $('#last_name').val(),
      gender: $('#gender').val(),
      office_visited: $('#office_visited').val(),
      date_of_birth: $('#date_of_birth').val(),
      on_behalf: $('#on_behalf').val(),
      csrfmiddlewaretoken: csrf,
    },
    dataType: 'json',
    before: function(){},
    success: function(res){
      console.log(res)
    },
    error: function(err){
      console.log(err)
    }
  }).done(function(){
    setTimeout(function(){
      $('.spinner-grow').fadeOut(500);
    }, 500);

});

})


  // searchInput.addEventListener('keyup', e=> {
  //   console.log(e.target.value)

  //   sendSearchData(e.target.value)
  // })


 





// add office function

$('#save_office').on('click', function(){
  const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  $(document).ajaxSend(function(){
    $('spinner-grow').fadeIn(500);
    var loading = ` <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>`;
    $("#save_office").html(loading);
  });
  
  $.ajax({
    type: 'POST',
    url: '/offices/save_office/',
    
    
    data: {
      'csrfmiddlewaretoken': csrf,
      'name': $('#name').val(),
      'created_on': $('#created_on').val(),
      
    },
    dataType: 'json',
    before: function(){
      
    },
    success: function(res){
      console.log(res.data)
    }
  })
})






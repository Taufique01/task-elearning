
$(document).ready( function () {



  //////initialize data table
      var table = $('#course-table').DataTable({
          destroy: true,
          paging:   false,
          ordering: true,
          info:     false,
          searching: true,


          columns: [
              { data: null, render: 'id',visible: false },
              { data: null, render: 'title',visible: true },
              { data: null, render: 'is_active',visible: true },


               { data: null,"render": function ( data, type, row, meta ) {


                      var edit='<button class="edit-btn  btn btn-secondary" >Edit</button>';

                      return  edit;
                       }
                },


          ],

          dom: 'Bfrtip',
          buttons: [
            {
              text: 'Add Course',
              action: function ( e, dt, node, config ) {
              $('#add-modal').modal('show');
              }
            }
          ],


      });

      $('#course-table tbody').on( 'click', 'button', function (){


               var data = table.row( $(this).parents('tr') ).data();

               var row_index = table.row( $(this).parents('tr') ).index();

               console.log(data);
               $('#course-title-update').val(data.title);
               $('#course-status-update').val(String(data.is_active)).change();
               $('#course-id-update-input').val(data.id);
               $('#course-table-edit-row').val(row_index);

               $('#update-modal').modal('show')




      });


    $.ajax({
        url:"/api/educator/",
        type: "GET",

        success: function (courses) {



            for(let i=0;i<courses.length;i++){

              table.row.add(courses[i]);
            }

            table.draw();
        },


        error: function (request, status, error) {



        }
    });



    $('#course-update-btn').click(function(){




      $.ajax({
      url: $('#course-update-form').attr("js-course-update-url"),
      type: $('#course-update-form').attr("method"),
      headers: {
          "X-CSRFToken": $('#course-update-form').attr("csrf-token"),
      },
      data: $('#course-update-form').serialize(),
      dataType: 'json',
      success: function (course) {

        alert("Course, successfully updated");

        var row_index =  $('#course-table-edit-row').val();

        table.row(row_index).data( course ).draw();


      },


      error: function (request, status, error) {

          alert(status);

      }
  });


});



  $('#course-save-btn').click(function(){


    $.ajax({
    url: $('#course-add-form').attr("js-course-add-url"),
    type: $('#course-add-form').attr("method"),

    data: $('#course-add-form').serialize(),
    dataType: 'json',
    success: function (course) {

      alert("Course, successfully added");



      table.row.add(course).draw();


    },


    error: function (request, status, error) {

        alert(status);

    }
  });





});




} );

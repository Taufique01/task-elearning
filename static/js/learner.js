
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
              { data: null, render: 'educator',visible: true },


               { data: 'is_enrolled',"render": function ( data, type, row, meta ) {



                      if(data){
                          var enroll = '<input type="button "  value="Enrolled" class="enroll-btn  btn btn-secondary" ' +'disabled' +  ' >' ;

                      }else{
                        var enroll = '<input type="button "  value="Enroll Now" class="enroll-btn  btn btn-primary" >';
                      }




                      return  enroll;
                       }
                },


          ],




      });

      $('#course-table tbody').on( 'click', 'input', function (){


               var row_data = table.row( $(this).parents('tr') ).data();
               $('#course-id-input').val(row_data.id);
               var row_index = table.row( $(this).parents('tr') ).index();

               $.ajax({
               url: $('#enrollment-form').attr("js-enrollment-url"),
               type: $('#enrollment-form').attr("method"),

               data: $('#enrollment-form').serialize(),
               dataType: 'json',
               success: function (course) {

                 alert("successfully Enrolled");



                 table.row(row_index).data( course ).draw();


               },


               error: function (request, status, error) {

                   alert(status);

               }
             });






      });




      $.ajax({
          url:"/api/learner/",
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



});

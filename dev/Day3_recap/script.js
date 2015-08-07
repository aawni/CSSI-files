console.log("hello");

$(document).ready(
  function(){
    $("#insert_button").click(createListElement);
  }
);

function createListElement() {
  console.log("hello");
  var person = $('#asignee').val();
  var task = $("#new_task").val();
  $('#task.list').append('<li>' + person + " " + task + '</li>')

}

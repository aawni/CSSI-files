$(document).ready(function(){

var count = 1;

	$("#add_button").click(
		function(){
			$("#task_list").append("<li>" + count + ". " + $("#task_name").val() + "</li>");
			count ++;
		});


	$("#remove_button").click(
	function(){
		var num= $("#task_num").val()-1;
	$("#task_list").children().eq(num).remove();
		count--;

		for (var ind = num; ind < count; ind++)
		{
			console.log("a");
			var task = $("#task_list").children().eq(ind).text();
			var space_ind=0;
			space_ind = task.indexOf(' ');
			var removed_num = task.substr(space_ind+1);
			$("#task_list").children().eq(ind).text((ind+1) + ". " + removed_num);
		}

	});

});

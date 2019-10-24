function getRandomUser(){
	peopleNumber = document.getElementById("peopleNumber").value;
	data = JSON.stringify({'number': peopleNumber});
	$.ajax({
	    type:'post',
	    contentType: "application/json",
		data: data,
		url: "/process_data/",
		async:'asynchronous',
		dataType:'json',
		success: function(data) {
			alert(data['answer'] + " users have been saved!")
		},
		error: function(request, status, error) {
			console.log("Error: " + error);
		}
   	});
}

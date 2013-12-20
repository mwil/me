
$(document).on("pageinit", "#main", function(){
/*	// generate publication list on server-side (deprecated)
	$.post('../cgi-bin/pubs.py', {'command': 'listbib'}, function(response) {
		console.log(response);
		$("#pub-lv").append(response).listview("refresh");
	});

	// fetch publication list via ajax (deprecated)
	$.get("ajax/pubs.html", function(data) {
  		$("#pub-lv").append(data).listview("refresh");
	});
*/
	$("#mail-id").text("E-Mail: ")
});


$(document).on("click", ".bibtex-btn", function() {
	$.post('../cgi-bin/pubs.py', {'command': 'bibentry', 'bibkey': $(this).data("bibkey")}, function(response) {
		$("#bibtex-textarea").val(response);
		$("#bibtex-popup").popup("open");
	});
});

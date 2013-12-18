
$(document).on("pageinit", "#main", function(){
/*	$.post('../cgi-bin/pubs.py', {'command': 'listbib'}, function(response) {
		console.log(response);
		$("#pub-lv").append(response).listview("refresh");
	});
*/
	$.get("ajax/pubs.html", function(data) {
  		$("#pub-lv").append(data).listview("refresh");
	});
});

$(document).on("click", ".bibtex-btn", function() {
	$.post('../cgi-bin/pubs.py', {'command': 'bibentry', 'bibkey': $(this).data("bibkey")}, function(response) {
		$("#bibtex-textarea").val(response);
		$("#bibtex-popup").popup("open");
	});
});

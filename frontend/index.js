var request = new XMLHttpRequest();
const url = "http://127.0.0.1:8000/items/5"
request.open('GET', url, true);
request.send();

request.onload = function () 
{
	// Begin accessing JSON data here
	var data = JSON.parse(this.response);

	if (request.status >= 200 && request.status < 400) 
	{
		alert(data.q);
	} 
	else 
	{
		const errorMessage = document.createElement('marquee');
		errorMessage.textContent = `Gah, it's not working`;
	}
}

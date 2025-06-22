const grid = document.getElementsByClassName("container")[0];


window.onload = function () 
{

	// Make each "cell" interactive
	for (var i = 0; i < grid.children.length; i++) 
	{
		grid.children[i].onclick = function()
		{	
			sendRequest(this);
			//test(this);
		}
	}	
}

function test(num)
{	
	alert(num.innerHTML);
}

function sendRequest(num)
{
	var baseURL = "http://127.0.0.1:8000/fib/";
	var url = baseURL + num.innerHTML.trim();
	
	//alert(url);
	
	var request = new XMLHttpRequest();
	request.onload = process;
	request.open('GET', url, true);
	request.send()

}

function process()
{
	// Begin accessing JSON data here
	var data = JSON.parse(this.response);

	if (this.status >= 200 && this.status < 400) 
	{
		alert(data.fib_n);
	} 
	else 
	{
		const errorMessage = document.createElement('marquee');
		errorMessage.textContent = `Gah, it's not working`;
	}
}

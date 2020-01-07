var myHeaders = new Headers();
myHeaders.append("API_KEY", "limzeyang");

var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
};

var dataFetched = {};

fetch("https://techtrek.herokuapp.com/api/v1.0/transaction", requestOptions)
    .then(response => response.text())
    .then(result => dataFetched = result)
    .catch(error => console.log('error', error));


function Copy() {
  /* Get the text field */
  var copyText = document.getElementById("url");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /*For mobile devices*/

  /* Copy the text inside the text field */
  document.execCommand("copy");
  var p = document.createElement("p");
  p.innerHTML += 'Copied'

  document.getElementById("url_div").appendChild(p)

  setTimeout(function(){ 
    document.getElementById("url_div").removeChild(p);
  }, 1000);

  }
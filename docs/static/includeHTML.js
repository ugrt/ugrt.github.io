// Src: https://www.w3schools.com/howto/howto_html_include.asp
// This code will allow us to import HTML files that are used across multiple pages
// It means we can change them in one file as opposed to 12+


// How to use
// <script src="{{url_for('static',filename='includeHTML.js')}}"></script>

//    <div include-html="{{url_for('static',filename= 'FILE NAME IN SINGLE QUOTES' )}}"></div>
//    <script>
//        includeHTML();
//    </script>


function includeHTML() {
    var z, i, elmnt, file, xhttp;
    /* Loop through a collection of all HTML elements: */
    z = document.getElementsByTagName("*");
    for (i = 0; i < z.length; i++) {
        elmnt = z[i];
        /*search for elements with a certain atrribute:*/
        file = elmnt.getAttribute("include-html");
        if (file) {
            /* Make an HTTP request using the attribute value as the file name: */
            xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4) {
                    if (this.status == 200) { elmnt.innerHTML = this.responseText; }
                    if (this.status == 404) { elmnt.innerHTML = "Page not found."; }
                    /* Remove the attribute, and call this function once more: */
                    elmnt.removeAttribute("include-html");
                    includeHTML();
                }
            }
            xhttp.open("GET", file, true);
            xhttp.send();
            /* Exit the function: */
            return;
        }
    }
}
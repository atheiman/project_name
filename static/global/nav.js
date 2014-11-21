// Set active nav element based on url path

// get navLinks
navLinks = document.getElementsByClassName('nav-link');
// loop through navLinks
for (var i=0; i < navLinks.length; i++) {
    // generate regexp based on navLink href
    var patt = new RegExp(navLinks[i].href);
    // if URL contains the href of the link
    if (patt.test(document.URL)) {
        // mark the navLink's parent <li> as class active
        navLinks[i].parentElement.classList.add('active');
    }
}

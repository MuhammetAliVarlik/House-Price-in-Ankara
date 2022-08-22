var slideIndex = 1;
showSlides(slideIndex);
function plusSlides(n) {
showSlides(slideIndex += n);
}
function currentSlide(n) {
showSlides(slideIndex = n);
}
function showSlides(n) {
var i;
var slides = document.getElementsByClassName("mySlides");
var dots = document.getElementsByClassName("dot");
if (n > slides.length) {slideIndex = 1}    
if (n < 1) {slideIndex = slides.length}
for (i = 0; i < slides.length; i++) {
slides[i].style.display = "none";  
}
for (i = 0; i < dots.length; i++) {
dots[i].className = dots[i].className.replace("activebar", "");
}
slides[slideIndex-1].style.display = "block";  
dots[slideIndex-1].className += " activebar";
}
setInterval(function(){
slideIndex++;
showSlides(slideIndex);
},7000);
var src = document.getElementById("slidercontrol");
var clientX;
src.addEventListener('touchstart', function(e) {
// Cache the client X/Y coordinates
clientX = e.touches[0].clientX;  
}, false);
src.addEventListener('touchend', function(e) {
var deltaX;
// Compute the change in X and Y coordinates. 
// The first touch point in the changedTouches
// list is the touch point that was just removed from the surface.
deltaX = e.changedTouches[0].clientX - clientX;
if(deltaX>50){
slideIndex--;
showSlides(slideIndex);
// Process the data ... 
}
else if(deltaX<-50){
slideIndex++;
showSlides(slideIndex);
}
}, false);
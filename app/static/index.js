document.addEventListener("DOMContentLoaded", function(event) {
   
   const showNavbar = (toggleId, navId, bodyId, headerId) =>{
   const toggle = document.getElementById(toggleId),
   nav = document.getElementById(navId),
   bodypd = document.getElementById(bodyId),
   headerpd = document.getElementById(headerId)
   
   // Validate that all variables exist
   if(toggle && nav && bodypd && headerpd){
   toggle.addEventListener('click', ()=>{
   // show navbar
   nav.classList.toggle('show')
   // change icon
   toggle.classList.toggle('bx-x')
   // add padding to body
   bodypd.classList.toggle('body-pd')
   // add padding to header
   headerpd.classList.toggle('body-pd')
   })
   }
   }
   
   showNavbar('header-toggle','nav-bar','body-pd','header')
   
   /*===== LINK ACTIVE =====*/
   const linkColor = document.querySelectorAll('.nav_link')
   
   function colorLink(){
   if(linkColor){
   linkColor.forEach(l=> l.classList.remove('active'))
   this.classList.add('active')
   }
   }
   linkColor.forEach(l=> l.addEventListener('click', colorLink))
   
    // Your code to run since DOM is loaded and ready
   });
   
   // slider start
   const slider = document.querySelector('.slider');
const slides = slider.querySelectorAll('li');

// Store the total number of images
const slideCount = slides.length;
let activeSlide = 0;

// To change the images dynamically every
// 5 Secs, use SetInterval() method
setInterval(() => {
  slides[activeSlide].classList.remove('active');
  activeSlide++;
  if (activeSlide === slideCount) {
     activeSlide = 0;
  }
  slides[activeSlide].classList.add('active');
}, 2000);

function logohide(){
   var element1=document.getElementById("logoshow");
   element1.classList.toggle("mystyle1");
   var element=document.getElementById("logoimg");
element.classList.toggle("mystyle");
}
// function logoshow(){
//     var element=document.getElementById("logoshow");
//     element.classList.toggle("mystyle1");
//    }

// card animation

function opencard(){
   var cardopen= document.getElementById("caption")
   cardopen.style.display="none";

}
function showcard(){
   var cardopen= document.getElementById("caption")
   cardopen.style.display="block";
}


document.getElementById(
   "containerlong").addEventListener(
       "mouseover", over);
document.getElementById(
   "containerlong").addEventListener(
       "mouseout", out);

function over() {
   document.getElementById(
       "caption").style.display = "none";
}
function out() {
   document.getElementById(
       "caption").style.display = "block";
}
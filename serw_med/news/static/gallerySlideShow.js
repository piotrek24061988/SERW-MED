var maxNumber = 4;
var number = Math.floor(Math.random()*maxNumber)+1;

function changeSlide() {
    number++;
    if(number > maxNumber) number = 1;

    var file = "<img src=\"/media/gallery/" + number + ".jpg\">";
    document.getElementById("galerrySlider").innerHTML = file;

    setTimeout("changeSlide()", 5000);
}
var maxNumber = 4;
var number = 0;

function changeSlide() {
    number++;
    if(number > maxNumber) number = 1;

    var file = "<img src=\"/media/gallery/" + number + ".jpg\">";
    document.getElementById("gallerySlider").innerHTML = file;

    setTimeout("changeSlide()", 5000);
}
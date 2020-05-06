var maxNumber = 4;
var number = 0;

function hideSlide() {
    $('#gallerySlider').fadeOut(1000);
}

function changeSlide() {
    number++;
    if(number > maxNumber) number = 1;

    var file = "<img src=\"/media/gallery/" + number + ".jpg\"/>";
    document.getElementById("gallerySlider").innerHTML = file;
    $('#gallerySlider').fadeIn(1000);

    setTimeout("hideSlide()", 4000);
    setTimeout("changeSlide()", 5000);
}
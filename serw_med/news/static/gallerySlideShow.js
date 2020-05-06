var maxNumber = 3;
var number = 0;
var playing = true;
var timer1 = 0;
var timer2 = 0;

function hideSlide() {
    if(playing) {
        $('#gallerySlider').fadeOut(1000);
    }
}

function replaceSlide(slideNumber) {
    if(playing) {
        var file = "<img src=\"/media/gallery/" + slideNumber + ".png\"/>";
        document.getElementById("gallerySlider").innerHTML = file;
        $('#gallerySlider').fadeIn(1000);
    }
}

function playSlide() {
    if(playing) {
        playing = false;
        var file = "<img src=\"/media/gallery/play.png\" onclick=\"playSlide()\"/>";
        document.getElementById("galleryPauseButton").innerHTML = file;
    } else {
        playing = true;
        var file = "<img src=\"/media/gallery/pause.png\" onclick=\"playSlide()\"/>";
        document.getElementById("galleryPauseButton").innerHTML = file;
    }
    resetTimers();
}

function resetTimers() {
    clearTimeout(timer1);
    clearTimeout(timer2);
    timer1 = setTimeout("hideSlide()", 4000);
    timer2 = setTimeout("changeSlide()", 5000);
}

function changeSlide() {
    number++;
    if(number > maxNumber) number = 1;

    replaceSlide(number);
    resetTimers();
}

function nextSlide() {
    number++;
    if(number > maxNumber) number = 1;

    replaceSlide(number);
    resetTimers();
}

function prevSlide() {
    number--;
    if(number == 0) number = maxNumber;

    replaceSlide(number);
    resetTimers();
}
jQuery(function($)
{
    $('#link1').click(function()
    {
        $.scrollTo($('#link1dent'), 1500);
    });

    $('#link2').click(function()
    {
        $.scrollTo($('#link2dent'), 1500);
    });

    $('#link3').click(function()
    {
        $.scrollTo($('#link3dent'), 1500);
    });

    $('#link4').click(function()
    {
        $.scrollTo($('#link4dent'), 1500);
    });

    $('#link5').click(function()
    {
        $.scrollTo($('#link5dent'), 1500);
    });

    //Scroll to top when button selected
    $('.scrollup').click(function()
    {
        $.scrollTo(0, 1500);
    });

    //Show / hide button depend os position
    $(window).scroll(function()
    {
        if($(this).scrollTop()>500) $('.scrollup').fadeIn();
        else $('.scrollup').fadeOut();
    });
});
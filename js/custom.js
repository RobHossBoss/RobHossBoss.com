$(function(){
    //Variables
    var slideqty = $('#featured .item').length; //get the number of slides in the carousel deck
    var wheight = $(window).height(); //get the height of the window
    var randSlide = Math.floor(Math.random()*slideqty); //pick a random number from 0-slideqty
    //makeIndicators
    //Automatically make indicators on the carousel for each slide in the deck
    for (var i=0; i < slideqty; i++) {
        var insertText = '<li data-target="#featured" data-slide-to="' + i + '"';
        if (i === 0) {
            insertText += ' class="active" ';
        }
        insertText += '></li>';
        $('#featured ol').append(insertText);
    }

    $('.carousel').carousel({
        pause: false
    }); // end of makeIndicator

     //replace IMG inside carousels with a background image
    $('#featured .item img').each(function() {
        var imgSrc = $(this).attr('src');
        $(this).parent().css({'background-image':'linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url('+imgSrc+')'});
        $(this).remove();
    });

    //fullHeight
    // set all elements with class "fullheight" to a height equal to height of viewport on load
    $('.fullheight').css('height', wheight);

    //resize the "fullheight" elements on screen resize
    $(window).resize(function() {
        wheight = $(window).height(); //get the height of the window
        $('.fullheight').css('height', (wheight)); //set to window tallness
    });

    //adjust the interval of the carousel
    $('.carousel').carousel({
        interval: 7000 //changes the speed in miliseconds
    })

    //make images darker
    $('.item img').each(function() {
        $(this).wrap('<div class="tint"></div>'); //wraps the carousel images with a div of class "tint"
    });

    //global getJSON for Posts
  

}); //end of main function

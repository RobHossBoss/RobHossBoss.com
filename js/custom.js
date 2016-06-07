
    $(document).ready(function(){
            var wheight = $(window).height()-50; //get the height of the window

        $('.fullheight').css('height', wheight);
                $('.halfheight').css('height', wheight/2);


    //resize the "fullheight" elements on screen resize
    $(window).resize(function() {
        wheight = $(window).height(); //get the height of the window
        $('.fullheight').css('height', (wheight)); //set to window tallness
                $('.halfheight').css('height', wheight/2);

    });

    $(".pill").click(function() { 
      $('.pill').removeClass('active');
      $(this).addClass('active');
    }); 
    $('.post').mouseenter(function(){
        $(this).find('.thumbnail').css('background-size', '110%');
    });
     $('.post').mouseleave(function(){
        $(this).find('.thumbnail').css('background-size', '100%');
    });

   
      $("[href^='/#']").on("click", function( e ) {

        var target = $(this).attr('href').substring(1);

        var scrollTop = $( target ).offset().top-$('nav').height();

        if ( target =='#home'){
           scrollTop = 0;
        }

        $("body, html").animate({
                scrollTop: scrollTop
            }, 800);

        e.preventDefault();


      });

      var imgs = document.getElementsByTagName('img');

    // loop through fetched images
    for (i = 0; i < imgs.length; i++) {
        // and define onmousedown event handler
        imgs[i].onmousedown = disableDragging;
    }
          var post = $('.thumbnail');
    // loop through fetched images
    for (i = 0; i < post.length; i++) {
        // and define onmousedown event handler
        post[i].onmousedown = disableDragging;
    }

function disableDragging(e) {
        e.preventDefault();
    }

/*
        var lastFixPos = 0;

$(window).on('scroll', function(){
  lastFixPos = $(window).scrollTop();
  console.log(lastFixPos);
  $("#motd").css("height",  wheight - lastFixPos);
  $("#motd").fadeTo(0, 1/(lastFixPos/70));

}); */
});



 //end of main function

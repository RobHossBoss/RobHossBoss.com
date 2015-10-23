$(function() {

	var slideqty = $('#featured .item').length;
	var topoffset = 50; //variable for menu height
	var wheight = $(window).height(); //get the height of the window
	var randSlide = Math.floor(Math.random()*slideqty);
	var seriesqty = $('.post-preview .post-series').length;

	$('.fullheight').css('height',wheight); //set to the window height
	$('.subheading').css('top',wheight - 100); //place social buttons at bottom of viewport
	//adjust height of image on window resize
	$(window).resize(function() {
		wheight = $(window).height();
		$('.fullheight').css('height', wheight);

	});
	//adjust placement of social buttons
	$(window).resize(function() {
		wheight = $(window).height();
		$('.subheading').css('top', wheight - 100);

	});
	//replace ING inside carousels with a background image
	$('#featured .item img').each(function() {
        var imgSrc = $(this).attr('src');
        $(this).parent().css({'background-image': 'url('+imgSrc+')'});
        $(this).remove();
    });

    $('.carousel').carousel({
        interval: '10000',
    });
//Use smooth scrolling when clicking on navigation
    $('.navbar a[href*=#]:not([href=#])').click(function() {
        if (location.pathname.replace(/^\//,'') ===
            this.pathname.replace(/^\//,'') &&
            location.hostname === this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: target.offset().top+2
                }, 500);
                return false;
            } //target.length
        } //click function
    }); //smooth scrolling

    for (var i=0; i < slideqty; i++) {
        var insertText = '<li data-target="#featured" data-slide-to="' + i + '"';
        if (i === randSlide) {
            insertText += ' class="active" ';
        }
        insertText += '></li>';
        $('#featured ol').append(insertText);
    }
    //make a post-preview div inside #fillup
    function makePostPreview(){
        $('#fillup').append('<div class="post-preview"/>');
    }
    //populate "post-preview" div with content
    function makeContentNodes(){
        $('.post-preview').append('<a class="post-link"/>');
        $('.post-preview').append('<p class="post-meta"/>');
        $('.post-link').append('<h2 class="post-title"/>');
        $('.post-link').append('<h3 class="post-subtitle"/>');
    }
    function makePosts(){
        $.getJSON('post-data.json', function(data){   
            $.each(data, function(key, val){
                makePostPreview();
                if ((key+1)==data.length){
                    makeContentNodes();
                }
            });
        });    
    }   
    makePosts();
 
    $.getJSON('/post-data.json', function(data){   
        $.each(data, function(key, val){
            $('.post-title').eq(key).html(val.title);
            $('.post-subtitle').eq(key).html(val.description);
            var date = 'Posted on ' + val.date + "."
            $('.post-meta').eq(key).html(date);
            $('.post-preview a').eq(key).attr("href", val.url);
            $('.post-preview').eq(key).css({
                'background-image': 'linear-gradient( rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.5) ), url(' + val.img + ')',
                'background-position': 'center'});
                console.log(data.length)
            
        });
    });


})


$(document).ready(function (){
    var Python = new Skill_bar('#Skill_1');
    var JS = new Skill_bar('#Skill_2');
    var HTML = new Skill_bar('#Skill_3');
    var CSS = new Skill_bar('#Skill_4');
    var CSharp = new Skill_bar('#Skill_5');
    var typed = new Typed('#typed', {
        strings: ["Hello World", "My name is Krishna","Welcome to my portfolio website"],
        typeSpeed: 70,
        backSpeed: 70,
        showCursor:  false
    });
    var navbar = new Waypoint({
        element: $(".js--section-portfolio-summary"),
        handler: function(direction){
            if(direction == "down"){
                $('nav').addClass('sticky-nav');
            }
            else{
                $("nav").removeClass('sticky-nav');
            }
        },
        offset: "30%"
    });

    $(function(){
        $('a[href*="#js-"]:not([href="#"])').click(function(){
            if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname){
                var target = $(this.hash);
                target == target.length ? target : $('[name='+this.hash.slice(1)+']');
                if(target.length){
                    $('html,body').animate({
                        scrollTop : target.offset().top-100
                    },1000);
                    return false;
                }
            }
        });
    });

    var scroll_1 = new Waypoint({
        element: $('.js--wp-1'),
        handler: function(direction){
            this.element.addClass("animated fadeIn");
        },
        offset: "60%"
    });

    var scroll_2 = new Waypoint({
        element: $('.js--wp-2'),
        handler: function(direction){
            this.element.addClass('animated fadeInUp');
            Python.animate_bar();
            
            JS.animate_bar();
            
            HTML.animate_bar();
            
            CSS.animate_bar();
            
            CSharp.animate_bar();
        },
        offset: "60%"
    });

    var scroll_3 = new Waypoint({
        element: $('.js--wp-3'),
        handler: function(direction){
            this.element.addClass('animated fadeInUp');
        },
        offset: "60%"
    });

    var scroll_4 = new Waypoint({
        element: $('.js--wp-4'),
        handler: function(direction){
            this.element.addClass('animated fadeInUp');
        },
        offset: "60%"
    });

    $('#inline-popups').magnificPopup({
    delegate: 'a',
    removalDelay: 500, //delay removal by X to allow out-animation
    callbacks: {
      beforeOpen: function() {
         this.st.mainClass = this.st.el.attr('data-effect');
      }
    },
    midClick: true // allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source.
    });
    $('#inline-popups_1').magnificPopup({
      delegate: 'a',
      removalDelay: 500, //delay removal by X to allow out-animation
      callbacks: {
        beforeOpen: function() {
           this.st.mainClass = this.st.el.attr('data-effect');
        }
      },
      midClick: true // allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source.
    });
});

class Skill_bar {
    constructor(id,color='#000000',color_from='#FA3D3D',color_to = '#74E800'){
        this.value = parseFloat($(id).text())/100;
        console.log(`${id} => ${this.value}`);
        this.color = color
        this.color_from = color_from
        this.color_to = color_to
        this.id = id
        this.skill_progress_bar = new ProgressBar.Circle(this.id, {
            color: this.color,
            // This has to be the same size as the maximum width to
            // prevent clipping
            strokeWidth: 4,
            trailWidth: 1,
            easing: 'easeInOut',
            duration: 2500,
            text: {
              autoStyleContainer: false
            },
            from: { color: this.color_from, width: 1 },
            to: { color: this.color_to, width: 4 },
            // Set default step function for all animate calls
            step: function(state, circle) {
              circle.path.setAttribute('stroke', state.color);
              circle.path.setAttribute('stroke-width', state.width);
          
              var value = Math.round(circle.value() * 100);
              if (value === 0) {
                circle.setText('');
              } else {
                circle.setText(value);
              }
          
            }
        });
    }

    animate_bar(){
        this.skill_progress_bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
        this.skill_progress_bar.text.style.fontSize = '2rem';
        this.skill_progress_bar.animate(this.value);
    }
}

// Prices calculator functionality
$('#indywidualne-tab, #grupowe-tab').click(function () {
    $('div[id^=\'coursesTabContent\'].tab-content div.tab-pane:first-child').addClass('active show');
})
$('#prices-section a[id$="-tab"].picker-button').click(function () {
    $(this).closest('ul').next().find('div[id^=\'coursesTabContent\'] .tab-pane').removeClass('active show');
    $(this).closest('ul').next().find('div[id^=\'coursesTabContent\'] .tab-pane:first-child').addClass('active show');
    $('.subject_selector').text('Wybierz kurs:');

})
// Tabs activation
var triggerTabList = [].slice.call(
    document.querySelectorAll('#lessonsTypeTab a, [id^=\'subscriptionTypeTab\'] a, [id^=\'lessonTimeTab\'] a, [id^=\'coursesTab\'] a')
)
triggerTabList.forEach(function (triggerEl) {
  var tabTrigger = new bootstrap.Tab(triggerEl)

  triggerEl.addEventListener('click', function (event) {
    event.preventDefault()
    tabTrigger.show()
  })
})
// Subjects selector
var trigger = $('.subject_selector');
var list = $('.list_of_subjects');
trigger.click(function() {
    list.slideDown(200);
    list.click(function() {
        list.slideUp(200);
    });
    $('.list_of_subjects .nav-item').click(function () {
        let subject = $(this).text();
        $('.subject_selector').text(subject);
    });
});


//Alignment
$(document).ready(function(){
    $('.container').each(function(){
        var highestBox = 0;
        $('.alignment', this).each(function(){
            if($(this).height() > highestBox) {
                highestBox = $(this).height();
            }
        });
        $('.alignment',this).height(highestBox);
    });

    $.getJSON("http://jsonip.appspot.com?callback=?",
        function(data){
            alert( "Your ip: " + data.ip);
        });

    $.getJSON("https://api.ipify.org/?format=json", function(e) {
        document.querySelector(".js-ip-address").value = e.ip;
    });
});
$(window).resize(function(){
    $(".alignment").css({"height":"100%"});
    $('.container').each(function(){
        var highestBox = 0;
        $('.alignment', this).each(function(){
            if($(this).height() > highestBox) {
                highestBox = $(this).height();
            }
        });
        $('.alignment',this).height(highestBox);
    });
});

//Steps
$('.progressbar .active').hover(
    function() {
        $( '.progressbar .active:before' ).addClass('custom-step');
        $( this ).find('.service-box-4').addClass('custom-step');
    }, function() {
        $( this ).find(':before').removeClass('custom-step');
        $( this ).find('.service-box-4').removeClass('custom-step');
    }
);

$('.sidebar .h2-what-we-list li').hover(
    function() {
        $( this ).find('span, a').addClass('courses-list');
    }, function() {
        $( this ).find('span, a').removeClass('courses-list');
    }
);

$('.accordion-step').click(function() {
    var id = $(this).attr('id');
    $('.progressbar li').removeClass('hovered');
    $('.progressbar li#li-' + id).toggleClass('hovered');
});

// Cookies bottom popup
(function() {
    //copyright JGA 2013 under MIT License
    var monster={set:function(e,t,n,r){var i=new Date,s="",o=typeof t,u="";r=r||"/",n&&(i.setTime(i.getTime()+n*24*60*60*1e3),s="; expires="+i.toGMTString());if(o==="object"&&o!=="undefined"){if(!("JSON"in window))throw"Bummer, your browser doesn't support JSON parsing.";u=JSON.stringify({v:t})}else u=escape(t);document.cookie=e+"="+u+s+"; path="+r},get:function(e){var t=e+"=",n=document.cookie.split(";"),r="",i="",s={};for(var o=0;o<n.length;o++){var u=n[o];while(u.charAt(0)==" ")u=u.substring(1,u.length);if(u.indexOf(t)===0){r=u.substring(t.length,u.length),i=r.substring(0,1);if(i=="{"){s=JSON.parse(r);if("v"in s)return s.v}return r=="undefined"?undefined:unescape(r)}}return null},remove:function(e){this.set(e,"",-1)},increment:function(e,t){var n=this.get(e)||0;this.set(e,parseInt(n,10)+1,t)},decrement:function(e,t){var n=this.get(e)||0;this.set(e,parseInt(n,10)-1,t)}};

    if (monster.get('cookieinfo') === 'true') {
        return false;
    }

    var container = document.createElement('div'),
        link = document.createElement('a');

    container.setAttribute('id', 'cookieinfo');
    container.setAttribute('class', 'cookie-alert');
    container.innerHTML =
        '<h6>This website uses cookies to provide services at the highest level</h6>' +
        '<p>By continuing to use the site, you agree to their use</p>';
    link.setAttribute('href', '#');
    link.setAttribute('title', 'Close');
    link.innerHTML = 'Agree';

    function clickHandler(e) {
        if (e.preventDefault) {
            e.preventDefault();
        } else {
            e.returnValue = false;
        }

        container.setAttribute('style', 'opacity: 1');

        var interval = window.setInterval(function() {
            container.style.opacity -= 0.01;

            if (container.style.opacity <= 0.02) {
                document.body.removeChild(container);
                window.clearInterval(interval);
            }
        }, 4);
    }

    if (link.addEventListener) {
        link.addEventListener('click', clickHandler);
    } else {
        link.attachEvent('onclick', clickHandler);
    }

    container.appendChild(link);
    setTimeout(function () {
        document.body.appendChild(container);
    }, 5000);

    monster.set('cookieinfo', 'true', 365);

    return true;
})();

//Prices tables
$(document).ready(function(){
    $( '.single-pricing.prt_2.show' ).mouseenter(function(){
        $(this).hide();
        $(this).next().show();
    });
    $( '.single-pricing.prt_2.hide' ).mouseleave(function(){
        $(this).hide();
        $(this).prev().show();
    });
});


// // Phone popup
// $('#popup__toggle').delay(10000).animate({'opacity':'1'},500);
// $('.speech').delay(15000).slideDown(500).delay(10000).fadeOut(3000);

// function przelewy24_ind35() {
//     if ($('#z24_nazwa_ind35').val() == 'Zajecia indywidualne (35 min), 8 lekcji w miesiacu') {
//         $('#z24_kwota_ind35').val(28000)
//     }
//     else if ($('#z24_nazwa_ind35').val() == 'Zajecia indywidualne (35 min), 12 lekcji w miesiacu') {
//         $('#z24_kwota_ind35').val(38400)
//     }
//     else if ($('#z24_nazwa_ind35').val() == 'Zajecia indywidualne (35 min), 16 lekcji w miesiacu') {
//         $('#z24_kwota_ind35').val(48000)
//     }
// }
// function przelewy24_ind55() {
//     if ($('#z24_nazwa_ind55').val() == 'Zajecia indywidualne (55 min), 4 lekcji w miesiacu') {
//         $('#z24_kwota_ind55').val(20000)
//     }
//     else if ($('#z24_nazwa_ind55').val() == 'Zajecia indywidualne (55 min), 8 lekcji w miesiacu') {
//         $('#z24_kwota_ind55').val(37600)
//     }
//     else if ($('#z24_nazwa_ind55').val() == 'Zajecia indywidualne (55 min), 12 lekcji w miesiacu') {
//         $('#z24_kwota_ind55').val(54000)
//     }
//     else if ($('#z24_nazwa_ind55').val() == 'Zajecia indywidualne (55 min), 16 lekcji w miesiacu') {
//         $('#z24_kwota_ind55').val(68800)
//     }
// }
// function przelewy24_gr55() {
//     if ($('#z24_nazwa_gr55').val() == 'Zajecia grupowe (55 min), 4 lekcji w miesiacu') {
//         $('#z24_kwota_gr55').val(10800)
//     }
//     else if ($('#z24_nazwa_gr55').val() == 'Zajecia grupowe (55 min), 8 lekcji w miesiacu') {
//         $('#z24_kwota_gr55').val(20000)
//     }
//     else if ($('#z24_nazwa_gr55').val() == 'Zajecia grupowe (55 min), 12 lekcji w miesiacu') {
//         $('#z24_kwota_gr55').val(26400)
//     }
//     else if ($('#z24_nazwa_gr55').val() == 'TEST: Zajecia grupowe (55 min), 12 lekcji w miesiacu') {
//         $('#z24_kwota_gr55').val(100)
//     }
// }


var $page = $('html, body');
$('.scrollto').click(function() {
    $page.animate({
        scrollTop: $($.attr(this, 'href')).offset().top
    }, 400);
    return false;
});

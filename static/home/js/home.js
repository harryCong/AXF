$(function () {

    var swiper = new Swiper('#topSwiper', {
      slidesPerView: 1,
      spaceBetween: 30,
      autoplay: 2500,
      loop: true,
      pagination: '.swiper-pagination',
    });

    var swiper1 = new Swiper('#mustbuySwiper', {
      slidesPerView: 3,
      spaceBetween: 10,
      loop: true,
    });

})
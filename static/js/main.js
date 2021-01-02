var typed = new Typed('#typed', {
    stringsElement: '#typed-strings',
    cursorChar:"_",
    typeSpeed:40,
    loop:true,
    loopDelay:200,
    backDelay:1000
  });

$('.terminal').tilt({
  glare:true,
  maxGlare:.1
});

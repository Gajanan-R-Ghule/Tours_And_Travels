document.getElementById('start').addEventListener('change', function () {
    document.getElementById('myForm').submit();
});
document.getElementById('start1').addEventListener('change', function () {
    document.getElementById('myForm').submit();
});


document.querySelectorAll('.navbar').forEach(link => {
  if (link.href === window.location.href) {
    link.classList.add('active');
  }
});





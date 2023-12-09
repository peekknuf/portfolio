document.getElementById('button1').addEventListener('click', function(event) {
    toggle(event, 'description1');
});
document.getElementById('button2').addEventListener('click', function(event) {
    toggle(event, 'description2');
});
document.getElementById('button3').addEventListener('click', function(event) {
    toggle(event, 'description3');
});
document.getElementById('button4').addEventListener('click', function(event) {
    toggle(event, 'description4');
});

function toggle(event, descriptionId) {
    var description = document.getElementById(descriptionId);
    
    if (description.style.display === 'none' || description.style.display === '') {
      event.target.innerText = 'Hide description';
      description.style.display = 'block';
    } else {
      event.target.innerText = 'Show full description';
      description.style.display = 'none';
    }
  }
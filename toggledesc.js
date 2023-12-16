
for (let i = 1; i <= 4; i++) {
  let buttonId = 'button' + i;
  let descriptionId = 'description' + i;
  let button = document.getElementById(buttonId);
  
  button.addEventListener('click', function(event) {
      toggle(event, descriptionId);
  });
}

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
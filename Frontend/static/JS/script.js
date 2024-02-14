// scripts.js
document.addEventListener('DOMContentLoaded', function() {
  // Handle offer form submission
  document.getElementById('offerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var text = document.getElementById('offerText').value;
    fetch('/analyze_offer', {
      method: 'POST',
      body: JSON.stringify({ text: text }),
      headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('results').innerHTML = JSON.stringify(data);
    });
  });

  // Handle resume upload
  document.getElementById('uploadButton').addEventListener('click', function() {
    document.getElementById('resumeInput').click();
  });

  document.getElementById('resumeInput').addEventListener('change', function(event) {
    var files = event.target.files;
    var formData = new FormData();
    for (var i =  0; i < files.length; i++) {
      formData.append('resumes[]', files[i]);
    }
    fetch('/parse_resumes', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      var skillsDiv = document.getElementById('parsedSkills');
      skillsDiv.innerHTML = '';
      data.forEach(skill => {
        var skillDiv = document.createElement('div');
        skillDiv.textContent = skill;
        var removeButton = document.createElement('button');
        removeButton.textContent = 'x';
        removeButton.onclick = function() {
          skillsDiv.removeChild(skillDiv);
        };
        skillDiv.appendChild(removeButton);
        skillsDiv.appendChild(skillDiv);
      });
    });
  });
});

document.addEventListener('DOMContentLoaded', function() {
 
  function displaySelectedCVs(files) {
   var cvListDiv = document.getElementById('cvList');
   cvListDiv.innerHTML = ''; // Efface le contenu précédent avant d'ajouter de nouveaux éléments

   var cvListHeading = document.createElement('h2');
   cvListHeading.textContent = 'Selected Resumes';
   cvListDiv.appendChild(cvListHeading);

   var ul = document.createElement('ul');
   for (var i = 0; i < files.length; i++) {
     var li = document.createElement('li');
     li.textContent = files[i].name;
    
     // Création du bouton de suppression
     var removeButton = document.createElement('button');
     removeButton.textContent = 'x';
     removeButton.className = 'remove-button'; // Ajout d'une classe pour le style ou l'écouteur d'événement
     removeButton.setAttribute('data-index', i); // Stocke l'index du fichier dans l'attribut data-index
    
     // Écouteur d'événement pour la suppression du fichier
     removeButton.addEventListener('click', function(event) {
       var index = event.target.getAttribute('data-index'); // Récupère l'index du fichier à supprimer
       var liToRemove = event.target.parentNode; // Obtient l'élément li parent du bouton
       liToRemove.parentNode.removeChild(liToRemove); // Supprime l'élément li de la liste
     });

     li.appendChild(removeButton); // Ajoute le bouton de suppression à l'élément li
     ul.appendChild(li);
   }
   cvListDiv.appendChild(ul);
 }

 // Gestion de l'upload des CV
 document.getElementById('uploadButton').addEventListener('click', function() {
   document.getElementById('resumeInput').click();
 });

 document.getElementById('resumeInput').addEventListener('change', function(event) {
   var files = event.target.files;
   displaySelectedCVs(files); // Appel de la fonction pour afficher les CV sélectionnés
 });
});

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
   })
 })


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
        skillsDiv.appendChild(skillDiv);
      });
    })
  })
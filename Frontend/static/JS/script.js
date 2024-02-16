document.addEventListener("DOMContentLoaded", function () {
  const offerForm = document.getElementById("offerForm");
  const resumeInput = document.getElementById("resumeInput");
  const cvList = document.getElementById("cvList");
  const downloadButton = document.getElementById("downloadButton");
  const loader = document.getElementById("loader");

  let resumes = [];

  // Event listener for resume selection
  document.getElementById("uploadButton").addEventListener("click", function () {
      resumeInput.click();
  });

  // Event listener for resume file selection
  resumeInput.addEventListener("change", function () {
      resumes = Array.from(resumeInput.files);
      updateCVList();
  });

  // Event listener for offer form submission
  offerForm.addEventListener("submit", function (event) {
      event.preventDefault();

      const jobOfferText = document.getElementById("offerText").value;

      // Show loader during submission
      loader.style.display = "block";

      // Create FormData object to send files
      const formData = new FormData();
      for (const resume of resumes) {
          formData.append('resumes', resume);
      }
      formData.append('jobOfferText', jobOfferText);

      // Call backend to process resumes and offer text
      fetch("/process", {
          method: "POST",
          body: formData,
      })
      .then(response => response.json())
      .then(data => {
          // Display results and enable download button
          document.getElementById("results").innerText = "Best matched resume: " + data.bestResume;
          downloadButton.setAttribute("data-bestResume", data.bestResume);
          downloadButton.style.display = "block";
      })
      .catch(error => console.error("Error:", error))
      .finally(() => {
          // Hide loader after completion
          loader.style.display = "none";
      });
  });

  // Event listener for download button
  downloadButton.addEventListener("click", function () {
      // Retrieve the best-matched resume file name from the data attribute
      const bestResume = downloadButton.getAttribute("data-bestResume");

      // Implement download functionality with the best-matched resume
      if (bestResume) {
          // You can use the bestResume value to construct the download URL
          const downloadURL = `/download?resume=${bestResume}`;
          
          // Redirect to the download URL or open it in a new tab
          window.location.href = downloadURL;
      }
  });

  // Update CV list on the webpage
  function updateCVList() {
      cvList.innerHTML = "";
      resumes.forEach(resume => {
          const li = document.createElement("li");
          li.innerText = resume.name;
          cvList.appendChild(li);
      });
  }
});
// Add this jQuery code in your script.js file

$(document).ready(function () {
  // Show loader when needed
  $('#loader-container').show();

  // Hide loader when the content is loaded
  // You can replace this with your actual logic for hiding the loader
  $(window).on('load', function () {
    $('#loader-container').hide();
  });

  // Toggle the loader's position when scrolling
  $(window).scroll(function () {
    var scrollPosition = $(window).scrollTop();
    var windowHeight = $(window).height();
    var loaderHeight = $('#loader-container').height();

    // Show loader at the middle of the screen when scrolling
    if (scrollPosition > windowHeight / 2) {
      $('#loader-container').css('top', '50%');
    } else {
      $('#loader-container').css('top', '0');
    }
  });
});

// Initialize storage
if (!localStorage.getItem("records")) {
  localStorage.setItem("records", JSON.stringify([]));
}
if (!localStorage.getItem("analysisHistory")) {
  localStorage.setItem("analysisHistory", JSON.stringify([]));
}

// Browse Files
function browseFiles() {
  document.getElementById("fileInput").click();
}

// Handle file selection
document.getElementById("fileInput")?.addEventListener("change", function(e) {
  if (this.files.length > 0) {
    const fileName = this.files[0].name;
    const displayElement = document.getElementById("selectedFileName");
    if (displayElement) {
      displayElement.innerText = "Selected: " + fileName;
      displayElement.style.color = "#2563eb";
      displayElement.style.fontWeight = "500";
      displayElement.style.marginTop = "10px";
    }
  }
});

// Upload + Analyze
function uploadAnalyze() {
  const fileInput = document.getElementById("fileInput");
  const patient = document.getElementById("patientId").value;
  const category = document.getElementById("category").value;
  const dept = document.getElementById("department").value;

  if (!fileInput.files.length || !patient || !category || !dept) {
    alert("Please complete all fields.");
    return;
  }

  const file = fileInput.files[0];

  // Save record to localStorage
  const records = JSON.parse(localStorage.getItem("records"));
  records.push({
    fileName: file.name,
    patient: patient,
    category: category,
    dept: dept,
    time: new Date().toLocaleString(),
    status: "Analyzed",
    analysis: {}
  });
  localStorage.setItem("records", JSON.stringify(records));

  // Save to history
  const history = JSON.parse(localStorage.getItem("analysisHistory"));
  history.push({
    date: new Date().toLocaleDateString(),
    patientId: patient,
    diagnosis: "Clinical analysis completed",
    risk: category === "Radiology" ? "High" : category === "Lab Report" ? "Medium" : "Low",
    recommendation: "Continue monitoring"
  });
  localStorage.setItem("analysisHistory", JSON.stringify(history));

  // Navigate to dashboard
  window.location.href = "dashboard.html";
}

// Load Dashboard
function loadDashboard() {
  const records = JSON.parse(localStorage.getItem("records"));
  const totalUploads = document.getElementById("totalUploads");
  const pending = document.getElementById("pending");
  
  if (totalUploads) totalUploads.innerText = records.length;
  if (pending) pending.innerText = 0;

  const table = document.getElementById("recordsTable");
  if (!table) return;

  table.innerHTML = "";
  records.forEach(r => {
    table.innerHTML += `
      <tr>
        <td>${r.fileName}</td>
        <td>${r.patient}</td>
        <td>${r.category}</td>
        <td>${r.dept}</td>
        <td>${r.time}</td>
      </tr>
    `;
  });
}

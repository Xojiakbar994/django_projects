/** @format */

function checkName() {
  let input_val = document.getElementById("name").value;
  if (input_val.includes(" ")) {
    alert("PROBEL yozilmasin");
    document.getElementById("name").value = "";
  }
}

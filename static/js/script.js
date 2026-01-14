
document.addEventListener("DOMContentLoaded", () => {
  const studentsLink = document.getElementById("studentsLink");
  const studentListCard = document.getElementById("studentListCard");

  console.log("studentsLink:", studentsLink);
  console.log("studentListCard:", studentListCard);

  if (!studentsLink || !studentListCard) return;

  studentsLink.addEventListener("click", (e) => {
    e.preventDefault();
    studentListCard.classList.toggle("show");
  });
});

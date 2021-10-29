const elements = document.querySelectorAll(".careerPoints");
const elementsOnE = document.querySelectorAll(".pinstcarrer");

elementsOnE.forEach(element => {
  const elemsntoeasd = element.textContent * 10;
  console.log(elemsntoeasd + 'px');
  element.style.height = elemsntoeasd + 'px';
});
function goToLunch(student) {
  //Instructions go here
  console.log(student + ", walk around desk");
  console.log(student + ", turn right");
  if(student.charAt(0)=='A')
  console.log(student + ", fly out the door");
  else
  console.log(student + ", swim out the door");
  return student.toUpperCase();
}
var student1 = "Alia";
var student2 = "John";
//goToLunch(student1);
//goToLunch(student2);

function add(firstNum, SecondNum) {
  return firstNum +SecondNum;
}

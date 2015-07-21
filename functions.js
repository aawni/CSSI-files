function aBitNervous(statement) {
  console.log(statement + " ...I think");
}

function todayILearned(statement) {
  console.log("Today I learned " + statement);
}

function salesTaxCheckout(subtotal) {
var total = subtotal + subtotal*.095;
return total;
}

function roll() {
return Math.random()*10;
}

function skeeballRater(score) {
  if (score<150) window.alert("You stink like garbage");
  else if (score<=250) window.alert("Not bad, but nothing to write home to mother about");
  else if (score<=350) window.alert("Looks like you're not a lost cause!");
  else if (score<=450) window.alert("So close to glory");
  else window.alert("You're a star!");
}

function fizzbuzz(num) {

  if (num%3===0 && num%5===0) console.log("fizzbuzz");
  else if (num%3===0) console.log("fizz");
  else if (num%5===0) console.log("buzz");
  else console.log("");
}

var students = ["Jewel", "Bex", "Alia"];

function printName(students) {
  for (var x=0;x<students.length; x++)
    console.log(students[x]);
}



var myArr = [];
myArr[0]="Hello";
myArr[2]=54.3;
myArr[3]=true;
myArr[1]="Stuff";
var fruits = ["apples", "oranges", "pears", "bananas"];
myArr = fruits;
myArr.push("strawberries");
myArr.pop();
myArr.splice(2, 0, "tiger");
myArr.splice(myArr.length-2, 1, "lion");
myArr.splice(3, 1);

var nums = [23, 4, 5, 8, 10]
function doubleNum(nums) {
  for (var x=0; x<nums.length; x++)
  {
    console.log(nums[x]*2);
  }
}

var favs= ["Inception", "Night Crawler", "Gigli"]
function myFavorites(favs) {
  var x=0;
  while (x<favs.length)
  {
    if (favs[x]!= "Demon Island" && favs[x]!="Gigli" && favs[x]!="Santa with Muscles")
    {
      window.alert(favs[x]+"? That's my favorite too!");
    }
    else
    {
      window.alert(favs[x]+"? That movie sucks!");
    }
    x++;
  }

}




//Deli
var line= []
function takeANum(line, name) {
  line.push(name);
  console.log(line.length);
}
function currentLine(line) {
  var output = "The line is currently: "
  for (var x=0;x<line.length;x++)
  {
    output += (x+1) + ". " + line[x] + " ";
  }
  if (line.length===0) output="There is nobody waiting to be served!";
  console.log(output);
}
function nowServing(line) {
  console.log("Currently serving " + line[0])
  line.splice(0,1);
}

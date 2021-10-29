/*
Arrays are list like objects.  They are used to store multiple values written as a list between square brackets, 
separated by commas
*/

var baseballTeams = ['Dodgers', 'Giants', 'Mets', 'Yankees', 'Astros'];

// add a value to the end of the array:
baseballTeams[5] = 'Cardinals';

console.log(baseballTeams)

baseballTeams[1] = "Angels";
baseballTeams[2] = 'Phillies'

function print(value){
    console.log(value);
}

print(baseballTeams);

var shoppingList = ['apples', 'pizza','chicken', 'mushrooms', 'orange', 'beef']
// adding in the front
shoppingList.unshift('crackers');
print(shoppingList);

// adding in the back
shoppingList.push('orange');
print(shoppingList);

print(shoppingList.length);

shoppingList.push('siracha', 'popcorn');

shoppingList.unshift('lemonade', 'orange juice');

print(shoppingList.length)
print(shoppingList)
// removing from the back
shoppingList.pop();
print(shoppingList);

// removing from the back
shoppingList.shift();
print(shoppingList);

print(shoppingList.length);

var firstItemSarah = shoppingList.shift();
var lastItemPhil = shoppingList.pop();

print(firstItemSarah);
print(lastItemPhil);
print(shoppingList);
print(shoppingList.length);

var colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'];
// building another array and add the two together.

var colors2 = ['back', 'white', 'brown', 'purple'];
var allColors = colors.concat(colors2);
print(allColors);

var colors3 = [ 'red', 'white', 'blue'];
var moreAllColors = colors.concat(colors2, colors3);

print(moreAllColors);

// reverse all the elements in the allColors array 
var reverseColors = allColors.reverse();
print("Reverse method: " + reverseColors)

// sort all the elements in the allColors array by alphabetical order
var alphabetColors = allColors.sort();
print("Sort method: "+ alphabetColors)

var weather = ['rainy', 'cold', 'chilly', 'snowy', 'cloudy', 'hot', 'warm', 'humid'];

// creating var winter and fill with winter values
var winter = weather.slice(0, 5);

// creating var summer and fill with summer values
var summer = weather.slice(5);

print(summer);
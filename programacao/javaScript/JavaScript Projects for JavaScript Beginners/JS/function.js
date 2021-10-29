
function print(value){
    return console.log(value);
}

// function declaration
function knockKnock(){
    return 'Who\'s there?'
}
// Calling the function
print(knockKnock());
// turn the function into an anonymous function within a function expressions 
var knockKnock = function(){
    return 'Who\'s there?'
}
// Value of the function
print(knockKnock);
// Calling the function
print(knockKnock());
// anonymous expressions

// IFFEs (Immediately Invoked Function Expressions);

var dogWalker = (function(person, dog){
    return person + ' is taking ' + dog + ' for a walk';
}('Paul', 'Charlei'));

print(dogWalker);
/*
function roadTrip(){
    var gallons = 12;
    var mpg = 34;
    return gallons * mpg;
}
print(roadTrip())
*/
var gallons = 12;
var mpg = 34;

function roadTrip(){
    return gallons * mpg;
}
print(roadTrip())

// Creating a nested function

// global scope
var height = 10;

function volume(){
    // parent scope
    var width = 10;
    var length = 10;
    var volumeOfObject = function() {
        // child or local scope
        return length * width * height;
    }
    return volumeOfObject();
}
print(volume());
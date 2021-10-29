/* 
Objects:
    A value type consisting of key/value pairs. 
    Anything that isn't a primitive (string, number, boolean, null, underfined, symbol)
    is an object

    variables -> properties
    functions -> methods
*/

// forma 1
var humanBeing = {
    hungry: true,
    age: 25,
    height: '5\'10'
};
// forma 2
var pizza = {};
pizza.crust = 'wheat';
pizza.sauce = 'marinara';
pizza.cheese = 'mozzarella';
pizza.toppings = 'cheese, pepperoni, olives, mushrooms';

// forma 3
var cup = {};
cup['insulated'] = true;
cul['liquid'] = 'wather';
cop['oz'] = 16;

var snowman = {
    isSnow: true,
    color: 'white',
    madeOfSnowballs: 3,
    'first name': 'Frosty'
}

function alertaUsuario(texto){
    alert(cup.insulated);
}
var button = document.getElementById('change-background');
var button2 = document.getElementById('change-background2');
var button3 = document.getElementById('change-background3');
var button4 = document.getElementById('change-background4');


button.addEventListener('click', function() {
    // action will go here
    document.body.style.backgroundColor = 'tomato';
});

button2.addEventListener('dblclick', function(){
    document.body.style.backgroundColor = 'blue';
});

button3.addEventListener('mouseenter', function(){
    document.body.style.backgroundColor ='yellow';
});

button4.addEventListener('mouseout', function(){
    document.body.style.backgroundColor = 'orange';
});

// appendChild() -> adds a node to the end of the list of children of a specified parent node
// removeChild() -> removes a child node from de DOM
// createElement() -> creates the HTML element specified by tagName
// firstChild -> read-only property returns the node's first child in the tree
/*




*/
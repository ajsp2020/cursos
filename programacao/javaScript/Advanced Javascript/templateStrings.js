function h1(strings, ...values){
    var body = "";
    for(var i = 0; i < strings.length; i++){
        console.log(strings[i]);
        body += strings[i] + (values[i] || "");
    }
    return `<h1>${body}</h1>`;
}
var name = "asim";
var place = "world";

console.log(h1`hello ${place} my name is ${name}`);
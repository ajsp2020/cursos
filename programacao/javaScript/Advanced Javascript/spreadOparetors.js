var meth = "Twitter";
var opts = ["key", "callbackUrl"];

function login(method, ...options){
    console.log(method);
    console.log(options);
}

login(meth, ...opts);
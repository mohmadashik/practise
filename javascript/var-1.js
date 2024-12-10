var a = 'hello'
var a = 34 /* will work since var allows redeclartion and redefinition */

const b = 87 

// const b = 8989 //will  throw a slipper in your face , no redeclarations for a const variable

// b = 'hello' // bro are you kidding me? it is a const variable you can't even redefine it

let y = 'mom'

y = 'dad' // will work dude. let allows redefinitions

// let y =98  // which brand are you drinking ? let won't allow redeclartions

const car = {'name':'maruthi'}
car['name'] = 'ford'  // now you are sober I think
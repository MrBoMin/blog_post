'use strict';

const restaurant = {
    name: 'Classico Italiano',
    location: 'Via Angelo Tavanti 23, Firenze Italy',
    categories: ['Italian', 'Pizzaeria', 'Vegetarian','Organic'],
    starterMenu: ['Focaccia','Bruschetta','Garlic','Bread','Caprese Salad'],
    mainMenu: ['Pizza','Pasta','Risotto'],
    openingHours : {
        thu: {
            open: 12,
            close: 22
        },
        fri: {
            open: 11,
            close: 23
        },
        sat: {
            open: 0,
            close: 24
        }
    },

    orders: function(starterIndex, mainMenuIndex){
        return [this.starterMenu[starterIndex], this.mainMenu[mainMenuIndex]];
    },

    orderDelivery: function(obj){
        console.log(obj);
    }
}


// Object Destructuring with Curly Brackets

// exact properties names from original objects
// order does not matter
// useful in API calls
const {name, openingHours, categories} = restaurant;
console.log(name,openingHours,categories);


// if we want the different names from properties name

const {name: restaurantName, openingHours: hours, categories: tags} = restaurant;
console.log(restaurantName, hours, tags);


// setting the default value
const {
    menu = [],
    starterMenu: starters = []
} = restaurant;

console.log(menu, starters);


// mutating the variables

let a = 111;
let b = 999;
const object = {a : 23, b : 7, c: 14};

// javascript treats the curly braces as code block, we can not assign the code block
// we can use parenthesis
({a,b} = object);

console.log(a,b)

//nested objects
const {fri: {open,close}} = openingHours
console.log(open,close)


restaurant.orderDelivery({
    time: '22:30',
    address: 'Yangon',
    mainIndex : 2,
    starterIndex : 2 
});
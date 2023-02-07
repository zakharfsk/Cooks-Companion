
let categories = document.querySelectorAll('.category'),
    backgrounds = [
        '#befbd4',
        '#FDE598',
        '#BEE8FF',
        '#FCA896',
        '#F2AFDF',
        '#7ED9BF',
        '#FFD698',
        '#FFFADD',
        '#DEF7FE',
        '#B5F2EA',
        '#FDEED9',
        '#C6D8FF',
    ];

    function rand(number1, number2){  // функція рандома 
        return Math.floor(Math.random() * (number2 - number1 + 1) + number1);
    }

    categories.forEach((category) => {
        category.style.backgroundColor = backgrounds[rand(0, backgrounds.length - 1)];
    });
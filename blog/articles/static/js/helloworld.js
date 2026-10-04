var outlets = [
    {
        "name": "Павильон 1-05",
        "tenant": "ООО «Модный дом»",
        "floor": "1",
        "payments": [93000, 93000, 90000]
    },
    {
        "name": "Павильон 1-12",
        "tenant": "ИП Гришин А. В.",
        "floor": "1",
        "payments": [46500, 46500, 45000]
    },
    {
        "name": "Островок 2-03",
        "tenant": "ООО «Кофе Тайм»",
        "floor": "2",
        "payments": [31000, 31000, 30000]
    },
    {
        "name": "Павильон 2-17",
        "tenant": "АО «ЭлектроМаркет»",
        "floor": "2",
        "payments": [150000, 155000, 150000]
    },
    {
        "name": "Павильон 3-08",
        "tenant": "ООО «Детский мир игрушек»",
        "floor": "3",
        "payments": [75000, 77500, 75000]
    },
    {
        "name": "Островок 3-01",
        "tenant": "ИП Назарова Л. С.",
        "floor": "3",
        "payments": [24800, 24000, 24800]
    }
];

var rpad = function(str, length) {
    // js не поддерживает добавление нужного количества символов
    // справа от строки, т.е. аналога ljust из Python здесь нет
    str = str.toString(); // преобразование в строку
    while (str.length < length)
        str = str + ' '; // добавление пробела в конец строки
    return str; // когда все пробелы добавлены, возвратить строку
};

var printOutlets = function(items) {
    console.log(
        rpad("Торговая точка", 16),
        rpad("Арендатор", 28),
        rpad("Этаж", 8),
        rpad("Платежи, руб.", 24)
    );
    // был выведен заголовок таблицы
    for (var i = 0; i <= items.length - 1; i++) {
        // в цикле выводится каждая запись
        console.log(
            rpad(items[i]['name'], 16),
            rpad(items[i]['tenant'], 28),
            rpad(items[i]['floor'], 8),
            rpad(items[i]['payments'], 24)
        );
    }
    console.log('\n'); // добавляется пустая строка в конце вывода
};

// фильтрация по этажу
var filterByFloor = function(items, group) {
    var result = [];
    for (var i = 0; i < items.length; i++) {
        if (items[i]['floor'] == group)
            result.push(items[i]);
    }
    return result;
};

// фильтрация по среднему ежемесячному платежу
var filterByAveragePayment = function(items, minAverage) {
    var result = [];
    for (var i = 0; i < items.length; i++) {
        var values = items[i]['payments'];
        var sum = 0;
        for (var j = 0; j < values.length; j++)
            sum = sum + values[j];
        if (sum / values.length > minAverage)
            result.push(items[i]);
    }
    return result;
};

printOutlets(outlets);

var group = prompt("Введите номер этажа для фильтрации:");
console.log("Торговые точки на этаже " + group + ":");
printOutlets(filterByFloor(outlets, group));

var minAverage = parseFloat(prompt("Введите минимальный средний платеж:"));
console.log("Торговые точки со средним платежом выше " + minAverage + ":");
printOutlets(filterByAveragePayment(outlets, minAverage));

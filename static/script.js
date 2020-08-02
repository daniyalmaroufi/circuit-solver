let selectedItem = 'Battery';
$("#selectedelement").html("Selected Element: " + selectedItem);
const elements = ['Battery', 'Current', 'Resistor'];
let nodeCount = 0;
let canvasElements = [];

function renderSidebar() {
    let sidebar = document.getElementById("sidebar");
    for (i in elements) {
        sidebar.innerHTML += (`<img src="${"./static/img/" + elements[i] + ".png"}"
								onclick="console.log(selectedItem = '${elements[i]}');$('#selectedelement').html('Selected Element: ' + selectedItem);"
								class="sidebar-element"
								id="${elements[i]}"
								/>\n`);
    }
}

function createEl(event) {
    let coord = { x: event.pageX, y: event.pageY };
    let canvas = document.getElementById("canvas");
    let neg = Number(prompt("Enter the node number connected to the negative/left side of this element:"));
    let pos = Number(prompt("Enter the node number connected to the positive/right side of this element:"));
    var value;
    value = Number(prompt("Please enter this element's value:"));

    $.ajaxSetup({
        async: false
    });
    const map = {
        'Battery': 'IV',
        'Current': 'IC',
        'Resistor': 'R'
    };
    const statement = `${map[selectedItem]} ${neg} ${pos} ${value}`;
    console.log('statement: ', statement)

    $.ajax({
        type: 'POST',
        contentType: 'application/json;charset-utf-08',
        dataType: 'json',
        url: `/state/${statement}`,
        success: (data, textStatus, jQxhr) => {
            if (textStatus == 'success') console.log('successfully sent data and response is: ', data);
            else console.error('data: ', data, '\n jQxhr: ', jQxhr);
        }
    });
    canvasElements.push({ "type": selectedItem, "points": { "neg": neg, "pos": pos }, "value": value });


    canvas.innerHTML += (
        (`<div class="canvas-element"
	style="left:${coord.x - 5}px;top:${coord.y - 70}px;">
	<p style="bottom: -20px;position: relative;">${value}</p>
	<div class="inner-el">
	<p>${neg}</p>
	<img class="canvas-img" src="${'./static/img/' + selectedItem + '.png'}" style="width: 50px">
	<p>${pos}</p>
	</div>
	</div>`))
}

$("#calc-btn").click(() => {
    $.ajaxSetup({
        async: false
    });
    const prevs = [];
    $.ajax({
        type: 'POST',
        url: '/state/calculate',
        success: (data) => {
            $("#results").html(data);
        }
    });
    return false;
});


$("#reset-btn").click(() => {
    location.reload();
});

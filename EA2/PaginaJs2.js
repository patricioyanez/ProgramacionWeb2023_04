function sumar(){
    var n1 = document.getElementById("num1").value;
    var n2 = document.getElementById("num2").value;
    let total = parseInt(n1) + parseInt(n2);
    document.getElementById("res").value = total;
}

// Ejercicios: Agregar botones y funciones para realizar:
// resta, multiplicación y división (evitar dividir por cero).

function restar(){
    var n1 = document.getElementById("num1").value;
    var n2 = document.getElementById("num2").value;
    let total = parseInt(n1) - parseInt(n2);
    document.getElementById("res").value = total;
}
function dividir(){
    var n1 = document.getElementById("num1").value;
    var n2 = document.getElementById("num2").value;
    n1 = parseInt(n1)
    n2 = parseInt(n2)
    
    if(n2 == 0)
    {
        alert("No se puede dividir por cero");
        return false;
    }

    let total = n1/n2;
    document.getElementById("res").value = total;
}
function multiplicar(){
    var n1 = document.getElementById("num1").value;
    var n2 = document.getElementById("num2").value;
    let total = parseInt(n1) * parseInt(n2);
    document.getElementById("res").value = total;
}

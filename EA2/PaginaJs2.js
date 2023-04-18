function miFuncion(){
    var n1 = document.getElementById("num1").value;
    var n2 = document.getElementById("num2").value;
    let total = parseInt(n1) + parseInt(n2);
    document.getElementById("res").value = total;
}

// Ejercicios: Agregar botones y funciones para realizar:
// resta, multiplicación y división (evitar dividir por cero).
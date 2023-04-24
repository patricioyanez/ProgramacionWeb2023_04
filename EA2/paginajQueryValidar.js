$(function()
{
    let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,4})+$/
    $('.btnAceptar').click(function()
    {
        if(!$('.txtRut').val())
        {
            alert('Falta el rut');
            $('.txtRut').focus();
        }
        else if(!$('.txtDv').val())
        {
            alert('Falta el dv');
            $('.txtDv').focus();
        }
        else if(!$('.txtNombre').val())
        {
            alert('Falta el nombre');
            $('.txtNombre').focus();
        }
        else if(!emailRegex.test($('.txtEmail').val()))
        { //verifica que el formato del correo este correcto
            alert('El formato del correo no es correcto');
            $('.txtEmail').focus();
        }
    });
    $('.btnLimpiar').click(function()
    {
        $('.txtRut, .txtDv, .txtNombre').val('');
        $('.txtRut').focus();
    });

    // definir patrones de caracteres a permitir
    let numeros = '123457890';
    let letras = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMÁÉÍÓÚáéíóú ';

    $('.txtRut').keypress(function(e)
    {
        // obtiene el codigo del caracter presionado y es convertido a 
        // el mismo caracter
        let caracter = String.fromCharCode(e.which); 
        if(numeros.indexOf(caracter)<0) // verifica si el caracter esta en el patrón
            return false; // evita que se escriba el caracter presionado
    });
    $('.txtDv').keypress(function(e)
    {
        // obtiene el codigo del caracter presionado y es convertido a 
        // el mismo caracter
        let dv = numeros + 'kK';
        let caracter = String.fromCharCode(e.which); 
        if(dv.indexOf(caracter)<0) // verifica si el caracter esta en el patrón
            return false; // evita que se escriba el caracter presionado
    });
    $('.txtNombre').keypress(function(e)
    {
        // obtiene el codigo del caracter presionado y es convertido a 
        // el mismo caracter
        let caracter = String.fromCharCode(e.which); 
        if(letras.indexOf(caracter)<0) // verifica si el caracter esta en el patrón
            return false; // evita que se escriba el caracter presionado
    });
})
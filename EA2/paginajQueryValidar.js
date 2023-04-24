$(function()
{
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
    });
})
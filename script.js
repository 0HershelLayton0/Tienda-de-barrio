function openSidebar() {
  document.querySelector('.sidebar').classList.toggle('open');
}

// Obtener el contenedor donde se mostrarán las imágenes
var contenedor = document.getElementById("contenedor-imagenes");

// Obtener los elementos del DOM
const enlacesSidebar = document.querySelectorAll('.sidebar li a');
const subpaginas = document.querySelectorAll('.main-content div');

// Recorrer los enlaces del sidebar
enlacesSidebar.forEach((enlace, i) => {
    // Agregar un evento click a cada enlace
    enlace.addEventListener('click', function(e) {
        e.preventDefault();

        // Ocultar todas las subpáginas
        subpaginas.forEach((subpagina) => {
            subpagina.style.display = 'none';
        });

        // Mostrar la subpágina correspondiente al enlace
        subpaginas[i].style.display = 'flex';
        
        document.querySelector('.sidebar').classList.toggle('open');
    });
});


var t=0;
function ampliarImg(imagen){
    document.getElementById('ampliada').src=imagen.src;
    document.getElementById('ampliada').style.display='block';
}
function quitar(){
    document.getElementById('ampliada').src='';
}
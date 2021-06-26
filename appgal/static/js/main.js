$(document).ready(function (){
	$('#subir').click(agragarImagen)
});

const addImage = (base64) => {
	let div = `<div class="contenedor">
			<img src="${base64}" alt="Imagen Normal">
			<p>Nombre Normal</p>
		</div>`;
	$(".galeria").append(div);
	$('#myfile').val('');
}

function agragarImagen(){
	const imagen = $('#myfile')[0].files[0];
	let reader = new FileReader();

	reader.onloadend = function () {
		// preview.src = reader.result;
		addImage(reader.result);
	}

	if (imagen){
		reader.readAsDataURL(imagen);
	}
}
$(document).ready(function (){
	$('#subir').click(agragarImagen)
})

function agragarImagen(){
	const imagen = $('#myfile').val()
	if (imagen != ''){
		let div = `<div class="contenedor">
				<img src="${imagen}" alt="${imagen.split('\\').pop()}">
				<p>${imagen.split('\\').pop()}</p>
			</div>`;
		$(".galeria").append(div);
		$('#myfile').val('');
	}
}
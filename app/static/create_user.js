$(document).ready(function () {
  $('label[for="id_comissao"]').hide();
  $("#id_comissao").hide();

  $("#id_tipo").on("change", function () {
    var tipo = $("#id_tipo").val();

    if (tipo == "COMISSIONADO") {
      $("#id_comissao").show();
      $('label[for="id_comissao"]').show();
    } else {
      $('label[for="id_comissao"]').hide();
      $("#id_comissao").hide();
    }
  });
});

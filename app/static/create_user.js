$(document).ready(function () {
  console.log("oi");
  $("#id_data_pagamento").datepicker({
    changeYear: true,
    changeMonth: true,
  });

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

// $(document).ready(function () {
//   //DATE PICKER CONFIG
//   console.log(1);
//   $("#id_data_ponto").datepicker({ changeYear: true, changeMonth: true });
// });

$(document).ready(function () {
  var dateToday = new Date();


  $("#id_taxa_sindicato").hide();
  $('label[for="id_taxa_sindicato"]').hide();

  $('label[for="id_comissao"]').hide();
  $("#id_comissao").hide();

  $("#id_sindicato").on("change", function () {
    option = $("#id_sindicato option:selected").text();

    if (option == "Yes") {
      $('label[for="id_taxa_sindicato"]').show();
      $("#id_taxa_sindicato").show();
    } else {
      $("#id_taxa_sindicato").hide();
      $('label[for="id_taxa_sindicato"]').hide();
    }
  });

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

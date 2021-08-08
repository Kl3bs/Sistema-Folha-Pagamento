$(document).ready(function () {
  $("#salvar_data").prop("disabled", true);

  $("#nova_data").datepicker({ changeYear: true, changeMonth: true });

  $("#botao").click(function () {
    $("#exampleModal").modal("show");
  });

  $(".close").click(function () {
    $("#exampleModal").modal("hide");
  });

  $("#nova_data").on("change", function () {
    $("#salvar_data").prop("disabled", false);
  });

  $("#salvar_data").click(function () {
    data = $("#nova_data").val();
    id = $("#user_id").val();

    console.log(data);
    console.log(id);
    $.post(`agenda_pagamento/${id}/${data}`);
  });
});

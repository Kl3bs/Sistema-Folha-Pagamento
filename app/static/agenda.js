  const csrftoken = Cookies.get("csrftoken");

  var funcionario_id;

  function getId(id) {
    funcionario_id = id;
  }

  $("#salvar_data").prop("disabled", true);

  var dateToday = new Date();
  $("#nova_data").datepicker({
    changeYear: false,
    changeMonth: false,
    minDate: dateToday,
    maxDate: "+15d",
    dateFormat: "dd-M-yy",
  });

  $(".botao").click(function () {
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
    data = `${data[0]}${data[1]}`  
    
    $.post(`agenda_pagamento/${funcionario_id}/${data}`, {
      csrfmiddlewaretoken: csrftoken,
    });

    window.location.reload()

  });

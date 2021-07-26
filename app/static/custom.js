$(document).ready(function () {
  $("#id_data_ponto").datepicker({ changeYear: true, changeMonth: true });

  $("#id_data_venda").datepicker({ changeYear: true, changeMonth: true });

  //TIME PICKER CONFIG

  // $("#id_valor_venda").mask("0000.000");

  $("#id_hora_entrada").timepicker({
    timeFormat: "HH:mm",
    interval: 60,
    minTime: "8",
    maxTime: "6:00pm",
    defaultTime: "8",
    startTime: "08:00",
    dynamic: false,
    dropdown: true,
    scrollbar: true,
  });

  $("#id_hora_saida").timepicker({
    timeFormat: "HH:mm",
    interval: 60,
    minTime: "8",
    maxTime: "6:00pm",
    defaultTime: "18",
    startTime: "08:00",
    dynamic: false,
    dropdown: true,
    scrollbar: true,
  });
});

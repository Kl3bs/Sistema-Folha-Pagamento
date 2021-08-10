$(document).ready(function () {
  //DATE PICKER CONFIG
  var dateToday = new Date();

  $("#id_data_ponto").datepicker({
    changeYear: false,
    changeMonth: false,
    minDate: dateToday});

  $("#id_data_venda").datepicker({
    changeYear: false,
    changeMonth: false,
    minDate: dateToday,});

  //TIME PISCKER CONFIG

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

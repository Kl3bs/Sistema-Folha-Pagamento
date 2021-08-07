$(document).ready(function () {
  //   $("#aplicar_taxa").click(aplicarTaxa());
});

const csrftoken = Cookies.get("csrftoken");

function aplicarTaxa(pk) {
  value = parseInt(prompt("Insira o valor da taxa: "));

  //Aceita somente números no prompt
  while (!/^[0-9]+$/.test(value)) {
    alert("Por favor, insira um número!");
    value = parseInt(prompt("Insira o valor da taxa: "));
  }

  $.post(`aplicar_taxa/${pk}/${value}`, {
    csrfmiddlewaretoken: csrftoken,
  });

  window.location.reload();

  // console.log(typeof value);
}

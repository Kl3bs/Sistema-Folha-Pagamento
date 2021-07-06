(function (win, doc) {
  "use strict";

  //Script para onfirmar exclusão de dado
  if (document.querySelector(".btnDel")) {
    let btnDel = doc.querySelectorAll(".btnDel");
    for (let i = 0; i < btnDel.length; i++) {
      btnDel[i].addEventListener("click", function (event) {
        if (confirm("Desejar realmente excluir este funcionário?")) {
          return true;
        } else {
          event.preventDefault();
        }
      });
    }
  }
})(window, document);

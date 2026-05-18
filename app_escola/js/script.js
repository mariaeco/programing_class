const form_gestor = document.getElementById("login-escola");

form_gestor.addEventListener("submit", function(event) {

    event.preventDefault(); //PREVINIR O PROCESSAMENTO DA PAGINA


    //NO FUTURO - SUBSTITUIREMOS PELO BANCO DE DADOS
    let inep = "25090909"
    let senha = "1234"

    let userINEP = document.getElementById("inep").value;
    let userSenha = document.getElementById("senha").value;

    // verificando se a função está funcionando
    console.log(userINEP)
    console.log(userSenha)

    if (userINEP === inep && userSenha === senha) {
        alert("Login realizado com Sucesso!");
        window.location.href = "home_gestor.html"
    } else {
        alert("Usuário ou senha incorretos!");
    }

    


});
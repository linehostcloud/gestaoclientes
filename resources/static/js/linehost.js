document.addEventListener("DOMContentLoaded", function() {

    // Esta é uma função de formatação geral que formatará uma string com base no tipo (CPF, CNPJ, CEP) especificado.
    let formatar = (str, tipo) => {
        // Remove todos os caracteres não numericos.
        str = str.replace(/\D/g, '');

        // Formatos variam com base no tipo.
        switch(tipo) {
            case 'CNPJ': // Para CNPJ
                return str
                    .replace(/(\d{2})(\d)/, '$1.$2')
                    .replace(/(\d{3})(\d)/, '$1.$2')
                    .replace(/(\d{3})(\d)/, '$1/$2')
                    .replace(/(\d{4})(\d)/, '$1-$2');
            case 'CPF': // Para CPF
                return str
                    .replace(/(\d{3})(\d)/, '$1.$2')
                    .replace(/(\d{3})(\d)/, '$1.$2')
                    .replace(/(\d{3})(\d)/, '$1-$2');
            case 'CEP': // Para CEP
                return str
                    .replace(/(\d{5})(\d{1,3})/, '$1-$2');
        }
    }

    // Esta função vai adicionar EventListeners para campos específicos baseado em seus IDs.
    // Uma função específica é chamada a cada vez que uma tecla é solta (keyup).
    // Cada valor de entrada é formatado de acordo com os formatos CNPJ, CPF ou CEP.
    function adicionarEventoParaCampo(id, tipo) {
        let campo = document.querySelector(id);
        campo.addEventListener("keyup", function(){
            campo.value = formatar(campo.value, tipo);
        });
    }

    // Adiciona event listeners para cada campo
    adicionarEventoParaCampo("#id_cnpj", 'CNPJ'); // CNPJ
    adicionarEventoParaCampo("#id_cpf", 'CPF'); // CPF
    adicionarEventoParaCampo("#id_cep", 'CEP'); // CEP

    // Busca informações de endereço a partir do CEP informado.
    let campoCEP = document.querySelector("#id_cep");
    campoCEP.addEventListener("blur", function() {
        fetch(`https://viacep.com.br/ws/${campoCEP.value}/json/`)
            .then(response => response.json())
            .then(data => {
                // Preenche automaticamente os campos de endereço com base nos dados recebidos.
                document.querySelector("#id_rua").value = data.logradouro;
                document.querySelector("#id_bairro").value = data.bairro;
                document.querySelector("#id_cidade").value = data.localidade;
                document.querySelector("#id_estado").value = data.uf;
            })
            .catch(error => console.error(error)); // Mostra erros no console se ocorrerem.
    });
});


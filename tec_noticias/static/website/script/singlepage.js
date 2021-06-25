function showSection(section) {
    document.querySelector('#fig_quizz').style.display = 'none'; // faz desaparecer o resultado do quizz
    document.querySelector('#fig_coments').style.display = 'none'; // faz desaparecer o resultado dos comentarios
    document.querySelectorAll('div').forEach(div => {
        div.style.display = 'none';
    });
    document.querySelector(`#${section}`).style.display = 'block';
    if(section != "apple" && section != "windows" && section != "linux")
    {
     document.querySelector(`#${section}`).style.display = 'block';
     fetch(`sections/${section}`)
    .then(response => response.text())
    .then(text =>
     document.querySelector(`#${section}`).innerHTML = text);
    }
}

document.addEventListener('DOMContentLoaded', function() {
     // envia pedido GET ao URL
        fetch('getNews')
        // converte a resposta em formato json
        .then(response => response.json())
        .then(data => {
            data.forEach(add_post_apple);
            data.forEach(add_post_windows);
            data.forEach(add_post_linux);
        })
        // Apanha erros e mostra-os na consola
        .catch(error => {
            console.log('Error:', error);
        });

        var id = 0;
       function add_post_apple(contents) {
       if(contents.categoria_id == 3)
       {
                const post = document.createElement('ul');
                post.className = 'post';

                const a = document.createElement('a');
                a.href = "#";
                a.onclick = function () {
                   showNews(contents);
                };


                const h1 = document.createElement('h1');
                h1.innerHTML = contents['titulo'];

                const p = document.createElement('p');
                p.innerHTML = "Autor: " + contents['autor'];

                const image = document.createElement('img');
                image.src = contents['imagem'];
                image.style.width  = "50%";
                image.style.height  = "50%";

                a.append(h1);
                a.append(p);
                a.append(image);
                post.append(a);

                // Add post to DOM
                document.querySelector('#apple').append(post);
       }
            };

                   function add_post_windows(contents) {
                if(contents.categoria_id == 1)
                {
                const post = document.createElement('ul');
                post.className = 'post';

                const a = document.createElement('a');
                a.href = "#";
                a.onclick = function () {
                            showNews(contents);
                };

                const h1 = document.createElement('h1');
                h1.innerHTML = contents['titulo'];

                const p = document.createElement('p');
                p.innerHTML = "Autor: " + contents['autor'];

                const image = document.createElement('img');
                image.src = contents['imagem'];
                image.style.width  = "50%";
                image.style.height  = "50%";

                a.append(h1);
                a.append(p);
                a.append(image);
                post.append(a);

                // Add post to DOM
                document.querySelector('#windows').append(post);
                }
            };

                   function add_post_linux(contents) {
                if(contents.categoria_id == 2)
                {
                const post = document.createElement('ul');
                post.className = 'post';

                const a = document.createElement('a');
                a.href = "#";
                a.onclick = function () {
                            showNews(contents);
                };

                const h1 = document.createElement('h1');
                h1.innerHTML = contents['titulo'];

                const p = document.createElement('p');
                p.innerHTML = "Autor: " + contents['autor'];

                const image = document.createElement('img');
                image.src = contents['imagem'];
                image.style.width  = "50%";
                image.style.height  = "50%";

                a.append(h1);
                a.append(p);
                a.append(image);
                post.append(a);

                // Add post to DOM
                document.querySelector('#linux').append(post);
                }
            };


            function showNews(contents){
                    id = contents['id'];
                document.querySelectorAll('div').forEach(div => {
                    div.style.display = 'none';
                });

                document.querySelector('#conteudo').style.display = 'block';
                document.querySelector('#noticia_titulo').innerHTML = contents['titulo'];
                document.querySelector('#noticia_data_autor').innerHTML = "Autor " + contents['autor'];
                document.querySelector('#noticia_imagem').src = contents['imagem'];
                document.querySelector('#noticia_imagem').style.width="50%";
                document.querySelector('#noticia_imagem').style.height="50%";
                document.querySelector('#noticia_texto').innerHTML = contents['descricao'];

                $.ajax({
                url : "devolveComentarios/" + contents['id'],
                headers: {'X-CSRFToken': csrftoken},
                mode:'same-origin',
                type : "GET",

                success : function(json) {
                if(json.length > 0){
                json.forEach(add_comments);
                }else{
                document.querySelector('#Comment').innerHTML = "Vazio !!";
                }

                },

                // handle a non-successful response
                error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
            });
            }


                $('#post-form').on('submit', function(event){
                    event.preventDefault();
                    const nome = document.querySelector('#author').value;
                    const texto = document.querySelector('#commentText').value;
                    create_post(id,nome,texto);
                });

            function add_comments(contents)
            {
                const h1 = document.createElement('li');
                h1.innerHTML = contents['autor'] +  " escreveu " + contents['texto'];
                document.querySelector('#Comment').innerHTML = contents['autor'] +  " escreveu " + contents['texto'];
            }

            function create_post(id,nome,texto) {
            console.log("id " + id + " none " + nome + " texto " + texto);
            $.ajax({
                url : "PostarComentario/",
                headers: {'X-CSRFToken': csrftoken},
                mode:'same-origin',
                type : "POST",
                data : { "id": id, "nome":nome,"texto":texto },

                // handle a successful response
                success : function(json) {
                    console.log("YESSSSS!!"); // another sanity check
                },

                // handle a non-successful response
                error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
            });
        };

    document.querySelectorAll('a').forEach(button => {
    button.onclick = function() {
        const section = this.dataset.section;
        history.pushState({section:section},"",`section${section}`);
        showSection(this.dataset.section);
        };
    });
});
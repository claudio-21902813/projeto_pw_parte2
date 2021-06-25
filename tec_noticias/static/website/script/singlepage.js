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
            }

    document.querySelectorAll('a').forEach(button => {
    button.onclick = function() {
        const section = this.dataset.section;
        history.pushState({section:section},"",`section${section}`);
        showSection(this.dataset.section);
        };
    });
});
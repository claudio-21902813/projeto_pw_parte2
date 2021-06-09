import json

def retornaDados():
    Noticias_API = {
        'Windows':[
            {
                'titulo': 'Atualização de maio de 2021 do Windows 10 começa a chegar a todos',
                'autor': 'CC',
                'data': '2021-03-12',
                'sinopse': 'Apesar de ser uma atualização menor, a Microsoft apostou em lançar a última versão do Windows 10 de forma lenta e controlada. '
                           'Com tantos problemas associados às atualizações,'
                           ' a empresa quis garantir que as situações anormais chegavam ao mínimo de utilizadores, corrigindo-as atempadamente.',
                'Texto': 'Apesar de ser uma atualização menor, a Microsoft apostou em lançar a última versão do Windows 10 de forma lenta e controlada. Com tantos problemas associados às atualizações, a'
                         ' empresa quis garantir que as situações anormais chegavam ao mínimo de utilizadores, corrigindo-as atempadamente.'
                         'Claro que tem como objetivo tornar pública esta nova atualização e isso começou agora. Está suportado com sistemas de inteligência artificial'
                         ', que assim ajudam a garantir que não existem problemas relevantes neste processo.',
                'imagem': 'https://pplware.sapo.pt/wp-content/uploads/2020/11/pplware_cores_windows_10_1.jpg'
            },
            {
                'titulo': 'A tecla Alt abre-lhe acesso a um novo lote de atalhos no teclado do Windows 10',
                'autor': 'CC',
                'data': '2021-02-12',
                'sinopse': 'O Windows 10, e outras versões anteriores, esconde algumas opções que muitos utilizadores desconhecem.',
                'Texto': '',
                'imagem': 'https://pplware.sapo.pt/wp-content/uploads/2020/08/pplware_win_key_windows_10_5.jpg'
            }
        ],
        'Linux':[
            {
                'titulo': 'Descarregar o Ubuntu via torrent leva utilizador a ser notificado por violar direitos de autor',
                'autor': 'CC',
                'data': '2021-02-12',
                'sinopse': 'Apesar de estar constantemente associado à pirataria e à violação de direitos de autor, os torrent têm em muitos casos outras utilizações.',
                'Texto': '',
                'imagem': 'https://pplware.sapo.pt/wp-content/uploads/2021/05/pirataria_torrent_1.jpg'
            },
            {
                'titulo': 'Bodhi Linux 6.0.0: Distro baseada no Ubuntu com interface levezinha',
                'autor': 'CC',
                'data': '2021-02-12',
                'sinopse': 'O Bodhi Linux é uma pequena, mas potente distribuição, que pode ser personalizada de acordo com as necessidades de cada utilizador.',
                'Texto': '',
                'imagem': 'https://pplware.sapo.pt/wp-content/uploads/2021/05/bodhi_00.jpg'
            }
        ],
        'Apple':[
                {
                    'titulo': 'Vem aí o Monterey! Conheça a nova versão do macOS',
                    'autor': 'CC',
                    'data': '2021-02-12',
                    'sinopse': 'Tal como previam os rumores, a nova versão do macOS poderia chamar-se Mammoth ou Monterey',
                    'Texto': '',
                    'imagem': 'https://pplware.sapo.pt/wp-content/uploads/2021/06/imagem-2021-06-07-as-19.21.38-768x431.jpg'
                },
                {
                    'titulo': 'iOS 15: Conheça as fantásticas novidades que estão para chegar',
                    'autor': 'CC',
                    'data': '2021-02-12',
                    'sinopse': 'Uma das peças bases do ecossistema da Apple é o iOS.',
                    'Texto': '',
                    'imagem': 'https://pplware.sapo.pt/wp-content/uploads/2021/06/imagem-2021-06-07-as-18.06.13-768x431.jpg'
                }
        ]
    }

    return json.dumps(Noticias_API)
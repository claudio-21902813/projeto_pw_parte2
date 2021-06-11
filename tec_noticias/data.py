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
                'texto': 'Apesar de ser uma atualização menor, a Microsoft apostou em lançar a última versão do Windows 10 de forma lenta e controlada. Com tantos problemas associados às atualizações, a'
                         ' empresa quis garantir que as situações anormais chegavam ao mínimo de utilizadores, corrigindo-as atempadamente.'
                         'Claro que tem como objetivo tornar pública esta nova atualização e isso começou agora. Está suportado com sistemas de inteligência artificial'
                         'Não sendo um processo que tenha corrido de forma pacífica nas últimas versões, as atualizações do Windows 10 têm sido muito mais controladas. '
                         'Com este controlo aplicado, a Microsoft evita trazer problemas aos utilizadores de forma generalizada, limitando as máquinas onde está presente.'
                         'Esta não será apresentada de forma automática, mas fará a instalação direta a quem satisfizer as condições da Microsoft e do Windows 10. '
                         'Este processo será aproveitado pela Microsoft para treinar os seus sistemas de machine learning, que vão ser úteis no futuro próximo deste processo.'
                         'Toda a informação recolhida irá depois ser usada para controlar a forma como a atualização será apresentada aos utilizadores. '
                         'Irá ser importante para detetar e controlar problemas que surjam no processo e que podem assim bloquear a chegada da atualização a mais máquinas.'
                         ', que assim ajudam a garantir que não existem problemas relevantes neste processo.',
                'imagem': 'https://pplware.sapo.pt/wp-content/uploads/2020/11/pplware_cores_windows_10_1.jpg'
            },
            {
                'titulo': 'A tecla Alt abre-lhe acesso a um novo lote de atalhos no teclado do Windows 10',
                'autor': 'CC',
                'data': '2021-02-12',
                'sinopse': 'O Windows 10, e outras versões anteriores, esconde algumas opções que muitos utilizadores desconhecem.',
                'texto': 'Uma das opções mais interessantes, para quem se habituou a usar o teclado, está na tecla Alt. '
                         'Se para muitos utilizadores serve simplesmente para alguns atalhos, a verdade é que se for explorada, '
                         'abre toda uma nova realidade aos utilizadores do Windows 10.'
                         'Para além do rato, o teclado permite um controlo muito grande no Windows 10. '
                         'Este sistema pode ser controlado na sua (quase) totalidade com este periférico, sem terem de recorrer a qualquer outro que já se habituaram a usar.'
                         'Claro que estes atalhos podem ser tornados ainda mais simples com uma pequena mudança no sistema da Microsoft. Desse momento em diante, e após carregar na tecla Alt, '
                         'só precisa de escolher a tecla que abre a opção do menu que está presente. Assim, tudo fica mais simples no Windows 10.'
                         'Comece por abrir as Definições e depois escolha a área Acessibilidade. Aqui dentro, deve escolher o separador Teclado, '
                         'para continuar todo este processo. Nesta nova área, deve descer e encontrar a opção Alterar a forma como os atalhos de teclado funcionam.',
                'imagem': 'https://pplware.sapo.pt/wp-content/uploads/2020/08/pplware_win_key_windows_10_5.jpg'
            }
        ],
        'Linux':[
            {
                'titulo': 'Descarregar o Ubuntu via torrent leva utilizador a ser notificado por violar direitos de autor',
                'autor': 'CC',
                'data': '2021-02-12',
                'sinopse': 'Apesar de estar constantemente associado à pirataria e à violação de direitos de autor, os torrent têm em muitos casos outras utilizações.',
                'texto': 'Apesar de estar constantemente associado à pirataria e à violação de direitos de autor, '
                         'os torrent têm em muitos casos outras utilizações. Existem muitos conteúdos a serem partilhados de forma totalmente legal.'
                         'Distribuições Linux são um desses exemplos, sendo até incentivada a partilha desta forma. '
                         'Assim, é muito estranho que um utilizador tenha recebido uma notificação após descarregar o Ubuntu via torrent.'
                         'Desde que a DMCA (Digital Millennium Copyright Act) foi criada em 1998, que as empresas podem enviar aos utilizadores alertas de violação de direitos de autor. '
                         'Estes são entregues aos ISPs, que depois os fazem chegar aos seus clientes.'
                         'Foi precisamente isso que aconteceu ao utilizador NateNate60 do Reddit, que acabou por reportar esta situação caricata e insólita. '
                         'Após descarregar a versão 20.4 do Ubuntu, pelo link fornecido no site da Canonical, acabou por receber uma notificação vinda do seu operador, a Comcast.'
                         'A notificação enviada deixa claro que não foi a Canonical a reportar a situação, mas sim a OpSec Security, '
                         'uma empresa alemã que até agora ainda não se manifestou e que terá agido de forma independente.',
                'imagem': 'https://pplware.sapo.pt/wp-content/uploads/2021/05/pirataria_torrent_1.jpg'
            },
            {
                'titulo': 'Bodhi Linux 6.0.0: Distro baseada no Ubuntu com interface levezinha',
                'autor': 'CC',
                'data': '2021-02-12',
                'sinopse': 'O Bodhi Linux é uma pequena, mas potente distribuição, que pode ser personalizada de acordo com as necessidades de cada utilizador.',
                'texto': 'O Bodhi Linux é uma pequena, mas potente distribuição, que pode ser personalizada de acordo com as necessidades de cada utilizador. '
                         'Esta distribuição é uma semi-rolling distro, baseada no Ubuntu e vem com um conjunto de '
                         'ferramentas pré-instaladas, como o Midori, LXTerminal, PCManFM, Leafpad ou o Synaptic.'
                         'Para quem procurar uma distribuição Linux com uma interface elegante e funcional, então o Bodhi Linux é sem dúvida uma excelente sugestão.'
                         'Esta distribuição oferece uma agradável experiência de utilização uma vez que garante a melhor performance, mesmo quando usado hardware mais antigo.'
                         'Novidades Bodhi Linux 6.0.0'
                         'Esta nova versão do Bodhi vem com várias novidades das quais se destacam:'
                         'Look ainda mais moderno com novos temas'
                         'Nova interface de Login'
                         'Thunar como gestor de ficheiros'
                         'Baseado no Ubuntu 20.04.2 LTS (Focal Fossa)'
                         'Chromium é agora o browser por omissão'
                         'Para realmente sentir o “feeling” deste sistema operativo é necessário que o instalem. '
                         'Pessoalmente gostei bastante da forma harmoniosa como o sistema se comporta e da interação entre utilizador e o próprio sistema operativo.',
                'imagem': 'https://pplware.sapo.pt/wp-content/uploads/2021/05/bodhi_00.jpg'
            }
        ],
        'Apple':[
                {
                    'titulo': 'Vem aí o Monterey! Conheça a nova versão do macOS',
                    'autor': 'CC',
                    'data': '2021-02-12',
                    'sinopse': 'Tal como previam os rumores, a nova versão do macOS poderia chamar-se Mammoth ou Monterey',
                    'texto': 'A Apple escolheu Monterey e será este o nome da nova versão do novo macOS (sucessor do macOS Big Sur). '
                             'O “conceito” já circulava na internet em alguns vídeos e hoje a Apple confirmou que este novo '
                             'sistema operativo é muito mais funcional e terá muitas novas funcionalidades que ajudarão os utilizadores a ser mais produtivos.'
                             'Com esta nova versão, a Apple promete também  mais interoperabilidade com outros sistemas da marca. Por exemplo, será possível partilhar um teclado e rato entre um Mac e um iPad.'
                             'O novo macOS irá trazer excelentes novidades ao nível das videochamadas e do teletrabalho, com a opção Focus. '
                             'A funcionalidade é semelhante ao que se pode encontrar nos teclados e ratos da Logitech, permitindo que o utilizador'
                             ' mova o cursor e transfira ficheiros entre um Mac e um iPad. Esta nova funcionalidade chama-se Universal Control.'
                             'A Apple também anunciou que os Macs irão receber o Shortcuts que estará associado ao Finder, barra de menu,'
                             ' Spotlight e Siri. Com esta funcionalidade será possível partilhar conteúdos entre dispositivos com um simples clique.',
                    'imagem': 'https://pplware.sapo.pt/wp-content/uploads/2021/06/imagem-2021-06-07-as-19.21.38-768x431.jpg'
                },
                {
                    'titulo': 'iOS 15: Conheça as fantásticas novidades que estão para chegar',
                    'autor': 'CC',
                    'data': '2021-02-12',
                    'sinopse': 'Uma das peças bases do ecossistema da Apple é o iOS.',
                    'texto': 'Este ano a Apple parece dedicada a melhorar as ferramentas que tem para a comunicação. '
                             'O centro destas é sem qualquer dúvida o FaceTime, que agora recebe um lote de novidades importantes.'
                             'Começamos com melhorias substanciais no áudio, com a chegada do Spatial Audio. '
                             'Há filtros que permitem agora isolar a voz e impedir que todos os ruídos estejam presentes.'
                             'A somar a isso há também novidades no vídeo, que permitem melhorar as chamadas em grupo, colocando todos no ecrã, de forma simples e direta.'
                             'Também com esta versão será possível agendar reuniões no FaceTime, com links diretos, que até podem '
                             'ser usadas noutros sistemas, pelo browser. A partilha de ecrã é também uma realidade, '
                             'para aumentar ainda mais as possibilidades, não se limitando ao vídeo, mas indo até ao áudio, no SharePlay.'
                             'O iMessage tem também novidades importantes, com a chegada do Shared with You. '
                             'Esta opção estará espalhada nos serviços da Apple e permite partilhar conteúdos com os utilizadores, que os podem ler mais tarde.'
                             'No campo das notificações, há melhorias que vão permitir fazer a sua gestão muito mais inteligente. '
                             'Os utilizadores têm agora um resumo das notificações, que podem ser lidas mais tarde, com tod aa calma.',
                    'imagem': 'https://pplware.sapo.pt/wp-content/uploads/2021/06/imagem-2021-06-07-as-18.06.13-768x431.jpg'
                }
        ]
    }

    return json.dumps(Noticias_API)
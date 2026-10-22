def cap6(r, D):
    r.chapter('Arquitetura e Implementação Proposta')
    r.para('Este capítulo descreve as tecnologias escolhidas, a arquitetura do sistema e da aplicação, as medidas de segurança e privacidade, a interface com o utilizador e o planeamento da implementação.')

    r.h2('Tecnologias')
    n = r.next_tab()
    r.para(f'A instituição definiu como obrigatórios o Kotlin e o Firebase. A Tabela {n} detalha as tecnologias e a justificação de cada escolha.')
    r.table(['Tecnologia', 'Utilização', 'Justificação'], [
        ['Kotlin', 'Linguagem das aplicações Android.', 'Linguagem recomendada pela Google para Android, concisa, com segurança de nulos e corrotinas para operações assíncronas (JetBrains, 2026).'],
        ['Jetpack Compose', 'Interface declarativa.', 'Padrão atual de UI em Android; menos código e melhor testabilidade (Google, 2026d).'],
        ['Arquitetura MVVM + Hilt', 'Organização em camadas e injeção de dependências.', 'Separação de responsabilidades e testes da camada de domínio (Google, 2026d; Martin, 2017).'],
        ['Firebase Authentication', 'Autenticação de colaboradores (email) e utentes (telemóvel).', 'Integrado com as regras de segurança; suporta *custom claims* para perfis.'],
        ['Cloud Firestore', 'Base de dados principal.', 'Sincronização em tempo real, cache local, transações e regras de segurança declarativas.'],
        ['Cloud Functions (TypeScript)', 'Regras de negócio críticas, transações, geração de PDF, tarefas agendadas.', 'Executam no servidor, impedindo que um cliente adulterado contorne as regras de stock.'],
        ['Cloud Storage', 'Imagens de guias e PDF gerados.', 'Armazenamento de ficheiros com regras de acesso.'],
        ['Cloud Messaging (FCM)', 'Notificações de alertas.', 'Notificações push por tópico (perfil).'],
        ['Firebase Hosting', 'Painel web da agenda.', 'Alojamento estático com HTTPS, no mesmo projeto.'],
        ['ML Kit Barcode Scanning', 'Leitura de QR de locais e credenciais.', 'Funciona no dispositivo, sem custos nem envio de imagens (Google, 2026c).'],
        ['Biblioteca PDF (ex.: pdfmake)', 'Geração do RGDHSA049.', 'Permite reproduzir o layout do modelo em formato A4 horizontal.'],
        ['Firebase Emulator Suite, JUnit, Espresso/Compose Test', 'Testes.', 'Testes locais das regras e funções sem afetar dados reais.'],
        ['GitHub', 'Controlo de versões e documentação (incluindo os diagramas PlantUML).', 'Histórico e colaboração.'],
    ], 'Tecnologias propostas.', widths=[2.6, 3.2, 4.4], first_bold=True)

    r.h2('Arquitetura do sistema')
    n = r.next_fig()
    r.para(f'A Figura {n} apresenta a arquitetura lógica em três camadas: clientes, backend Firebase e serviços externos previstos para a evolução futura. Os clientes comunicam com o backend através dos SDK do Firebase, sobre HTTPS.')
    r.figure(f'{D}/arq_componentes.png', 'Arquitetura lógica do sistema.', max_h=10)
    r.para('As leituras são feitas diretamente no Firestore, com subscrições em tempo real filtradas pelas regras de segurança. As escritas que afetam o stock ou que envolvem várias entidades (receção, arrumação, marcação de local cheio, congelação, entrega, saída para a cozinha, desperdício, levantamento de refeições) e a resolução das credenciais QR (`identificarPessoa`) são feitas através de Cloud Functions do tipo *callable*. Os totais derivados, como o número de refeições previstas de um serviço, são mantidos por funções acionadas por eventos do Firestore (*triggers*). Estas validam o perfil do utilizador, aplicam as regras de negócio e executam a operação numa transação. As escritas simples de dados mestre (por exemplo, editar um agregado) podem ser feitas diretamente pelo cliente, protegidas pelas regras de segurança.')
    n = r.next_fig()
    r.para(f'A Figura {n} mostra a implantação física. Inclui o posto biométrico previsto como melhoria futura, num computador fixo.')
    r.figure(f'{D}/arq_implantacao.png', 'Diagrama de implantação.', max_h=8)

    r.h2('Arquitetura da aplicação Android')
    n = r.next_fig()
    r.para(f'As aplicações Android seguem a arquitetura recomendada pela Google (Google, 2026d), com as camadas de apresentação, domínio e dados (Figura {n}). Os ecrãs Compose observam o estado exposto pelos *ViewModels* (StateFlow). Os casos de uso encapsulam as regras de negócio que também correm no cliente, como a conversão de unidades ou a pré-visualização FEFO. Os repositórios abstraem o acesso ao Firebase.')
    r.figure(f'{D}/arq_camadas.png', 'Camadas da aplicação Android.', max_h=9)
    r.para('A organização proposta para os pacotes do projeto é a seguinte:')
    r.code('''
pt.gasc.gestao
 ├─ ui/            rececao, arrumacao, stock, utentes, entregas, refeicoes, relatorios, admin
 ├─ domain/
 │   ├─ model/     Lote, Produto, Local, Agregado, Pessoa, PedidoRefeicao, ...
 │   ├─ usecase/   RegistarRececaoUseCase, SugerirLocalUseCase, SelecionarFefoUseCase, ...
 │   └─ rules/     ConversaoUnidades, Fefo, RegraCongelacao
 ├─ data/
 │   ├─ remote/    FirestoreDataSource, FunctionsDataSource, StorageDataSource
 │   ├─ dto/       documentos Firestore e mapeadores
 │   └─ repository/
 └─ di/            módulos Hilt
''')

    r.h2('Segurança e privacidade')
    r.para('O sistema trata dados pessoais de pessoas em situação de vulnerabilidade, incluindo informação de saúde (alergias e restrições alimentares). Por isso, a segurança e a conformidade com o Regulamento Geral sobre a Proteção de Dados (Regulamento (UE) 2016/679) são requisitos estruturais. As medidas previstas são:')
    r.bullets([
        '**Autorização no servidor:** os perfis são atribuídos como *custom claims* no token do Firebase Authentication e verificados pelas *Security Rules* e pelas Cloud Functions. A interface limita-se a esconder o que o perfil não pode fazer.',
        '**Princípio do menor privilégio:** cada perfil acede apenas às coleções de que necessita (matriz de permissões da secção 3.2); o utente acede apenas aos dados do seu agregado.',
        '**Credenciais QR sem dados pessoais:** o QR contém um *token* aleatório que só é resolvido por uma Cloud Function, que regista o acesso.',
        '**Minimização e finalidade:** só são recolhidos os dados necessários; o consentimento e as finalidades ficam registados por agregado.',
        '**Direitos dos titulares:** funções de exportação (acesso e portabilidade) e de anonimização (apagamento) que preservam as estatísticas agregadas.',
        '**Localização dos dados:** projeto Firebase numa região da União Europeia.',
        '**Auditoria:** registo das operações sensíveis e dos acessos a fichas de utentes.',
        '**Dispositivos próprios:** sem armazenamento de dados sensíveis fora da cache do SDK; fim de sessão remoto ao desativar o utilizador; recomendação de bloqueio de ecrã.',
    ])
    r.para('Extrato ilustrativo das regras de segurança do Firestore:')
    r.code('''
rules_version = '2';
service cloud.firestore {
  match /databases/{db}/documents {
    function perfil(p) { return request.auth != null && request.auth.token[p] == true; }

    match /lotes/{id} {
      allow read: if perfil('OPERADOR') || perfil('RESPONSAVEL') || perfil('COZINHA');
      allow write: if false;            // apenas Cloud Functions (Admin SDK)
    }
    match /agregados/{id} {
      allow read, write: if perfil('TECNICO') || perfil('RESPONSAVEL');
      allow read: if request.auth.token.agregadoId == id;   // utente: só o seu
      match /pessoas/{p} {
        allow read, write: if perfil('TECNICO') || perfil('RESPONSAVEL');
      }
    }
    match /credenciais/{token} { allow read, write: if false; }
  }
}
''')

    r.h2('Interface com o utilizador')
    r.para('A interface segue o Material Design 3 e é adaptada ao perfil do utilizador. O mapa de navegação, os princípios de design e os protótipos de alta fidelidade de todos os ecrãs são apresentados no Capítulo 7.')

    r.h2('Planeamento')
    n = r.next_tab()
    r.para(f'A implementação segue um processo iterativo, com iterações de duas semanas e validação com a instituição no fim de cada uma. A Tabela {n} apresenta a sequência proposta; as durações são estimativas.')
    r.table(['Iteração', 'Âmbito', 'Duração', 'Entregável'], [
        ['0', 'Configuração do projeto Firebase, repositório, CI, autenticação, perfis e estrutura da app.', '2 sem.', 'App com login e perfis.'],
        ['1', 'Catálogo, categorias, tabela de congelação, células e equipamentos de frio, etiquetas QR.', '2 sem.', 'Configuração do armazém.'],
        ['2', 'Receção com controlo RGDHSA049, doadores, conversão de unidades e criação de lotes.', '2 sem.', 'Registo de receções.'],
        ['3', 'Arrumação com sugestão de local, consulta de stock, transferências.', '2 sem.', 'Armazém operacional.'],
        ['4', 'FEFO, congelação, tarefa diária de validades, desperdício e alertas.', '2 sem.', 'Controlo de validades.'],
        ['5', 'Agregados, pessoas, consentimentos, credenciais QR, agendamentos e entregas.', '3 sem.', 'Distribuição de cabazes.'],
        ['6', 'Refeições: serviços, pedidos, saídas para a cozinha, levantamentos.', '2 sem.', 'Gestão de refeições.'],
        ['7', 'RGDHSA049 em PDF, histórico, indicadores, exportações, painel web.', '2 sem.', 'Relatórios.'],
        ['8', 'App Utente; testes de aceitação e de usabilidade; correções; formação.', '3 sem.', 'Versão 1.0 (MVP).'],
    ], 'Plano de iterações.', widths=[1.1, 5.4, 1.2, 2.4])

    r.h2('Riscos')
    n = r.next_tab()
    r.para(f'A Tabela {n} identifica os principais riscos do projeto, avaliados qualitativamente quanto à probabilidade e ao impacto, e as medidas de mitigação previstas.')
    r.table(['ID', 'Risco', 'Prob.', 'Impacto', 'Mitigação'], [
        ['R01', 'Baixa adesão dos colaboradores e voluntários (literacia digital variável).', 'Média', 'Alto', 'Interface simples e orientada à tarefa, validação dos protótipos, formação curta e período em paralelo com o papel.'],
        ['R02', 'Má qualidade dos dados do catálogo (produtos duplicados), que começa vazio.', 'Alta', 'Médio', 'Sugestão de produtos semelhantes na criação (RF-CAT-07), revisão periódica pelo Responsável.'],
        ['R03', 'Incidente de segurança com dados pessoais de utentes.', 'Baixa', 'Alto', 'Autorização no servidor, menor privilégio, auditoria, dados na UE, avaliação de impacto antes da biometria.'],
        ['R04', 'Perda ou roubo de um dispositivo pessoal com sessão ativa.', 'Média', 'Médio', 'Desativação remota do utilizador, ausência de dados sensíveis fora da cache, bloqueio de ecrã recomendado.'],
        ['R05', 'Dependência do Firebase (custos e dependência do fornecedor).', 'Baixa', 'Médio', 'Alertas de orçamento, camada de repositórios que isola o acesso a dados, exportações regulares.'],
        ['R06', 'Alargamento do âmbito durante o desenvolvimento.', 'Alta', 'Médio', 'Priorização MoSCoW, iterações curtas com validação e registo das novas ideias como trabalho futuro.'],
        ['R07', 'Etiquetas QR danificadas ou ilegíveis nas arcas e prateleiras.', 'Média', 'Baixo', 'Etiquetas plastificadas, reimpressão a partir da aplicação e seleção manual do local como alternativa.'],
        ['R08', 'Divergência entre o stock registado e o físico.', 'Média', 'Médio', 'Confirmação por QR, transações atómicas, ajustes de inventário justificados e contagens periódicas.'],
    ], 'Riscos do projeto e medidas de mitigação.', widths=[0.8, 3.4, 1.0, 1.1, 4.0])


def cap7(r, D):
    r.chapter('Plano de Testes e Validação')
    r.para('A validação do sistema combina testes automáticos, executados em cada alteração, com testes de aceitação e de usabilidade realizados com os colaboradores da instituição.')

    r.h2('Estratégia de testes')
    r.table(['Nível', 'Objeto', 'Ferramentas', 'Critério'], [
        ['Unitário', 'Regras de domínio (FEFO, conversão de unidades, sugestão de local, congelação, periodicidade).', 'JUnit, MockK', 'Cobertura ≥ 60% no domínio; todas as regras RN com testes.'],
        ['Integração', 'Cloud Functions e Security Rules.', 'Firebase Emulator Suite, Jest', 'Cada perfil só consegue o que a matriz de permissões define.'],
        ['Interface', 'Fluxos principais em Compose.', 'Compose UI Test', 'UC01, UC02, UC06 e UC09 sem erros.'],
        ['Aceitação', 'Cenários reais com dados de teste.', 'Guião de testes', 'Todos os casos *Must* aprovados pela instituição.'],
        ['Usabilidade', 'Operadores, técnicos e cozinha.', 'Observação e questionário SUS', 'Pontuação SUS ≥ 70 (Brooke, 1996).'],
    ], 'Níveis de teste.', widths=[1.6, 3.6, 2.4, 2.8], first_bold=True)

    r.h2('Casos de teste de aceitação')
    n = r.next_tab()
    r.para(f'A Tabela {n} lista os casos de teste de aceitação, construídos a partir das regras de negócio e dos exemplos fornecidos pela instituição.')
    r.table(['ID', 'Cenário', 'Resultado esperado', 'Req.'], [
        ['TA-01', 'Receção da empresa Pingo Doce sem n.º de guia.', 'O sistema não permite confirmar e pede o n.º da guia.', 'RN-11'],
        ['TA-02', 'Receção de particular anónimo com 2 linhas.', 'Receção gravada sem doador e marcada como anónima.', 'RF-REC-02'],
        ['TA-03', 'Receção de 1 palete de leite 35 cl (30 UN).', 'Lote criado com 30 UN.', 'RN-02'],
        ['TA-04', '10 pacotes de arroz da mesma marca e validade + 5 de outra validade.', 'Dois lotes: 10 UN e 5 UN.', 'RN-01'],
        ['TA-05', 'Saída de 10 kg de um saco de batatas de 50 kg.', 'Stock: 1 UN, 40 kg.', 'RN-02'],
        ['TA-06', 'Arrumação de arroz com uma célula com arroz disponível.', 'É sugerida a célula que já contém arroz.', 'RN-06'],
        ['TA-07', 'Operador assinala a célula 003-02-01 como cheia.', 'É sugerida a célula seguinte mais próxima (ex.: 003-02-02).', 'RF-ARM-05'],
        ['TA-08', 'Arrumação de frango congelado.', 'É sugerida primeiro uma zona da arca de uso preferencial para aves.', 'RN-05'],
        ['TA-09', 'Cabaz com dois lotes de iogurte (validades 24/10 e 30/10).', 'O lote de 24/10 é sugerido primeiro.', 'RN-07'],
        ['TA-10', 'Congelar carne picada (categoria com 90 dias).', 'Nova validade proposta = hoje + 90; validade original preservada.', 'RN-08'],
        ['TA-11', 'Tentar congelar um lote de iogurtes (categoria não congelável).', 'Operação indisponível.', 'RN-08'],
        ['TA-12', 'Tarefa diária com um lote de validade de ontem.', 'Lote EXPIRADO na lista de remoção, sem poder sair para cabaz.', 'RN-09'],
        ['TA-13', 'Filho não autorizado apresenta QR para levantar o cabaz.', 'Levantamento recusado.', 'RN-13'],
        ['TA-14', 'Pedido de 2 refeições de seg. a qui. e 3 à sex. numa semana.', 'Cinco pedidos com as quantidades corretas.', 'RF-REF-03'],
        ['TA-15', 'Pedido de jantar num dia sem serviço de jantar.', 'Pedido recusado.', 'RN-15'],
        ['TA-16', 'Emissão do RGDHSA049 de 1 a 15 de outubro.', 'PDF com todas as receções do intervalo e colunas preenchidas.', 'RF-REL-01'],
        ['TA-17', 'Operador tenta abrir a ficha de um agregado.', 'Acesso negado pelas regras de segurança.', 'RNF-06'],
        ['TA-18', 'Entrega com stock entretanto insuficiente num lote.', 'Transação recusada; stock inalterado; aviso ao operador.', 'RN-18'],
    ], 'Casos de teste de aceitação.', widths=[1.1, 4.0, 4.0, 1.3])

    r.h2('Critérios de aceitação do MVP')
    r.bullets([
        'Todos os requisitos *Must* implementados e com os testes de aceitação aprovados.',
        'Uma semana de utilização em paralelo com o processo em papel, sem divergências de stock superiores a 2%.',
        'Pontuação média SUS igual ou superior a 70.',
        'RGDHSA049 gerado pelo sistema aceite pela equipa HACCP.',
        'Regras de segurança validadas no emulador para todos os perfis.',
    ])


FUTURO = [
    ('F01', 'Reconhecimento de produtos por imagem', 'Fotografar o produto e identificar automaticamente o tipo e o produto do catálogo, para dar entrada e saída.', 'Exige um catálogo estabilizado e testes de fiabilidade; o erro de classificação tem impacto direto no stock.', 'LLM multimodal ou modelo próprio treinado com imagens do catálogo; confirmação sempre pelo operador.'),
    ('F02', 'Leitura da validade por imagem', 'Ler a data de validade impressa na embalagem.', 'Os formatos de data são muito variados; requer validação.', 'ML Kit Text Recognition no dispositivo, com heurísticas de datas e confirmação.'),
    ('F03', 'Extração automática das guias', 'Ler a guia digitalizada e propor as linhas da receção (descrição, quantidade, unidade).', 'As guias são digitalizações de qualidade variável; é necessário associar descrições do fornecedor a produtos.', 'OCR + LLM com saída estruturada; tabela de correspondência código do fornecedor → produto.'),
    ('F04', 'Identificação biométrica facial', 'Identificar o utente pelo rosto num posto fixo.', 'Os dados biométricos são uma categoria especial (art. 9.º do RGPD): exigem consentimento explícito, avaliação de impacto e alternativa não biométrica.', 'Aplicação para PC num local fixo, com modelos de reconhecimento facial locais; o QR mantém-se como alternativa.'),
    ('F05', 'Cabaz automático equilibrado', 'Propor cabazes com proteína, hidratos de carbono, etc., segundo regras do Responsável e a dimensão do agregado.', 'Requer informação nutricional por categoria e a definição das regras pela instituição.', 'Heurística de otimização (*knapsack* multiobjetivo) sobre os lotes FEFO, respeitando alergias.'),
    ('F06', 'Sugestão de pratos', 'Propor pratos a confecionar com base no stock e nas validades.', 'Depende de uma base de receitas e da validação da cozinha.', 'LLM com o stock FEFO como contexto e restrições de quantidade; ou base de receitas própria.'),
    ('F07', 'Mapa do armazém', 'Representar graficamente o armazém e usar distâncias reais nas sugestões.', 'Ainda não existe mapa das prateleiras.', 'Editor de planta e coordenadas por coluna; algoritmo de proximidade por distância.'),
    ('F08', 'Dashboards avançados', 'Indicadores históricos e comparativos na web.', 'O MVP inclui apenas indicadores básicos.', 'Exportação para BigQuery e Looker Studio, ou página web própria.'),
    ('F09', 'Códigos de barras EAN', 'Associar o EAN ao produto e pesquisar por leitura.', 'Ganho elevado, mas não essencial para o MVP.', 'ML Kit Barcode (já usado para o QR).'),
    ('F10', 'Avisos na App Utente', 'Comunicações da instituição aos utentes.', 'Requer definição editorial e de consentimento.', 'FCM por tópico de agregado.'),
    ('F11', 'Valorização em euros', 'Valorizar doações e desperdício em euros (relatórios, mecenato).', 'Para já só se contabilizam quantidades.', 'Preço de referência por produto ou o valor da guia.'),
    ('F12', 'Sensores de temperatura', 'Monitorizar a temperatura das arcas e frigoríficos (HACCP).', 'Exige hardware.', 'Sensores IoT com envio periódico e alertas.'),
    ('F13', 'Integração com outras entidades', 'Exportar dados para programas de apoio alimentar e para a Câmara Municipal.', 'Formatos ainda por definir.', 'Exportações normalizadas (CSV/API) no âmbito do Barcelos Solidário.'),
    ('F14', 'Previsão de refeições', 'Prever a procura diária com base no histórico.', 'Requer histórico de vários meses.', 'Modelos simples de séries temporais.'),
    ('F15', 'Gestão de voluntários', 'Escalas e turnos de voluntários no armazém.', 'Fora do âmbito inicial.', 'Novo módulo sobre os perfis existentes.'),
]


def cap8(r, D):
    r.chapter('Trabalho Futuro')
    r.para('De acordo com a decisão de concentrar a primeira versão no essencial, as funcionalidades seguintes ficam registadas como intenção futura de melhoria. Para cada uma indica-se a razão de não integrar o MVP e a abordagem prevista. O modelo de dados e a arquitetura (camada de serviços externos, campos como `codigo_barras`, `url_guia` ou `tipo_data_validade`) já preparam a sua introdução sem alterações estruturais.')
    n = r.next_tab()
    r.para(f'A Tabela {n} resume as melhorias identificadas.')
    r.table(['ID', 'Melhoria', 'Descrição', 'Razão para adiar', 'Abordagem prevista'],
            [list(x) for x in FUTURO], 'Melhorias futuras.', widths=[0.8, 1.9, 2.6, 2.6, 2.6], size=8)

    r.h2('Inteligência artificial na receção')
    r.para('As melhorias F01 a F03 têm o mesmo objetivo: reduzir o tempo de registo na receção. A abordagem recomendada é incremental. Começa-se pela leitura de códigos de barras (F09), que é determinística. Segue-se a extração das guias (F03), já que as guias das grandes superfícies têm estrutura tabular regular (código, descrição, quantidade, unidade), como mostram os exemplos do Anexo B. Por fim, o reconhecimento por imagem (F01 e F02). Em todos os casos o sistema **propõe** e o operador **confirma**, para que um erro do modelo não chegue ao stock.')

    r.h2('Identificação biométrica')
    r.para('A identificação facial (F04) foi admitida pela instituição apenas se não for muito complexa e preferencialmente como sistema à parte, num PC em local fixo. Para além da complexidade técnica, os dados biométricos para identificação inequívoca são uma categoria especial de dados pessoais (art. 9.º do RGPD). A sua utilização exige consentimento explícito, uma avaliação de impacto sobre a proteção de dados e a garantia de uma alternativa (o QR) para quem não consinta. Recomenda-se que esta funcionalidade seja reavaliada depois de o MVP estar em produção.')

    r.h2('Cabaz automático e sugestão de pratos')
    r.para('O cabaz automático (F05) pode ser formulado como um problema de otimização: escolher lotes que satisfaçam metas por grupo alimentar (proteína, hidratos de carbono, leguminosas, laticínios, fruta e legumes), definidas pelo Responsável em função da dimensão do agregado, minimizando a validade média dos lotes escolhidos e respeitando alergias e restrições. A sugestão de pratos (F06) pode usar um LLM a que se forneça o stock prioritário (FEFO) e o número de refeições, pedindo propostas de pratos com quantidades que a cozinha valida.')


def cap9(r, D):
    from cap3 import RF
    N_RF = sum(len(v) for v in RF.values())
    r.chapter('Conclusão')
    r.paras(
        f'Este documento apresentou a análise e modelação de um sistema de informação para a gestão do Espaço Social do GASC, no âmbito do projeto Barcelos Solidário. Partindo da descrição do problema e de várias rondas de clarificação com a instituição, foram documentados os atores e as permissões, {N_RF} requisitos funcionais organizados por módulo e priorizados, dezassete requisitos não funcionais e dezanove regras de negócio que traduzem com precisão a realidade do armazém: lotes definidos por produto, marca e validade; unidades múltiplas e produtos a granel; codificação de células e zonas de frio; FEFO com preferência por produtos não congelados; e controlo de pessoas autorizadas a levantar.',
        'A modelação UML, dividida por áreas para preservar a legibilidade, cobre os casos de uso, os processos (atividades), a estrutura (classes), o ciclo de vida das entidades principais (estados) e a colaboração entre componentes (sequências). O modelo entidade-relacionamento e o dicionário de dados foram traduzidos para um modelo físico em Cloud Firestore, com critérios explícitos de embebimento, subcoleções e desnormalização. A arquitetura proposta, em Kotlin com Firebase, concentra as operações críticas em Cloud Functions transacionais e aplica a segurança no servidor, o que é especialmente importante quando os colaboradores usam os seus próprios dispositivos e quando estão em causa dados pessoais sensíveis.',
        'A separação entre MVP e trabalho futuro torna o projeto exequível sem perder a visão completa. As funcionalidades de maior complexidade, como o reconhecimento de produtos e validades por imagem, a leitura automática de guias, a biometria, o cabaz automático e a sugestão de pratos, ficaram documentadas com a justificação e a abordagem prevista, e o modelo de dados já as acomoda. Os protótipos de interface completam a especificação, descrevendo ecrã a ecrã o comportamento esperado.',
        'O trabalho tem limitações que importa reconhecer. A análise baseou-se na documentação fornecida e em respostas escritas da instituição, sem observação direta das operações no armazém e na cozinha; os protótipos ainda não foram validados com os utilizadores finais; as durações do plano são estimativas; e a medida de proximidade entre locais é uma aproximação baseada na ordenação dos códigos, enquanto não existir o mapa do armazém. Estas limitações são endereçadas pelos próximos passos propostos.',
        'Como próximos passos, recomenda-se validar com os colaboradores os 42 protótipos de alta fidelidade do Capítulo 7, que servirão de especificação de referência para a implementação; confirmar com a equipa HACCP o tratamento dos tipos de data de validade e o layout do RGDHSA049 gerado, recolher a tabela de congelação por categoria e iniciar a implementação pela iteração 0 do plano proposto.',
    )


BIB = [
    'Brooke, J. (1996). SUS: A "quick and dirty" usability scale. Em P. W. Jordan, B. Thomas, B. A. Weerdmeester & I. L. McClelland (Eds.), *Usability Evaluation in Industry* (pp. 189–194). Taylor & Francis.',
    'Chen, P. P. (1976). The entity-relationship model – toward a unified view of data. *ACM Transactions on Database Systems, 1*(1), 9–36.',
    'Clegg, D., & Barker, R. (1994). *Case Method Fast-Track: A RAD Approach*. Addison-Wesley.',
    'Cockburn, A. (2000). *Writing Effective Use Cases*. Addison-Wesley.',
    'FAO. (2011). *Global food losses and food waste – Extent, causes and prevention*. Food and Agriculture Organization of the United Nations.',
    'GASC. (2026). *Relatório de análise organizacional – GASC, Grupo de Ação Social Cristã, Barcelos* [Documento interno].',
    'GASC, Câmara Municipal de Barcelos, & IPCA. (2026). *Barcelos Solidário – Desenvolvimento de uma plataforma de âmbito social para os cidadãos de Barcelos* [Apresentação].',
    'Google. (2026a). *Firebase documentation*. Obtido de https://firebase.google.com/docs',
    'Google. (2026b). *Cloud Firestore – Data model*. Obtido de https://firebase.google.com/docs/firestore/data-model',
    'Google. (2026c). *ML Kit – Barcode scanning*. Obtido de https://developers.google.com/ml-kit/vision/barcode-scanning',
    'Google. (2026d). *Guide to app architecture*. Android Developers. Obtido de https://developer.android.com/topic/architecture',
    'ISO/IEC. (2011). *ISO/IEC 25010:2011 – Systems and software engineering – Systems and software Quality Requirements and Evaluation (SQuaRE) – System and software quality models*. International Organization for Standardization.',
    'JetBrains. (2026). *Kotlin documentation*. Obtido de https://kotlinlang.org/docs',
    'Larman, C. (2004). *Applying UML and Patterns* (3.ª ed.). Prentice Hall.',
    'Martin, R. C. (2017). *Clean Architecture: A Craftsman\'s Guide to Software Structure and Design*. Prentice Hall.',
    'Object Management Group. (2017). *OMG Unified Modeling Language (OMG UML), Version 2.5.1*. Obtido de https://www.omg.org/spec/UML/2.5.1',
    'Parlamento Europeu e Conselho. (2004). Regulamento (CE) n.º 852/2004, relativo à higiene dos géneros alimentícios. *Jornal Oficial da União Europeia*, L 139.',
    'Parlamento Europeu e Conselho. (2011). Regulamento (UE) n.º 1169/2011, relativo à prestação de informação aos consumidores sobre os géneros alimentícios. *Jornal Oficial da União Europeia*, L 304.',
    'Parlamento Europeu e Conselho. (2016). Regulamento (UE) 2016/679, relativo à proteção das pessoas singulares no que diz respeito ao tratamento de dados pessoais (RGPD). *Jornal Oficial da União Europeia*, L 119.',
    'PlantUML. (2026). *PlantUML language reference guide*. Obtido de https://plantuml.com',
    'Pressman, R. S., & Maxim, B. R. (2020). *Software Engineering: A Practitioner\'s Approach* (9.ª ed.). McGraw-Hill.',
    'Sommerville, I. (2016). *Software Engineering* (10.ª ed.). Pearson.',
    'Wiegers, K., & Beatty, J. (2013). *Software Requirements* (3.ª ed.). Microsoft Press.',
]


def bibliografia(r):
    r.empty(4)
    r.unnumbered_title('Bibliografia')
    for b in BIB:
        p = r.doc.add_paragraph(style='Bibliography')
        from docx.shared import Cm
        p.paragraph_format.first_line_indent = Cm(-0.75)
        p.paragraph_format.left_indent = Cm(0.75)
        r.add_runs(p, b)
        for run in p.runs:
            run.font.name = 'Arial'
            run.font.size = __import__('docx').shared.Pt(11)


def anexos(r, D, UCS, RF):
    r.empty(10)
    r.unnumbered_title('ANEXOS')
    r._section_break(r.sect[11])

    r.empty(1)
    r.unnumbered_title('Anexo A – Mapeamento do registo RGDHSA049')
    r.para('O documento RGDHSA049 – *Monitorização do Controlo da Receção de Matérias-Primas* (Edição 1, Revisão 0, 12/2020) é um registo mensal com uma linha por produto recebido. A tabela seguinte indica a origem de cada coluna nos dados do sistema, o que permite gerá-lo automaticamente para qualquer intervalo de datas.')
    r.table(['Coluna do RGDHSA049', 'Origem no sistema'], [
        ['Mês/Ano', 'Intervalo pedido (cabeçalho; vários meses geram várias folhas).'],
        ['Dia', 'RECECAO.data_hora (dia).'],
        ['Produto / Fornecedor', 'PRODUTO.nome + marca / DOADOR.nome (ou "Particular anónimo").'],
        ['Documento de receção – Lote / N.º guia de remessa', 'LINHA_RECECAO.lote_fornecedor ou RECECAO.n_guia.'],
        ['Quantidade', 'LINHA_RECECAO.quantidade + apresentação (ex.: 1 palete / 30 UN).'],
        ['Condições de higiene (C / NC)', 'LINHA_RECECAO.higiene_c.'],
        ['Rotulagem / Data de validade (C / NC)', 'LINHA_RECECAO.rotulagem_c (e a validade registada).'],
        ['Características organoléticas (C / NC)', 'LINHA_RECECAO.organoleticas_c.'],
        ['Embalagem íntegra (C / NC)', 'LINHA_RECECAO.embalagem_c.'],
        ['Temperatura', 'LINHA_RECECAO.temperatura ou RECECAO.temperatura.'],
        ['Responsável (rubrica)', 'UTILIZADOR.nome de quem registou a receção.'],
        ['Observações', 'LINHA_RECECAO.observacoes (motivos de não conformidade, rejeição).'],
    ], 'Correspondência entre as colunas do RGDHSA049 e os dados do sistema.', widths=[4, 6])

    r.page_break()
    r.unnumbered_title('Anexo B – Exemplos de documentos de entrada')
    r.para('A instituição forneceu exemplos de guias de transporte de cadeias de distribuição (Pingo Doce e Recheio) e de um resumo de doações diárias. São documentos tabulares com, entre outros, o código do artigo do fornecedor, a descrição, a quantidade e a unidade (UN ou KG), e no cabeçalho o número da guia, a data e o NIF do fornecedor. A tabela seguinte mostra a correspondência com os dados do sistema; esta estrutura regular fundamenta a melhoria futura F03.')
    r.table(['Campo da guia', 'Exemplo', 'Campo do sistema'], [
        ['Fornecedor / loja', 'Pingo Doce – Barcelos Alcaides de Faria', 'DOADOR (tipo EMPRESA).'],
        ['N.º da guia / Refª', 'DPM1/4101774379', 'RECECAO.n_guia.'],
        ['Data do documento', '23.03.2026', 'RECECAO.data_hora (referência).'],
        ['Artigo (código)', '0000262753', 'Correspondência futura código → PRODUTO.'],
        ['Descrição', 'ALFACE FRISADA EMB. PD', 'PRODUTO.nome / marca / formato.'],
        ['Quantidade e unidade', '1,324 KG ; 3,000 UN', 'LINHA_RECECAO.quantidade + APRESENTACAO.'],
    ], 'Correspondência entre os campos das guias de transporte e o sistema.', widths=[2.8, 3.6, 3.6])

    r.page_break()
    r.unnumbered_title('Anexo C – Matriz de rastreabilidade')
    r.para('A matriz seguinte relaciona cada requisito funcional com os casos de uso descritos na secção 4.1 e com os mockups do Capítulo 7 que o concretizam, permitindo verificar que todos os requisitos do MVP estão cobertos pela modelação e pela interface.')
    import re
    from cap_mockups import DESC

    def expand(t):
        out = set(re.findall(r'RF-[A-Z]{3}-\d\d', t))
        for a, b in re.findall(r'(RF-[A-Z]{3}-\d\d) a (RF-[A-Z]{3}-\d\d)', t):
            out |= {f'{a[:7]}{i:02d}' for i in range(int(a[-2:]), int(b[-2:]) + 1)}
        return out
    uc, mk = {}, {}
    for uid, _, f in UCS:
        for x in expand(f['Requisitos']):
            uc.setdefault(x, []).append(uid)
    for mid, (_, req, _) in sorted(DESC.items()):
        for x in expand(req):
            mk.setdefault(x, []).append(mid)
    rows = []
    for reqs in RF.values():
        for rid, _, _, fase in reqs:
            rows.append([rid, ', '.join(uc.get(rid, [])) or '–', ', '.join(mk.get(rid, [])) or '–', fase])
    r.table(['Requisito', 'Casos de uso', 'Mockups', 'Fase'], rows,
            'Matriz de rastreabilidade requisitos – casos de uso – mockups.', widths=[1.6, 2.2, 4.8, 1.2], size=8)

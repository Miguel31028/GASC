M, S, C, W = 'Must', 'Should', 'Could', "Won't (agora)"
MVP, FUT = 'MVP', 'Futuro'

RF = {
    'Autenticação e utilizadores (UTZ)': [
        ('RF-UTZ-01', 'Autenticar os colaboradores com email e palavra-passe.', M, MVP),
        ('RF-UTZ-02', 'Permitir ao Administrador criar, editar e desativar utilizadores e atribuir-lhes um ou mais perfis.', M, MVP),
        ('RF-UTZ-03', 'Apresentar menus e ações de acordo com os perfis do utilizador autenticado.', M, MVP),
        ('RF-UTZ-04', 'Permitir a recuperação da palavra-passe por email.', S, MVP),
        ('RF-UTZ-05', 'Registar o autor e a data/hora de todas as operações que alteram dados (auditoria).', M, MVP),
    ],
    'Catálogo e categorias (CAT)': [
        ('RF-CAT-01', 'Gerir categorias de bens (nome, tipo de bem, condição de armazenamento, indicação de congelável, dias de aviso de validade).', M, MVP),
        ('RF-CAT-02', 'Gerir a tabela de congelação por categoria (dias de extensão da validade propostos ao congelar).', M, MVP),
        ('RF-CAT-03', 'Criar produtos no momento da receção ou na gestão do catálogo (nome, marca, formato, categoria, unidade de stock, conteúdo por unidade, indicação de validade). O catálogo começa vazio.', M, MVP),
        ('RF-CAT-04', 'Associar a cada produto várias apresentações com fator de conversão (ex.: caixa de 12 UN, palete de 30 UN, saco de 50 kg).', M, MVP),
        ('RF-CAT-05', 'Definir um stock mínimo por produto.', S, MVP),
        ('RF-CAT-06', 'Registar bens não alimentares (vestuário, higiene, limpeza) com atributos simples: tamanho, género e validade opcional.', M, MVP),
        ('RF-CAT-07', 'Pesquisar produtos por nome, marca ou categoria e sugerir produtos semelhantes para evitar duplicados.', S, MVP),
        ('RF-CAT-08', 'Associar códigos de barras (EAN) aos produtos e pesquisá-los por leitura com a câmara.', C, FUT),
    ],
    'Doadores e receção (REC)': [
        ('RF-REC-01', 'Gerir doadores dos tipos particular, empresa, organização e campanha (nome, NIF, morada, contacto).', M, MVP),
        ('RF-REC-02', 'Registar uma receção indicando a origem; uma doação de particular pode ser registada como anónima.', M, MVP),
        ('RF-REC-03', 'Exigir, numa receção de empresa, o número do documento de transporte e permitir anexar a fotografia ou digitalização da guia.', M, MVP),
        ('RF-REC-04', 'Registar as linhas da receção: produto, apresentação, quantidade, validade e lote do fornecedor.', M, MVP),
        ('RF-REC-05', 'Registar por linha o controlo de receção do RGDHSA049: higiene, rotulagem/validade, características organoléticas e embalagem (C/NC), temperatura e observações.', M, MVP),
        ('RF-REC-06', 'Converter automaticamente as quantidades recebidas para a unidade de stock do produto.', M, MVP),
        ('RF-REC-07', 'Criar lotes distintos quando o produto, a marca ou a validade diferem, e um único lote quando são iguais.', M, MVP),
        ('RF-REC-08', 'Registar as linhas rejeitadas (não conformes e não aproveitáveis) como desperdício de receção.', S, MVP),
        ('RF-REC-09', 'Consultar receções e corrigi-las, com registo de auditoria, enquanto os lotes não tiverem movimentos de saída.', S, MVP),
        ('RF-REC-10', 'Extrair automaticamente os artigos de uma guia digitalizada (OCR/LLM) e propor as linhas da receção.', W, FUT),
        ('RF-REC-11', 'Identificar o produto por imagem para dar entrada e saída do armazém.', W, FUT),
        ('RF-REC-12', 'Ler a data de validade por imagem (OCR).', W, FUT),
    ],
    'Armazém (ARM)': [
        ('RF-ARM-01', 'Gerir as células de prateleira, identificadas pelo código xxx-xx-xx (coluna, linha, andar), em número variável.', M, MVP),
        ('RF-ARM-02', 'Gerir os equipamentos de frio (código, nome, tipo) e as respetivas zonas (lados D, C, E e níveis), bem como as categorias de uso preferencial.', M, MVP),
        ('RF-ARM-03', 'Gerar e imprimir etiquetas com código QR para as células e as zonas de frio.', M, MVP),
        ('RF-ARM-04', 'Sugerir o local de arrumação de cada lote de acordo com as regras de localização.', M, MVP),
        ('RF-ARM-05', 'Permitir ao operador assinalar que o local sugerido está cheio e sugerir o local seguinte mais próximo.', M, MVP),
        ('RF-ARM-06', 'Confirmar a arrumação pela leitura do QR do local ou por seleção manual.', M, MVP),
        ('RF-ARM-07', 'Transferir um lote, total ou parcialmente, entre locais.', S, MVP),
        ('RF-ARM-08', 'Libertar o estado "cheio" de um local manualmente ou quando o seu último lote sai.', S, MVP),
        ('RF-ARM-09', 'Representar o mapa do armazém e calcular a proximidade física real entre locais.', W, FUT),
    ],
    'Stock e validades (STK)': [
        ('RF-STK-01', 'Consultar o stock por produto, categoria e local, na unidade de stock e em volumes (ex.: 1 UN batatas, 40 kg).', M, MVP),
        ('RF-STK-02', 'Ordenar os lotes pela regra FEFO, dando prioridade aos não congelados internamente.', M, MVP),
        ('RF-STK-03', 'Congelar um lote (total ou parcialmente) de uma categoria congelável, propondo a nova validade pela tabela, permitindo alterá-la e guardando a validade original.', M, MVP),
        ('RF-STK-04', 'Apresentar diariamente a lista de lotes expirados a remover do armazém.', M, MVP),
        ('RF-STK-05', 'Registar desperdício (quantidade e motivo: expirado, danificado, não conforme) e contabilizar as quantidades.', M, MVP),
        ('RF-STK-06', 'Registar ajustes de inventário com justificação obrigatória.', S, MVP),
        ('RF-STK-07', 'Permitir saídas parciais em peso de produtos a granel.', M, MVP),
        ('RF-STK-08', 'Consultar o histórico de movimentos de cada lote, desde a receção até à saída.', M, MVP),
    ],
    'Utentes e agregados (UTE)': [
        ('RF-UTE-01', 'Registar agregados familiares: morada, contactos, situação, técnico responsável e estado.', M, MVP),
        ('RF-UTE-02', 'Registar os membros do agregado com dados pessoais (nome, data de nascimento, NIF, NISS, parentesco), restrições alimentares e alergias.', M, MVP),
        ('RF-UTE-03', 'Indicar os membros autorizados a levantar cabazes e refeições em nome do agregado.', M, MVP),
        ('RF-UTE-04', 'Indicar se o agregado beneficia de cabazes, de refeições ou de ambos.', M, MVP),
        ('RF-UTE-05', 'Permitir ao Responsável definir a periodicidade do cabaz de cada agregado.', M, MVP),
        ('RF-UTE-06', 'Emitir uma credencial QR por pessoa autorizada, imprimível em cartão ou apresentada na App Utente, e revogá-la ou reemiti-la.', M, MVP),
        ('RF-UTE-07', 'Registar o consentimento para o tratamento de dados pessoais e as respetivas finalidades.', M, MVP),
        ('RF-UTE-08', 'Pesquisar agregados e pessoas por nome, código ou NIF.', M, MVP),
        ('RF-UTE-09', 'Consultar o histórico de entregas e refeições de um agregado.', S, MVP),
        ('RF-UTE-10', 'Identificar o utente por reconhecimento facial num posto fixo.', W, FUT),
    ],
    'Cabazes e outros bens (ENT)': [
        ('RF-ENT-01', 'Gerar agendamentos de cabaz a partir da periodicidade de cada agregado.', M, MVP),
        ('RF-ENT-02', 'Criar, reagendar e cancelar agendamentos.', M, MVP),
        ('RF-ENT-03', 'Apresentar a lista de entregas do dia.', M, MVP),
        ('RF-ENT-04', 'Identificar quem levanta pela leitura do QR, ou por pesquisa com confirmação manual, e validar se está autorizado.', M, MVP),
        ('RF-ENT-05', 'Apresentar as restrições alimentares e as alergias do agregado durante a preparação do cabaz.', M, MVP),
        ('RF-ENT-06', 'Compor o cabaz manualmente com sugestão de lotes pela regra FEFO.', M, MVP),
        ('RF-ENT-07', 'Registar a entrega, abatendo o stock e registando quem levantou, quem entregou e a data/hora.', M, MVP),
        ('RF-ENT-08', 'Registar entregas de outros bens (roupa, higiene, limpeza) associadas ao utente.', M, MVP),
        ('RF-ENT-09', 'Marcar automaticamente como falta os agendamentos não concretizados no fim do dia.', S, MVP),
        ('RF-ENT-10', 'Disponibilizar um painel web, só de leitura, com a agenda de entregas para ecrãs de parede.', S, MVP),
        ('RF-ENT-11', 'Propor automaticamente cabazes equilibrados (proteína, hidratos de carbono, etc.) de acordo com regras definidas pelo Responsável.', W, FUT),
    ],
    'Refeições (REF)': [
        ('RF-REF-01', 'Gerir serviços de refeição por dia e tipo: almoço por omissão e jantar em dias excecionais.', M, MVP),
        ('RF-REF-02', 'Registar pedidos de refeição por agregado, para uma data e um tipo, com o número de refeições.', M, MVP),
        ('RF-REF-03', 'Registar pedidos recorrentes por dia da semana num intervalo de datas (ex.: 2 refeições de segunda a quinta e 3 à sexta).', S, MVP),
        ('RF-REF-04', 'Alterar ou cancelar pedidos até à hora limite definida.', S, MVP),
        ('RF-REF-05', 'Apresentar o número total de refeições a confecionar por dia e tipo.', M, MVP),
        ('RF-REF-06', 'Registar a saída de produtos para a cozinha com sugestão FEFO.', M, MVP),
        ('RF-REF-07', 'Registar o levantamento de refeições com identificação e validação da pessoa.', M, MVP),
        ('RF-REF-08', 'Registar, no momento do levantamento, o pedido para o dia seguinte.', M, MVP),
        ('RF-REF-09', 'Registar levantamentos excecionais (sem pedido) com justificação.', S, MVP),
        ('RF-REF-10', 'Fechar o serviço, marcando os pedidos não levantados.', S, MVP),
        ('RF-REF-11', 'Sugerir pratos a confecionar com base no stock e nas validades.', W, FUT),
    ],
    'Relatórios, alertas e indicadores (REL)': [
        ('RF-REL-01', 'Emitir o registo RGDHSA049 em PDF para qualquer intervalo de datas, sempre que solicitado.', M, MVP),
        ('RF-REL-02', 'Gerar alertas de validade próxima (antecedência configurável por categoria).', M, MVP),
        ('RF-REL-03', 'Gerar alertas de stock abaixo do mínimo.', M, MVP),
        ('RF-REL-04', 'Enviar notificações push aos perfis responsáveis.', S, MVP),
        ('RF-REL-05', 'Consultar o histórico de receções e entregas com filtros (período, doador, agregado, produto).', M, MVP),
        ('RF-REL-06', 'Consultar o desperdício por período, produto, categoria e motivo (quantidades).', M, MVP),
        ('RF-REL-07', 'Apresentar um painel de indicadores básico (stock, entradas, saídas, desperdício, refeições).', S, MVP),
        ('RF-REL-08', 'Exportar listagens em CSV e PDF.', S, MVP),
        ('RF-REL-09', 'Disponibilizar dashboards avançados na web, com análise temporal e comparativa.', C, FUT),
    ],
    'App Utente (APU)': [
        ('RF-APU-01', 'Autenticar o utente pelo número de telemóvel (código por SMS) após ativação da conta pelo técnico.', S, MVP),
        ('RF-APU-02', 'Apresentar a credencial QR do utente.', S, MVP),
        ('RF-APU-03', 'Consultar as próximas entregas agendadas do agregado.', S, MVP),
        ('RF-APU-04', 'Registar e cancelar pedidos de refeição do agregado, dentro das regras definidas.', S, MVP),
        ('RF-APU-05', 'Receber avisos e comunicações da instituição.', C, FUT),
    ],
}

RNF = [
    ('RNF-01', 'Usabilidade', 'Interface em português europeu, com elementos de toque de pelo menos 48 dp e as operações mais frequentes (registar linha de receção, entregar cabaz, registar levantamento) acessíveis em três toques ou menos a partir do ecrã inicial.'),
    ('RNF-02', 'Facilidade de aprendizagem', 'Um colaborador sem formação técnica deve conseguir registar uma receção completa após uma sessão de formação de 30 minutos.'),
    ('RNF-03', 'Desempenho', 'As consultas de stock e a sugestão de local devem responder em menos de 2 segundos (percentil 90) numa ligação Wi-Fi ou 4G.'),
    ('RNF-04', 'Disponibilidade', 'O sistema deve estar disponível 24×7, beneficiando da disponibilidade dos serviços Firebase; as tarefas agendadas devem ser reexecutáveis sem efeitos duplicados (idempotência).'),
    ('RNF-05', 'Conectividade', 'Assume-se Internet disponível em todos os locais. A aplicação deve tolerar falhas curtas, mantendo em cache os dados consultados, mas as operações que alteram stock exigem ligação, para garantir transações atómicas.'),
    ('RNF-06', 'Segurança', 'Autenticação obrigatória; autorização por perfil, verificada no servidor (*custom claims* e *Security Rules*); comunicação cifrada (TLS); sessões terminadas após inatividade prolongada.'),
    ('RNF-07', 'Privacidade (RGPD)', 'Minimização dos dados pessoais, consentimento registado, direitos de acesso, retificação e apagamento (com anonimização que preserve as estatísticas), dados alojados numa região da União Europeia e registo dos acessos a dados de utentes.'),
    ('RNF-08', 'Integridade', 'Todos os movimentos de stock são executados em transações atómicas; o stock de um lote nunca pode ficar negativo.'),
    ('RNF-09', 'Rastreabilidade', 'Cada lote é rastreável desde a receção (doador, guia, controlo) até à saída (agregado, pessoa, cozinha ou desperdício).'),
    ('RNF-10', 'Compatibilidade', 'Android 8.0 (API 26) ou superior, em smartphones com ecrã de 5" ou mais; painel web compatível com as versões atuais do Chrome, Edge e Firefox.'),
    ('RNF-11', 'Manutenibilidade', 'Código em Kotlin numa arquitetura em camadas (MVVM), com testes unitários na camada de domínio (cobertura mínima de 60%) e versionado em Git.'),
    ('RNF-12', 'Escalabilidade', 'Suportar pelo menos 50 utilizadores, 5 000 lotes ativos e 2 000 agregados sem degradação perceptível.'),
    ('RNF-13', 'Custo', 'Operar dentro dos limites gratuitos ou de baixo custo do Firebase, com alertas de orçamento configurados.'),
    ('RNF-14', 'Cópias de segurança', 'Exportação diária automática da base de dados para armazenamento na nuvem, com retenção mínima de 30 dias.'),
    ('RNF-15', 'Extensibilidade', 'Novos tipos de bens, categorias, equipamentos e células devem ser configuráveis sem alteração de código.'),
    ('RNF-16', 'Acessibilidade', 'Respeito pelo tamanho de letra do sistema, contraste adequado e textos alternativos nos ícones.'),
    ('RNF-17', 'Localização', 'Datas no formato dd/mm/aaaa, fuso horário Europe/Lisbon e unidades do Sistema Internacional.'),
]

RN = [
    ('RN-01', 'Lote', 'Um lote agrupa unidades do mesmo produto (nome, marca e formato) com a mesma validade e o mesmo estado de congelação. Linhas iguais da mesma receção fundem-se num lote; qualquer diferença origina um lote distinto.'),
    ('RN-02', 'Unidades', 'Cada produto tem uma unidade de stock (UN, KG ou L). As apresentações têm um fator de conversão (ex.: palete = 30 UN). Nos produtos a granel o stock é contado em peso e em volumes: a saída em kg reduz o peso e o volume mantém-se até o peso chegar a zero (ex.: entra 1 UN de batatas com 50 kg, saem 10 kg, ficam 1 UN com 40 kg).'),
    ('RN-03', 'Células', 'O código de uma célula tem o formato xxx-xx-xx: três dígitos para a coluna, dois para a linha e dois para o andar. A ordenação é feita por coluna, depois linha e depois andar.'),
    ('RN-04', 'Zonas de frio', 'Uma zona é identificada pelo código do equipamento, pelo lado (D – direita, C – centro, E – esquerda) e pelo nível (ex.: ARCA1-D2). O número de zonas varia por equipamento, mas não existem lados para além de D, C e E.'),
    ('RN-05', 'Uso preferencial', 'O uso preferencial de um equipamento de frio por categoria (ex.: arca 1 para aves) é uma sugestão, nunca uma restrição.'),
    ('RN-06', 'Sugestão de local', 'O sistema sugere primeiro um local não cheio que já contenha o mesmo produto; na falta deste, o local não cheio mais próximo, na ordenação, do último local usado pelo produto ou pela categoria (algoritmo na secção 4.6).'),
    ('RN-07', 'FEFO', 'As saídas sugerem os lotes por ordem crescente de validade, colocando no fim os lotes congelados internamente. Os produtos já congelados na origem são tratados como não congelados.'),
    ('RN-08', 'Congelação', 'Só podem ser congelados lotes de categorias congeláveis. A nova validade proposta é a data de congelação somada dos dias da tabela da categoria e pode ser alterada pelo operador. A validade original é preservada. Congelar parte de um lote divide-o em dois.'),
    ('RN-09', 'Expiração', 'Um lote com validade anterior à data atual passa a EXPIRADO, aparece na lista de remoção e não pode ser usado em cabazes ou na cozinha.'),
    ('RN-10', 'Desperdício', 'O desperdício é contabilizado apenas em quantidades (na unidade de stock), por produto, categoria e motivo.'),
    ('RN-11', 'Origem', 'Uma receção de empresa exige o número da guia de transporte. Uma receção de particular pode ser anónima ou identificar totalmente o doador.'),
    ('RN-12', 'RGDHSA049', 'O controlo de receção é obrigatório em todas as receções, independentemente da origem. O responsável indicado no documento é o utilizador que registou a receção.'),
    ('RN-13', 'Autorização de levantamento', 'Só as pessoas marcadas como autorizadas no agregado podem levantar cabazes e refeições.'),
    ('RN-14', 'Pedidos de refeição', 'Os pedidos são feitos por agregado, para um dia e um tipo de refeição, com o número de refeições pretendido. O sistema avisa quando esse número excede o número de membros do agregado.'),
    ('RN-15', 'Jantar', 'Só é possível pedir jantar para os dias em que o Responsável abriu o serviço de jantar.'),
    ('RN-16', 'Periodicidade', 'A periodicidade do cabaz é definida pelo Responsável. O próximo agendamento é calculado a partir da data da última entrega.'),
    ('RN-17', 'Credencial QR', 'Cada pessoa tem no máximo uma credencial ativa. O QR contém apenas um *token* aleatório, sem dados pessoais, e uma reemissão invalida a credencial anterior.'),
    ('RN-18', 'Stock não negativo', 'Nenhuma operação pode deixar a quantidade de um lote abaixo de zero.'),
    ('RN-19', 'Aviso de validade', 'A antecedência do alerta de validade é definida por categoria (valor por omissão: 7 dias).'),
]

PERM = [
    ('Utilizadores e parâmetros', 'G', 'C', '–', '–', '–', '–'),
    ('Catálogo e tabela de congelação', 'G', 'G', 'C', 'G', 'C', '–'),
    ('Células e equipamentos de frio', 'G', 'G', '–', 'C', 'C', '–'),
    ('Receção e arrumação', 'C', 'G', '–', 'G', '–', '–'),
    ('Stock, congelação e desperdício', 'C', 'G', 'C', 'G', 'C', '–'),
    ('Agregados e pessoas', 'C', 'G', 'G', 'C', 'C', 'P'),
    ('Periodicidade dos cabazes', '–', 'G', 'C', 'C', '–', '–'),
    ('Agendamentos', '–', 'G', 'G', 'C', '–', 'P'),
    ('Entregas de cabazes e outros bens', '–', 'G', 'C', 'G', '–', 'P'),
    ('Serviços de refeição', '–', 'G', 'C', '–', 'G', '–'),
    ('Pedidos de refeição', '–', 'G', 'G', '–', 'G', 'P'),
    ('Saídas para a cozinha e levantamentos', '–', 'G', '–', 'C', 'G', '–'),
    ('Relatórios, RGDHSA049 e indicadores', 'C', 'G', 'C', 'C', 'C', '–'),
]


def cap3(r, D):
    r.chapter('Análise de Requisitos')
    r.para('Este capítulo identifica os intervenientes no sistema e documenta os requisitos funcionais e não funcionais, as regras de negócio e os pressupostos que condicionam a solução.')

    r.h2('Atores e perfis de utilizador')
    n = r.next_tab()
    r.para(f'Foram identificados seis perfis de utilizador humano e um ator temporal, descritos na Tabela {n}. Um colaborador pode acumular vários perfis; por exemplo, o Responsável da instituição pode também operar o armazém.')
    r.table(['Ator', 'Descrição', 'Principais responsabilidades'], [
        ['Administrador', 'Colaborador com conhecimentos informáticos que configura o sistema.', 'Gerir utilizadores e perfis, células, equipamentos de frio e parâmetros.'],
        ['Responsável da instituição', 'Coordenador do Espaço Social.', 'Definir regras (tabela de congelação, periodicidade dos cabazes, serviço de jantar), supervisionar o stock e emitir relatórios.'],
        ['Técnico de ação social', 'Técnico que acompanha os agregados.', 'Registar agregados e pessoas, consentimentos e credenciais; agendar entregas; registar pedidos de refeição.'],
        ['Operador de armazém', 'Colaborador ou voluntário do armazém.', 'Receber, arrumar, congelar, transferir, registar desperdício e entregar cabazes e outros bens.'],
        ['Cozinha', 'Colaborador da cozinha ou da cantina.', 'Consultar refeições a confecionar, registar saídas para a cozinha, levantamentos e pedidos do dia seguinte.'],
        ['Utente', 'Membro de um agregado apoiado com acesso à App Utente.', 'Apresentar a credencial QR, consultar entregas e registar pedidos de refeição.'],
        ['Tempo', 'Ator não humano (tarefas agendadas).', 'Verificar validades e stock mínimo, gerar alertas, marcar faltas e fechar serviços.'],
    ], 'Atores do sistema.', widths=[2.2, 3.4, 4.6], first_bold=True)

    r.h2('Matriz de permissões')
    n = r.next_tab()
    r.para(f'A Tabela {n} define as permissões de cada perfil por área funcional. As permissões são verificadas no servidor, pelas regras de segurança do Firestore e pelas Cloud Functions, e não apenas na interface (ver secção 6.4).')
    r.table(['Área funcional', 'ADM', 'RESP', 'TEC', 'OP', 'COZ', 'UT'],
            [list(p) for p in PERM],
            'Matriz de permissões por perfil (G – gerir; C – consultar; P – apenas dados do próprio agregado; – sem acesso).',
            widths=[4.2, 1, 1, 1, 1, 1, 1], first_bold=True)

    r.h2('Requisitos funcionais')
    r.para('Os requisitos funcionais estão organizados por módulo. Cada requisito tem um identificador único, uma prioridade MoSCoW e a fase em que será implementado. Os requisitos *Must* e *Should* constituem o MVP. Os requisitos *Could* e *Won\'t (agora)* são melhorias futuras, desenvolvidas no Capítulo 9.')
    for mod, reqs in RF.items():
        r.h3(mod)
        r.table(['ID', 'Descrição', 'Prioridade', 'Fase'],
                [[a, b, c, d] for a, b, c, d in reqs],
                f'Requisitos funcionais – {mod.split(" (")[0]}.',
                widths=[1.5, 6.2, 1.4, 1.0])
    total = sum(len(v) for v in RF.values())
    mvp = sum(1 for v in RF.values() for x in v if x[3] == MVP)
    r.para(f'No total foram identificados {total} requisitos funcionais, dos quais {mvp} integram o MVP e {total - mvp} são melhorias futuras.')

    r.h2('Requisitos não funcionais')
    n = r.next_tab()
    r.para(f'Os requisitos não funcionais (Tabela {n}) seguem as características de qualidade do modelo ISO/IEC 25010 (ISO/IEC, 2011) e refletem o contexto de utilização: colaboradores com perfis técnicos diversos, que usam o seu próprio smartphone, e o tratamento de dados pessoais de pessoas em situação de vulnerabilidade.')
    r.table(['ID', 'Característica', 'Descrição'], [list(x) for x in RNF],
            'Requisitos não funcionais.', widths=[1.3, 2.2, 6.6])

    r.h2('Regras de negócio')
    n = r.next_tab()
    r.para(f'As regras de negócio da Tabela {n} resultam das respostas da instituição e devem ser aplicadas de forma consistente em todos os pontos do sistema, preferencialmente na camada de domínio e nas Cloud Functions.')
    r.table(['ID', 'Regra', 'Descrição'], [list(x) for x in RN],
            'Regras de negócio.', widths=[1.2, 2.2, 6.7])

    r.h2('Pressupostos e restrições')
    r.bullets([
        '**Tecnologia imposta:** a aplicação móvel é desenvolvida em Kotlin com Firebase. Podem usar-se serviços de apoio (modelos de IA, tecnologias web básicas).',
        '**Plataforma:** todos os colaboradores usam smartphones Android próprios. Por isso, a aplicação não deve guardar dados sensíveis fora da cache gerida pelo SDK e deve terminar a sessão quando o utilizador é desativado.',
        '**Conectividade:** existe Internet com qualidade em todos os locais do armazém e da cozinha.',
        '**Dados iniciais:** o catálogo de produtos começa vazio e cresce com as receções. Os utentes e os agregados têm de ser todos registados, uma vez que não existe sistema anterior de onde importar.',
        '**Etiquetagem:** a instituição aceita colar etiquetas QR nas células das prateleiras e nas zonas dos equipamentos de frio.',
        '**Validação pendente:** convém confirmar com a equipa HACCP se o sistema deve distinguir a *data limite de consumo* ("consumir até") da *data de durabilidade mínima* ("consumir de preferência antes de"), prevista no Regulamento (UE) n.º 1169/2011, pois a regra de expiração pode diferir. O modelo de dados prevê um campo para este efeito (ver secção 5.2).',
    ])

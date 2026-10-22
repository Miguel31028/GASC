UCS = [
    ('UC01', 'Registar receção', {
        'Atores': 'Operador de armazém (principal).',
        'Descrição': 'Regista a entrada de bens doados, com a origem, as linhas de produto e o controlo de receção exigido pelo RGDHSA049.',
        'Pré-condições': 'Utilizador autenticado com o perfil Operador ou Responsável.',
        'Pós-condições': 'Receção e linhas gravadas; linhas aceites agrupadas em lotes no estado PENDENTE_ARRUMACAO; movimentos de ENTRADA registados; linhas rejeitadas registadas como desperdício na receção, sem lote.',
        'Fluxo principal': '1. O operador inicia uma nova receção.\n2. Indica a origem (empresa, particular, organização ou campanha) e o doador.\n3. Se a origem for empresa, indica o n.º da guia e fotografa-a ou anexa o ficheiro digitalizado.\n4. Para cada produto: pesquisa-o, escolhe a apresentação, indica a quantidade e a validade e avalia os critérios C/NC e a temperatura.\n5. O operador confirma a receção.\n6. O sistema grava tudo numa transação, cria os lotes e apresenta a lista de lotes a arrumar.',
        'Fluxos alternativos': '2a. Particular que não se quer identificar: a receção é marcada como anónima.\n4a. O produto não existe: o operador cria-o (nome, marca, formato, categoria, unidade).\n4b. A linha é não conforme: o operador regista o motivo e decide se o produto é aproveitável; se não for, a linha é rejeitada.\n6a. Falha de ligação: nada é gravado e o operador pode repetir a confirmação.',
        'Requisitos': 'RF-REC-01 a RF-REC-09, RF-CAT-03, RF-CAT-04; RN-01, RN-02, RN-11, RN-12.',
    }),
    ('UC02', 'Arrumar lote', {
        'Atores': 'Operador de armazém.',
        'Descrição': 'Guarda um lote num local físico seguindo a sugestão do sistema.',
        'Pré-condições': 'Existe pelo menos um lote no estado PENDENTE_ARRUMACAO.',
        'Pós-condições': 'Lote associado a um local e no estado DISPONIVEL (os produtos congelados na origem mantêm o indicador `congeladoOrigem`); movimento de ARRUMACAO registado.',
        'Fluxo principal': '1. O operador seleciona o lote.\n2. O sistema sugere um local (RN-06).\n3. O operador desloca-se ao local e lê o QR.\n4. O sistema valida o código e associa o lote ao local.',
        'Fluxos alternativos': '3a. O local está cheio: o operador assinala-o e o sistema marca o local como cheio e sugere o seguinte mais próximo.\n3b. O operador prefere outro local: lê o QR desse local ou escolhe-o numa lista.\n4a. O código lido não corresponde a um local ativo: é apresentado um erro.',
        'Requisitos': 'RF-ARM-04 a RF-ARM-06; RN-03 a RN-06.',
    }),
    ('UC03', 'Congelar lote', {
        'Atores': 'Operador de armazém.',
        'Descrição': 'Congela total ou parcialmente um lote perto do fim da validade, prolongando-a de acordo com a tabela da categoria.',
        'Pré-condições': 'Lote DISPONIVEL de uma categoria congelável.',
        'Pós-condições': 'Lote (ou o novo lote resultante da divisão, ligado ao de origem) no estado CONGELADO, com a nova validade, a validade original preservada e uma nova localização numa zona de frio de um congelador.',
        'Fluxo principal': '1. O operador seleciona o lote (por exemplo, a partir de um alerta).\n2. Indica a quantidade a congelar.\n3. O sistema propõe a nova validade (data atual + dias da tabela).\n4. O operador confirma ou corrige a validade.\n5. O sistema sugere uma zona de frio num congelador e o operador confirma-a pelo QR.',
        'Fluxos alternativos': '2a. A quantidade é inferior ao total: o lote é dividido e só o novo lote fica congelado.\n3a. A categoria não tem regra definida: o operador indica a validade manualmente.',
        'Requisitos': 'RF-STK-03, RF-CAT-02; RN-07, RN-08.',
    }),
    ('UC04', 'Registar desperdício', {
        'Atores': 'Operador de armazém, Responsável.',
        'Descrição': 'Retira do stock produtos expirados ou danificados e contabiliza a quantidade desperdiçada.',
        'Pré-condições': 'Lote com quantidade superior a zero.',
        'Pós-condições': 'Registo de desperdício criado; quantidade do lote reduzida; lote DESCARTADO quando a quantidade restante chega a zero.',
        'Fluxo principal': '1. O operador abre a lista de lotes expirados.\n2. Seleciona o lote e confirma a quantidade retirada.\n3. Indica o motivo (expirado, danificado, não conforme).\n4. O sistema regista o desperdício e o movimento correspondente.',
        'Fluxos alternativos': '1a. Produto danificado não expirado: o operador seleciona o lote a partir da pesquisa de stock.',
        'Requisitos': 'RF-STK-04, RF-STK-05; RN-09, RN-10.',
    }),
    ('UC05', 'Registar / editar agregado', {
        'Atores': 'Técnico de ação social, Responsável.',
        'Descrição': 'Cria ou atualiza a ficha de um agregado familiar e dos seus membros.',
        'Pré-condições': 'Utilizador com o perfil Técnico ou Responsável.',
        'Pós-condições': 'Agregado e pessoas gravados; consentimento registado; credenciais QR emitidas para as pessoas autorizadas.',
        'Fluxo principal': '1. O técnico cria o agregado (morada, contactos, situação).\n2. Adiciona os membros com os dados pessoais, as restrições alimentares e as alergias.\n3. Marca as pessoas autorizadas a levantar.\n4. Indica se o agregado beneficia de cabaz e/ou de refeições.\n5. Regista o consentimento (finalidades e documento assinado).\n6. O sistema emite as credenciais QR das pessoas autorizadas.',
        'Fluxos alternativos': '3a. Uma pessoa deixa de estar autorizada: a sua credencial é revogada.\n6a. O utente usa a App Utente: o técnico ativa a conta pelo número de telemóvel.',
        'Requisitos': 'RF-UTE-01 a RF-UTE-08, RF-APU-01; RN-13, RN-17; RNF-07.',
    }),
    ('UC06', 'Entregar cabaz', {
        'Atores': 'Operador de armazém.',
        'Descrição': 'Entrega um cabaz a uma pessoa autorizada do agregado, abatendo os produtos ao stock.',
        'Pré-condições': 'Agendamento AGENDADO para o dia; agregado ativo.',
        'Pós-condições': 'Entrega registada; stock abatido; agendamento ENTREGUE; próximo agendamento criado.',
        'Fluxo principal': '1. O operador abre as entregas do dia.\n2. Lê o QR da pessoa.\n3. O sistema (Cloud Function `identificarPessoa`) valida a autorização e devolve as restrições, as alergias e o agendamento do dia.\n4. O sistema sugere lotes não expirados por ordem FEFO.\n5. O operador adiciona os produtos e as quantidades.\n6. O operador confirma e o sistema regista a entrega numa transação.',
        'Fluxos alternativos': '2a. A pessoa não tem o QR: o operador pesquisa-a pelo nome e confirma a identidade manualmente (fica registado).\n3a. A pessoa não está autorizada: a entrega é recusada.\n6a. O stock de um lote ficou insuficiente entretanto: o sistema avisa e propõe outro lote.',
        'Requisitos': 'RF-ENT-03 a RF-ENT-07, RF-ENT-01 (pós-condição); RN-07, RN-09, RN-13, RN-16, RN-18.',
    }),
    ('UC07', 'Registar pedido de refeição', {
        'Atores': 'Técnico, Cozinha, Utente.',
        'Descrição': 'Regista a intenção de um agregado receber um número de refeições num dia e tipo.',
        'Pré-condições': 'Agregado ativo que beneficia de refeições; serviço aberto nessa data; hora limite do dia anterior não ultrapassada.',
        'Pós-condições': 'Pedido no estado PEDIDO; total previsto do serviço atualizado.',
        'Fluxo principal': '1. O ator identifica o agregado (ou o utente usa a app).\n2. Escolhe a data, o tipo (almoço/jantar) e o número de refeições.\n3. O servidor (Cloud Function `registarPedido`) valida as regras e grava o pedido.',
        'Fluxos alternativos': '2a. Pedido recorrente: o ator indica o intervalo e o número por dia da semana, e o sistema cria um pedido por dia.\n3a. O número excede o de membros: o sistema avisa e pede confirmação.\n3b. O jantar não está aberto nesse dia: o pedido é recusado.',
        'Requisitos': 'RF-REF-02 a RF-REF-04, RF-APU-04; RN-14, RN-15.',
    }),
    ('UC08', 'Registar saída para a cozinha', {
        'Atores': 'Cozinha.',
        'Descrição': 'Regista os produtos retirados do armazém para confecionar as refeições do dia.',
        'Pré-condições': 'Serviço de refeição do dia existente.',
        'Pós-condições': 'Saída para a cozinha registada; stock abatido (movimentos SAIDA_COZINHA).',
        'Fluxo principal': '1. A cozinha consulta o número de refeições a confecionar.\n2. Seleciona os produtos; o sistema sugere os lotes FEFO.\n3. Indica as quantidades (UN ou kg).\n4. Confirma e o sistema abate o stock.',
        'Fluxos alternativos': '2a. O produto pretendido não tem stock: o sistema informa e sugere produtos da mesma categoria.',
        'Requisitos': 'RF-REF-05, RF-REF-06, RF-STK-07; RN-02, RN-07.',
    }),
    ('UC09', 'Registar levantamento de refeição', {
        'Atores': 'Cozinha.',
        'Descrição': 'Regista a entrega das refeições a uma pessoa autorizada e o pedido para o dia seguinte.',
        'Pré-condições': 'Serviço aberto; distribuição iniciada.',
        'Pós-condições': 'Levantamento registado; pedido no estado LEVANTADO; eventual pedido para o dia seguinte criado.',
        'Fluxo principal': '1. A cozinha lê o QR da pessoa.\n2. O sistema mostra o pedido do agregado para hoje.\n3. A cozinha confirma o número de refeições entregues.\n4. O sistema pergunta pelo pedido do dia seguinte e regista-o.',
        'Fluxos alternativos': '2a. A pessoa não está autorizada: o levantamento é recusado, sem possibilidade de exceção (RN-13).\n2b. A pessoa está autorizada mas o agregado não tem pedido: a cozinha pode registar uma exceção com justificação obrigatória.',
        'Requisitos': 'RF-REF-07 a RF-REF-10; RN-13.',
    }),
    ('UC10', 'Emitir RGDHSA049', {
        'Atores': 'Responsável.',
        'Descrição': 'Gera o documento de monitorização do controlo da receção de matérias-primas para um intervalo de datas.',
        'Pré-condições': 'Existem receções no intervalo.',
        'Pós-condições': 'PDF gerado e guardado, disponível para abrir e partilhar.',
        'Fluxo principal': '1. O Responsável indica a data de início e de fim.\n2. O sistema recolhe as receções e linhas do intervalo.\n3. O sistema preenche as colunas do modelo e gera o PDF.\n4. O Responsável abre ou partilha o documento.',
        'Fluxos alternativos': '2a. Não há receções no intervalo: o sistema informa e não gera documento.',
        'Requisitos': 'RF-REL-01; RN-12; Anexo A.',
    }),
    ('UC11', 'Verificar validades, stock mínimo e fecho do dia', {
        'Atores': 'Tempo (tarefa diária).',
        'Descrição': 'Analisa diariamente os lotes e o stock, gerando alertas e atualizando estados, e fecha o dia de entregas e refeições.',
        'Pré-condições': 'Tarefa agendada configurada.',
        'Pós-condições': 'Lotes expirados marcados; alertas de validade e de stock mínimo criados; notificações enviadas; à hora de fecho, agendamentos não concretizados marcados como FALTOU e serviços do dia fechados.',
        'Fluxo principal': '1. Às 07:00 o agendador dispara a função.\n2. A função marca como EXPIRADO os lotes com validade ultrapassada.\n3. Cria alertas para os lotes que expiram dentro da antecedência da categoria.\n4. Calcula o stock por produto e cria alertas de stock mínimo.\n5. Envia notificações aos perfis responsáveis.',
        'Fluxos alternativos': '1a. Execução repetida no mesmo dia: os alertas já existentes não são duplicados (identificadores determinísticos).\n5a. À hora de fecho definida nos parâmetros, uma segunda tarefa marca as faltas e fecha os serviços ainda abertos (secção 4.5).',
        'Requisitos': 'RF-REL-02 a RF-REL-04, RF-STK-04, RF-ENT-09, RF-REF-10; RN-09, RN-19.',
    }),
]


def cap4(r, D):
    r.chapter('Modelação do Sistema')
    r.para('Este capítulo formaliza o comportamento e a estrutura do sistema através de diagramas UML (Object Management Group, 2017). Por legibilidade, cada diagrama foca uma área do sistema; os elementos de outras áreas aparecem apenas como referência.')

    # 4.1 Casos de uso
    r.h2('Casos de uso')
    r.h3('Visão geral')
    n = r.next_fig()
    r.para(f'O sistema foi decomposto em seis subsistemas. A Figura {n} relaciona os atores com os subsistemas que utilizam. Cada subsistema é detalhado nas figuras seguintes; o subsistema P3 foi dividido em dois diagramas por legibilidade.')
    r.figure(f'{D}/uc_geral.png', 'Diagrama de casos de uso – visão geral por subsistema.', max_h=14)
    r.h3('Casos de uso por subsistema')
    for img, cap, txt in [
        ('uc_rececao', 'Receção (P1)', 'A receção inclui obrigatoriamente a identificação do doador, o registo das linhas e o controlo de receção de cada linha. A anexação da guia só ocorre nas receções de empresas e a criação de produto só quando este ainda não existe no catálogo.'),
        ('uc_armazem', 'Armazém e Stock (P2)', 'A arrumação inclui sempre a sugestão de localização. Assinalar um local cheio é uma extensão que ocorre apenas quando o local sugerido não tem espaço. A congelação inclui a proposta de nova validade pela tabela da categoria.'),
        ('uc_utentes', 'Utentes e Entregas – gestão de utentes (P3)', 'O registo do agregado inclui a gestão dos membros e o consentimento. A definição de pessoas autorizadas, a emissão de credenciais e a ativação da conta na App Utente são extensões.'),
        ('uc_entregas', 'Utentes e Entregas – cabazes e outros bens (P3)', 'A entrega de cabaz e a de outros bens incluem a identificação de quem levanta. O cabaz inclui também a seleção de produtos com sugestão FEFO.'),
        ('uc_refeicoes', 'Refeições (P4)', 'Os pedidos de refeição podem ser registados pelo técnico, pela cozinha ou pelo próprio utente. O pedido recorrente estende o pedido simples.'),
        ('uc_administracao', 'Administração (P5)', 'A administração cobre a configuração do sistema: utilizadores, categorias e tabela de congelação, catálogo, células, equipamentos de frio e parâmetros.'),
        ('uc_relatorios', 'Relatórios e Alertas (P6)', 'Os relatórios são consultados sobretudo pelo Responsável. A verificação de validades e stock mínimo é desencadeada pelo ator Tempo.'),
    ]:
        n = r.next_fig()
        r.para(f'A Figura {n} apresenta o subsistema {cap}. {txt}')
        r.figure(f'{D}/{img}.png', f'Diagrama de casos de uso – {cap}.', max_h=12)

    r.h3('Descrição dos casos de uso principais')
    first = r.next_tab()
    r.para(f'Os onze casos de uso mais relevantes para o funcionamento do sistema estão descritos da Tabela {first} à Tabela {first + len(UCS) - 1}, segundo o formato proposto por Cockburn (2000). Os restantes casos de uso dos diagramas correspondem a operações de consulta ou de gestão de dados mestre, cujo comportamento é especificado pelos requisitos e pelos *mockups* do Capítulo 6.')
    for uid, name, f in UCS:
        rows = [[k, v] for k, v in f.items()]
        r.table(['Campo', f'{uid} – {name}'], rows, f'Descrição do caso de uso {uid} – {name}.', widths=[2.2, 7.8], first_bold=True)

    # 4.2 Atividades
    r.h2('Diagramas de atividade')
    r.para('Os diagramas de atividade descrevem os processos de negócio mais relevantes, com as responsabilidades repartidas por raias (*swimlanes*) entre os atores e o sistema.')
    for img, cap, txt in [
        ('act_rececao', 'Processo de receção de bens', 'mostra o processo de receção: identificação da origem e do doador, registo repetido de linhas e processamento final pelo sistema, que agrupa as linhas em lotes e as encaminha para arrumação.'),
        ('act_rececao_linha', 'Registo de uma linha de receção', 'detalha o registo de uma linha, incluindo a criação de produto, a escolha da apresentação, a validade e a avaliação dos critérios de conformidade do RGDHSA049.'),
        ('act_arrumacao', 'Arrumação com sugestão de localização', 'representa a sugestão de localização para produtos à temperatura ambiente e para produtos de frio, e o ciclo em que o operador assinala locais cheios até encontrar espaço.'),
        ('act_validades', 'Controlo diário de validades', 'descreve a tarefa diária de verificação e as decisões do operador perante cada tipo de alerta: remover como desperdício, congelar, dar prioridade de saída ou pedir doações.'),
        ('act_entrega_cabaz', 'Agendamento e entrega de cabaz', 'cobre o ciclo do cabaz, desde a definição da periodicidade até ao registo da entrega e ao cálculo do próximo agendamento.'),
        ('act_refeicoes', 'Ciclo diário das refeições', 'apresenta o ciclo das refeições: pedido antecipado, consulta do número a confecionar, saída de produtos, distribuição com identificação e registo do pedido do dia seguinte.'),
    ]:
        n = r.next_fig()
        r.para(f'A Figura {n} {txt}')
        r.figure(f'{D}/{img}.png', f'Diagrama de atividade – {cap}.', max_h=20)

    # 4.3 Classes
    r.h2('Modelo de domínio')
    r.para('O modelo de domínio representa os conceitos do problema e as suas relações, independentemente da tecnologia (Larman, 2004). Foi dividido em sete diagramas de classes, um por área; as classes que pertencem a outra área aparecem sem atributos. Os tipos enumerados estão descritos na secção 5.3.')
    for img, cap, txt in [
        ('cl_catalogo', 'Catálogo', 'A **Categoria** define o tipo de bem, a condição de armazenamento e se é congelável, e pode ter uma **RegraCongelacao** (tabela de datas). O **Produto** distingue nome, marca e formato e tem uma unidade de stock. As **Apresentacoes** convertem embalagens (caixa, palete, saco) para essa unidade.'),
        ('cl_armazem', 'Armazém', 'O **Local** é abstrato e especializa-se em **Celula** (coluna, linha, andar) e **ZonaFrio** (lado D/C/E e nível), que pertence a um **EquipamentoFrio**. A operação `chaveOrdenacao()` produz a chave usada para medir a proximidade entre locais.'),
        ('cl_rececao', 'Receção', 'A **Rececao** compõe-se de **LinhaRececao**, que guardam os critérios de conformidade do RGDHSA049 e originam **Lotes**. O **Doador** é opcional, para permitir doações anónimas.'),
        ('cl_stock', 'Stock', 'O **Lote** é a unidade de gestão de stock. Guarda a validade atual e a original, as quantidades e o estado, e regista todas as alterações como **Movimentos**. O **Desperdicio** e os **Alertas** referem-se a lotes.'),
        ('cl_agregados', 'Utentes e agregados', 'O **Agregado** compõe-se de **Pessoas**. Cada pessoa pode estar autorizada a levantar, ter uma **CredencialQR** e uma **ContaUtente** na aplicação. O **Consentimento** documenta a base legal do tratamento de dados.'),
        ('cl_entregas', 'Entregas', 'Um **Agendamento** é concretizado por uma **Entrega**, que regista quem levantou e quem entregou. As **LinhaSaida** ligam a entrega aos lotes, garantindo a rastreabilidade.'),
        ('cl_refeicoes', 'Refeições', 'O **ServicoRefeicao** representa um dia e tipo de refeição. Os **PedidoRefeicao** são feitos por agregado e os **Levantamentos** por pessoa. As **SaidaCozinha** reutilizam a classe LinhaSaida para abater os lotes.'),
    ]:
        n = r.next_fig()
        r.para(f'Figura {n} – {cap}. {txt}')
        r.figure(f'{D}/{img}.png', f'Diagrama de classes – {cap}.', max_h=16)

    # 4.4 Estados
    r.h2('Diagramas de estados')
    for img, cap, txt in [
        ('st_lote', 'Lote', 'O ciclo de vida do lote é central para o controlo de validades. Um lote só pode sair para cabazes ou para a cozinha nos estados DISPONIVEL e CONGELADO; os lotes EXPIRADOS só podem ser descartados.'),
        ('st_agendamento', 'Agendamento de cabaz', 'Os agendamentos não concretizados passam a FALTOU no fim do dia (RF-ENT-09) e podem ser reagendados.'),
        ('st_pedido', 'Pedido de refeição', 'Os pedidos só podem ser criados, alterados ou cancelados até à hora limite do dia anterior (RF-REF-04); os que não forem levantados ficam como NAO_LEVANTADO no fecho do serviço, o que permite medir a fiabilidade das previsões.'),
    ]:
        n = r.next_fig()
        r.para(f'Figura {n} – {cap}. {txt}')
        r.figure(f'{D}/{img}.png', f'Diagrama de estados – {cap}.', max_w=12, max_h=12)

    # 4.5 Sequência
    r.h2('Diagramas de sequência')
    r.para('Os diagramas de sequência mostram a colaboração entre a interface, os *ViewModels*, os repositórios e os serviços Firebase nos cenários principais. As operações que alteram stock são executadas em Cloud Functions, dentro de transações do Firestore, para garantir a atomicidade (RNF-08).')
    for img, cap in [
        ('sq_rececao', 'Registar receção'),
        ('sq_arrumacao', 'Arrumar lote com local cheio'),
        ('sq_entrega', 'Entregar cabaz'),
        ('sq_refeicao', 'Registar levantamento de refeição'),
        ('sq_rgdhsa049', 'Emitir RGDHSA049'),
        ('sq_validades', 'Tarefas agendadas (validades e fecho do dia)'),
    ]:
        n = r.next_fig()
        r.para(f'A Figura {n} apresenta o cenário "{cap}".')
        r.figure(f'{D}/{img}.png', f'Diagrama de sequência – {cap}.', max_h=17)

    # 4.6 Algoritmos
    r.h2('Algoritmos principais')
    r.h3('Sugestão de localização')
    r.para('A sugestão de localização implementa as regras RN-03 a RN-06. A distância entre dois locais é medida pela diferença das suas posições na lista ordenada de locais (coluna, linha, andar). Esta aproximação será substituída por distâncias reais quando existir o mapa do armazém (Capítulo 9).')
    r.code('''
fun sugerirLocal(lote: Lote, excluir: Set<String>): Local? {
    val candidatos = locaisAtivos()
        .filter { !it.cheio && it.id !in excluir && compativel(it, condicaoEfetiva(lote)) }
        .sortedBy { it.chaveOrdenacao() }            // coluna, linha, andar (ou equipamento, lado, nível)
    if (candidatos.isEmpty()) return null

    // 1. Local não cheio que já contém o mesmo produto
    candidatos.firstOrNull { contemProduto(it, lote.produtoId) }?.let { return it }

    // 2. Local de referência: último usado pelo produto ou, na falta deste, pela categoria
    val todos = locaisAtivos().sortedBy { it.chaveOrdenacao() }
    val ref = ultimoLocal(lote.produtoId) ?: ultimoLocalCategoria(lote.categoriaId)
        ?: return preferencial(candidatos, lote.categoria).first()
    val iRef = todos.indexOf(ref)

    // 3. Local não cheio mais próximo na ordenação (em qualquer sentido)
    return candidatos.minBy { abs(todos.indexOf(it) - iRef) }
}
''')
    r.para('A função `condicaoEfetiva` devolve CONGELADO quando o lote foi congelado na origem ou internamente e, nos restantes casos, a condição de armazenamento da categoria; `compativel` garante que os produtos refrigerados vão para frigoríficos, os congelados para congeladores e os restantes para células de prateleira. A função `preferencial` ordena primeiro os equipamentos cujo uso preferencial inclui a categoria do produto, tratando-o como sugestão e não como restrição (RN-05).')

    r.h3('Seleção FEFO')
    r.para('A seleção FEFO ordena os lotes elegíveis de um produto e reparte a quantidade pedida pelos primeiros lotes, até a satisfazer:')
    r.code('''
fun selecionarFefo(produtoId: String, qtdPedida: Double): List<Pair<Lote, Double>> {
    val lotes = lotesDoProduto(produtoId)
        .filter { it.estado in setOf(DISPONIVEL, CONGELADO) && it.quantidadeAtual > 0 && it.validade >= hoje() }
        .sortedWith(compareBy<Lote>({ it.congeladoInterno }, { it.validade }, { it.dataEntrada }))
    var restante = qtdPedida
    val resultado = mutableListOf<Pair<Lote, Double>>()
    for (l in lotes) {
        if (restante <= 0) break
        val q = minOf(l.quantidadeAtual, restante)
        resultado += l to q
        restante -= q
    }
    return resultado          // se restante > 0, o stock é insuficiente
}
''')

    r.h3('Conversão de unidades e produtos a granel')
    r.para('Na receção, a quantidade em stock obtém-se multiplicando a quantidade recebida pelo fator da apresentação: uma palete de leite (fator 30) dá 30 UN. Nos produtos a granel, cuja unidade de stock é o quilograma, o lote guarda o peso (`quantidadeAtual`) e o número de volumes (`volumes`). Uma saída de 10 kg num lote de 1 volume com 50 kg deixa 1 volume com 40 kg; o número de volumes só passa a zero quando o peso se esgota (RN-02).')

    r.h3('Geração de agendamentos')
    r.para('Depois de cada entrega, ou quando o Responsável altera a periodicidade, o sistema calcula a data do próximo cabaz a partir da data da última entrega: mais 7 dias (semanal), 14 dias (quinzenal), o mesmo dia do mês seguinte (mensal) ou o número de dias definido (personalizada). Se a data calculada não for dia de distribuição, avança para o dia de distribuição seguinte. O agendamento é criado no estado AGENDADO e pode ser ajustado manualmente.')

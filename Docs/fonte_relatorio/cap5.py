DICT = {
    'CATEGORIA': [
        ('id_categoria', 'String', 'S', 'Identificador.'),
        ('nome', 'String(60)', 'S', 'Ex.: Laticínios, Massas, Carne de aves, Vestuário.'),
        ('tipo_bem', 'TipoBem', 'S', 'ALIMENTAR, HIGIENE, LIMPEZA, VESTUARIO ou OUTRO.'),
        ('condicao_armazenamento', 'CondicaoArmazenamento', 'S', 'AMBIENTE, REFRIGERADO ou CONGELADO; determina o tipo de local sugerido.'),
        ('congelavel', 'Boolean', 'S', 'Se os produtos podem ser congelados para prolongar a validade.'),
        ('dias_aviso', 'Int', 'C', 'Antecedência, em dias, do alerta de validade (por omissão 7); nulo nas categorias de bens sem validade.'),
    ],
    'REGRA_CONGELACAO': [
        ('id_categoria', 'String', 'S', 'Categoria a que a regra se aplica (uma regra por categoria).'),
        ('dias_extensao', 'Int', 'S', 'Dias a somar à data de congelação para propor a nova validade.'),
        ('observacoes', 'String', 'N', 'Indicações de preparação para congelar.'),
    ],
    'PRODUTO': [
        ('id_produto', 'String', 'S', 'Identificador.'),
        ('id_categoria', 'String', 'S', 'Categoria do produto.'),
        ('nome', 'String(80)', 'S', 'Designação (ex.: Arroz agulha).'),
        ('marca', 'String(60)', 'N', 'Marca; distingue produtos e lotes.'),
        ('formato', 'String(30)', 'N', 'Formato de venda (ex.: 1 kg, 35 cl).'),
        ('unidade_stock', 'UnidadeStock', 'S', 'UN, KG ou L.'),
        ('conteudo_por_unidade', 'Decimal', 'N', 'Conteúdo de uma unidade (ex.: 0,5 kg), para estatísticas.'),
        ('tem_validade', 'Boolean', 'S', 'Falso para vestuário e alguns bens não alimentares.'),
        ('tipo_data_validade', 'TipoDataValidade', 'N', 'CONSUMIR_ATE ou CONSUMIR_PREFERENCIA (a validar com a equipa HACCP).'),
        ('stock_minimo', 'Decimal', 'N', 'Limiar para o alerta de stock mínimo.'),
        ('tamanho, genero', 'String', 'N', 'Atributos de vestuário.'),
        ('codigo_barras', 'String', 'N', 'EAN (melhoria futura).'),
        ('ativo', 'Boolean', 'S', 'Produtos inativos não aparecem na receção.'),
    ],
    'APRESENTACAO': [
        ('id_produto', 'String', 'S', 'Produto.'),
        ('nome', 'String(30)', 'S', 'Ex.: Unidade, Caixa, Palete, Saco.'),
        ('fator', 'Decimal', 'S', 'Quantidade na unidade de stock (ex.: 30 para palete de 30 UN; 50 para saco de 50 kg).'),
    ],
    'LOCAL': [
        ('id_local', 'String', 'S', 'Identificador.'),
        ('tipo', 'TipoLocal', 'S', 'CELULA ou ZONA_FRIO.'),
        ('codigo', 'String', 'S', 'Único. Célula: xxx-xx-xx; zona: EQUIPAMENTO-LadoNível (ex.: ARCA1-D1). Codificado no QR.'),
        ('coluna, linha, andar', 'Int', 'N', 'Componentes do código da célula.'),
        ('id_equipamento, lado, nivel', 'String/Char/Int', 'N', 'Componentes da zona de frio (lado ∈ {D, C, E}).'),
        ('cheio', 'Boolean', 'S', 'Assinalado pelo operador; excluído das sugestões.'),
        ('ativo', 'Boolean', 'S', 'Locais desativados não aparecem.'),
    ],
    'EQUIPAMENTO_FRIO': [
        ('id_equipamento', 'String', 'S', 'Identificador.'),
        ('codigo', 'String', 'S', 'Código curto (ex.: ARCA1, ARCA3).'),
        ('nome', 'String', 'S', 'Descrição.'),
        ('tipo', 'TipoEquipamento', 'S', 'CONGELADOR ou FRIGORIFICO.'),
        ('categorias_preferenciais', 'Lista', 'N', 'Categorias de uso preferencial (tabela EQUIPAMENTO_CATEGORIA).'),
    ],
    'DOADOR': [
        ('id_doador', 'String', 'S', 'Identificador.'),
        ('tipo', 'TipoDoador', 'S', 'PARTICULAR, EMPRESA, ORGANIZACAO ou CAMPANHA.'),
        ('nome', 'String', 'S', 'Nome ou designação.'),
        ('nif', 'String(9)', 'N', 'Número de identificação fiscal.'),
        ('morada, contacto', 'String', 'N', 'Dados de contacto.'),
    ],
    'RECECAO': [
        ('id_rececao', 'String', 'S', 'Identificador.'),
        ('id_doador', 'String', 'N', 'Nulo quando anónima.'),
        ('id_utilizador', 'String', 'S', 'Responsável pela receção (rubrica no RGDHSA049).'),
        ('data_hora', 'Timestamp', 'S', 'Momento da receção.'),
        ('tipo_origem', 'TipoDoador', 'S', 'Origem dos bens.'),
        ('anonimo', 'Boolean', 'S', 'Doação de particular anónimo.'),
        ('n_guia', 'String', 'C', 'Obrigatório quando a origem é EMPRESA.'),
        ('url_guia', 'String', 'N', 'Caminho da imagem da guia no Cloud Storage.'),
        ('temperatura, observacoes', 'Decimal/String', 'N', 'Dados gerais da receção.'),
    ],
    'LINHA_RECECAO': [
        ('id_rececao, id_produto', 'String', 'S', 'Receção e produto.'),
        ('id_lote', 'String', 'C', 'Lote em que a linha foi agrupada (RN-01); nulo nas linhas rejeitadas.'),
        ('id_apresentacao', 'String', 'N', 'Apresentação usada (nula = unidade de stock).'),
        ('quantidade', 'Decimal', 'S', 'Quantidade na apresentação indicada.'),
        ('validade', 'Date', 'C', 'Obrigatória se o produto tem validade.'),
        ('lote_fornecedor', 'String', 'N', 'Lote ou n.º de guia indicado pelo fornecedor.'),
        ('higiene_c, rotulagem_c, organoleticas_c, embalagem_c', 'Boolean', 'S', 'Critérios Conforme/Não conforme do RGDHSA049.'),
        ('temperatura', 'Decimal', 'N', 'Temperatura medida (refrigerados e congelados).'),
        ('aceite', 'Boolean', 'S', 'Falso quando a linha é rejeitada.'),
        ('observacoes', 'String', 'N', 'Motivo da não conformidade.'),
    ],
    'LOTE': [
        ('id_lote', 'String', 'S', 'Identificador (também impresso em etiqueta, se necessário).'),
        ('id_produto', 'String', 'S', 'Produto (as linhas de receção que originaram o lote referem-no através de LINHA_RECECAO.id_lote).'),
        ('id_lote_origem', 'String', 'N', 'Lote de que este resultou por divisão (congelação parcial).'),
        ('id_local', 'String', 'N', 'Local atual (nulo enquanto pendente).'),
        ('validade', 'Date', 'N', 'Validade atual (alterada na congelação).'),
        ('validade_original', 'Date', 'N', 'Validade de origem.'),
        ('qtd_inicial, qtd_atual', 'Decimal', 'S', 'Quantidades na unidade de stock; qtd_atual ≥ 0.'),
        ('volumes', 'Int', 'N', 'Número de volumes (produtos a granel).'),
        ('estado', 'EstadoLote', 'S', 'Ciclo de vida descrito na secção 4.4.'),
        ('congelado_origem, congelado_interno', 'Boolean', 'S', 'Origem da congelação (relevante para FEFO).'),
        ('data_entrada', 'Timestamp', 'S', 'Critério de desempate FEFO.'),
    ],
    'MOVIMENTO': [
        ('id_lote, id_utilizador', 'String', 'S', 'Lote e autor.'),
        ('tipo', 'TipoMovimento', 'S', 'Tipo de movimento.'),
        ('quantidade', 'Decimal', 'S', 'Quantidade movimentada (sinal implícito no tipo).'),
        ('data_hora', 'Timestamp', 'S', 'Momento.'),
        ('id_local_origem, id_local_destino', 'String', 'N', 'Para arrumações e transferências.'),
        ('referencia', 'String', 'N', 'Id da entrega, saída para a cozinha ou receção.'),
        ('justificacao', 'String', 'C', 'Obrigatória nos movimentos de AJUSTE.'),
    ],
    'DESPERDICIO': [
        ('id_lote / id_linha_rececao', 'String', 'C', 'Lote descartado ou linha rejeitada na receção; exatamente um dos dois é preenchido.'),
        ('id_produto, id_utilizador', 'String', 'S', 'Produto (para agregações) e autor.'),
        ('quantidade', 'Decimal', 'S', 'Quantidade desperdiçada na unidade de stock.'),
        ('motivo', 'MotivoDesperdicio', 'S', 'EXPIRADO, DANIFICADO ou NAO_CONFORME.'),
        ('data', 'Date', 'S', 'Data do registo.'),
    ],
    'ALERTA': [
        ('tipo', 'TipoAlerta', 'S', 'EXPIRADO, VALIDADE_PROXIMA ou STOCK_MINIMO.'),
        ('id_lote / id_produto', 'String', 'N', 'Objeto do alerta.'),
        ('data_hora, resolvido', 'Timestamp/Boolean', 'S', 'Criação e estado.'),
    ],
    'UTILIZADOR': [
        ('id_utilizador', 'String', 'S', 'UID do Firebase Authentication.'),
        ('nome, email', 'String', 'S', 'Identificação.'),
        ('perfis', 'Lista<Perfil>', 'S', 'ADMIN, RESPONSAVEL, TECNICO, OPERADOR, COZINHA (replicados em *custom claims*).'),
        ('ativo', 'Boolean', 'S', 'Utilizadores inativos não se autenticam.'),
    ],
    'AGREGADO': [
        ('id_agregado, codigo', 'String', 'S', 'Identificador interno e código legível (ex.: A-0142).'),
        ('morada', 'String', 'S', 'Morada do agregado.'),
        ('codigo_postal, localidade, telefone', 'String', 'N', 'Contactos.'),
        ('situacao', 'String', 'N', 'Caracterização socioeconómica resumida.'),
        ('beneficia_cabaz, beneficia_refeicoes', 'Boolean', 'S', 'Respostas de que beneficia.'),
        ('periodicidade', 'Periodicidade', 'C', 'Obrigatória quando beneficia_cabaz; definida pelo Responsável.'),
        ('periodicidade_dias', 'Int', 'C', 'N.º de dias quando a periodicidade é PERSONALIZADA.'),
        ('estado', 'EstadoAgregado', 'S', 'ATIVO, SUSPENSO ou INATIVO.'),
        ('data_inscricao', 'Date', 'S', 'Data de inscrição.'),
        ('id_tecnico, observacoes', 'String', 'N', 'Técnico responsável e observações.'),
    ],
    'PESSOA': [
        ('id_pessoa, id_agregado', 'String', 'S', 'Identificação e agregado.'),
        ('nome', 'String', 'S', 'Nome completo.'),
        ('data_nascimento', 'Date', 'N', 'Para cálculo da idade.'),
        ('nif, niss', 'String', 'N', 'Identificadores fiscais e da segurança social.'),
        ('parentesco, titular', 'String/Boolean', 'S', 'Relação com o titular.'),
        ('autorizada_levantar', 'Boolean', 'S', 'Pode levantar cabazes e refeições.'),
        ('restricoes_alimentares, alergias', 'String', 'N', 'Mostrados na preparação do cabaz.'),
    ],
    'CREDENCIAL_QR': [
        ('token', 'String(32)', 'S', 'Valor aleatório criptograficamente seguro codificado no QR.'),
        ('id_pessoa', 'String', 'S', 'Titular.'),
        ('suporte, emitida_em, ativa', 'Vários', 'S', 'PAPEL ou APP; data; estado.'),
    ],
    'EQUIPAMENTO_CATEGORIA': [
        ('id_equipamento, id_categoria', 'String', 'S', 'Chave composta; associa um equipamento de frio a uma categoria de uso preferencial (sugestão).'),
    ],
    'PARAMETROS (documento único)': [
        ('hora_limite_pedidos', 'Time', 'S', 'Hora do dia anterior até à qual se podem criar, alterar ou cancelar pedidos (ex.: 16:00).'),
        ('dias_distribuicao', 'Lista<DiaSemana>', 'S', 'Dias da semana em que há distribuição de cabazes.'),
        ('hora_fecho', 'Time', 'S', 'Hora da tarefa que marca faltas e fecha os serviços do dia.'),
    ],
    'CONSENTIMENTO': [
        ('id_consentimento, id_agregado', 'String', 'S', 'Identificação e agregado.'),
        ('data_hora', 'Timestamp', 'S', 'Momento em que o consentimento foi prestado.'),
        ('finalidades', 'String', 'S', 'Finalidades consentidas (ex.: gestão do apoio alimentar, contacto por SMS).'),
        ('url_documento', 'String', 'N', 'Digitalização do documento assinado.'),
    ],
    'CONTA_UTENTE': [
        ('uid', 'String', 'S', 'UID do Firebase Authentication (autenticação por telefone).'),
        ('id_pessoa', 'String', 'S', 'Pessoa associada (única).'),
        ('telefone', 'String', 'S', 'Número de telemóvel validado por SMS.'),
    ],
    'AGENDAMENTO / ENTREGA / LINHA_SAIDA': [
        ('AGENDAMENTO.data_hora, tipo, estado', 'Vários', 'S', 'Data prevista, CABAZ ou OUTROS_BENS, estado.'),
        ('ENTREGA.id_pessoa_levantou, id_utilizador', 'String', 'S', 'Quem levantou e quem entregou.'),
        ('ENTREGA.identificacao_manual', 'Boolean', 'S', 'Verdadeiro se não foi usado o QR.'),
        ('LINHA_SAIDA.id_lote, quantidade', 'String/Decimal', 'S', 'Lote e quantidade abatida.'),
        ('LINHA_SAIDA.id_entrega / id_saida_cozinha', 'String', 'C', 'Exatamente um dos dois é preenchido (restrição de exclusividade).'),
    ],
    'SERVICO_REFEICAO / PEDIDO_REFEICAO / LEVANTAMENTO / SAIDA_COZINHA': [
        ('SERVICO_REFEICAO.data, tipo, aberto', 'Vários', 'S', 'Dia, ALMOCO ou JANTAR, se aceita pedidos.'),
        ('SERVICO_REFEICAO.total_previsto, total_confecionado', 'Int', 'N', 'Totais do dia.'),
        ('PEDIDO_REFEICAO.data', 'Date', 'S', 'Data do serviço, desnormalizada para consultas por agregado.'),
        ('PEDIDO_REFEICAO.n_refeicoes, origem, estado', 'Vários', 'S', 'Quantidade, canal (OrigemPedido) e estado.'),
        ('PEDIDO_REFEICAO.id_utilizador / uid_conta_utente', 'String', 'C', 'Quem registou: um colaborador ou a conta do utente; exatamente um.'),
        ('LEVANTAMENTO.id_pessoa, id_utilizador', 'String', 'S', 'Pessoa que levantou e colaborador que entregou.'),
        ('LEVANTAMENTO.n_entregues', 'Int', 'S', 'Refeições entregues.'),
        ('LEVANTAMENTO.justificacao_excecao', 'String', 'C', 'Obrigatória quando não há pedido.'),
        ('SAIDA_COZINHA.id_servico, id_utilizador, data_hora', 'Vários', 'S', 'Serviço a que se destinam os produtos, autor e momento.'),
    ],
}

ENUMS = [
    ('TipoBem', 'ALIMENTAR, HIGIENE, LIMPEZA, VESTUARIO, OUTRO'),
    ('CondicaoArmazenamento', 'AMBIENTE, REFRIGERADO, CONGELADO'),
    ('UnidadeStock', 'UN, KG, L'),
    ('TipoDataValidade', 'CONSUMIR_ATE, CONSUMIR_PREFERENCIA'),
    ('TipoDoador', 'PARTICULAR, EMPRESA, ORGANIZACAO, CAMPANHA'),
    ('TipoEquipamento', 'CONGELADOR, FRIGORIFICO'),
    ('TipoLocal', 'CELULA, ZONA_FRIO'),
    ('EstadoLote', 'PENDENTE_ARRUMACAO, DISPONIVEL, CONGELADO, EXPIRADO, ESGOTADO, DESCARTADO'),
    ('TipoMovimento', 'ENTRADA, ARRUMACAO, TRANSFERENCIA, CONGELACAO, SAIDA_CABAZ, SAIDA_BENS, SAIDA_COZINHA, DESPERDICIO, AJUSTE'),
    ('MotivoDesperdicio', 'EXPIRADO, DANIFICADO, NAO_CONFORME'),
    ('TipoAlerta', 'EXPIRADO, VALIDADE_PROXIMA, STOCK_MINIMO'),
    ('Perfil', 'ADMIN, RESPONSAVEL, TECNICO, OPERADOR, COZINHA'),
    ('EstadoAgregado', 'ATIVO, SUSPENSO, INATIVO'),
    ('Periodicidade', 'SEMANAL, QUINZENAL, MENSAL, PONTUAL, PERSONALIZADA (com periodicidade_dias)'),
    ('TipoAgendamento', 'CABAZ, OUTROS_BENS'),
    ('SuporteCredencial', 'PAPEL, APP'),
    ('OrigemPedido', 'BALCAO (no levantamento), COLABORADOR (técnico ou responsável), APP_UTENTE'),
    ('EstadoAgendamento', 'AGENDADO, ENTREGUE, FALTOU, CANCELADO'),
    ('TipoRefeicao', 'ALMOCO, JANTAR'),
    ('EstadoPedido', 'PEDIDO, LEVANTADO, NAO_LEVANTADO, CANCELADO'),
]

FS = [
    ('utilizadores/{uid}', 'Dados do colaborador e perfis.', 'Perfis replicados em *custom claims* pela função de administração.'),
    ('categorias/{id}', 'Categoria com a regra de congelação embebida (`regraCongelacao`).', 'Relação 1:0..1 embebida.'),
    ('produtos/{id}', 'Produto com a lista `apresentacoes` embebida e o campo derivado `stockAtual`.', '`stockAtual` mantido pelas Cloud Functions.'),
    ('locais/{id}', 'Células e zonas de frio (campo `tipo`), com `chaveOrdenacao` pré-calculada.', 'Permite ordenar diretamente por consulta.'),
    ('equipamentos/{id}', 'Equipamentos de frio e categorias preferenciais.', '–'),
    ('doadores/{id}', 'Doadores.', '–'),
    ('rececoes/{id}', 'Cabeçalho da receção e subcoleção `linhas/{id}`.', 'Nome do doador e do responsável desnormalizados para o RGDHSA049.'),
    ('lotes/{id}', 'Lote com `produtoId`, `categoriaId`, `localId`, `validade`, `estado`, `qtdAtual`.', 'Nome do produto e código do local desnormalizados para listagens.'),
    ('movimentos/{id}', 'Registo imutável de movimentos.', 'Só escrita pelas Cloud Functions.'),
    ('desperdicios/{id}', 'Registos de desperdício.', 'Inclui `categoriaId` para agregações.'),
    ('alertas/{id}', 'Alertas gerados pela tarefa diária.', 'Id determinístico (tipo + lote ou produto + data) para idempotência.'),
    ('agregados/{id}', 'Agregado, subcoleções `pessoas/{id}` e `consentimentos/{id}`.', 'Acesso restrito ao Técnico e ao Responsável; o utente só ao seu agregado.'),
    ('contasUtente/{uid}', 'Conta da App Utente: pessoa e agregado associados.', 'Criada pela função de ativação, que define o *custom claim* agregadoId.'),
    ('credenciais/{token}', 'Mapeia o token QR para a pessoa e o agregado.', 'Leitura apenas por Cloud Function.'),
    ('agendamentos/{id}', 'Agendamentos de cabazes e outros bens.', 'Leitura pelos colaboradores e pelo utente do próprio agregado.'),
    ('painelAgenda/{data}', 'Projeção do dia para o painel web: hora, código do agregado, tipo e estado.', 'Escrita só por Cloud Function; sem nomes nem dados pessoais.'),
    ('entregas/{id}', 'Entrega com as linhas embebidas (`linhas`).', 'Linhas embebidas: são sempre lidas em conjunto.'),
    ('servicosRefeicao/{data_tipo}', 'Serviço do dia (ex.: `2026-10-22_ALMOCO`).', 'Id determinístico facilita a consulta.'),
    ('pedidosRefeicao/{id}', 'Pedidos por agregado e serviço, com a data desnormalizada.', 'Escrita só pela função `registarPedido`.'),
    ('levantamentos/{id}', 'Levantamentos de refeições.', '–'),
    ('saidasCozinha/{id}', 'Saídas para a cozinha com linhas embebidas.', '–'),
    ('parametros/geral', 'Parâmetros gerais (hora limite dos pedidos, dias de distribuição, hora de fecho).', 'Documento único, gerido pelo Administrador.'),
    ('auditoria/{id}', 'Registo de operações sensíveis (acesso a dados de utentes, alterações).', 'Só escrita pelo servidor.'),
]

IDX = [
    ('lotes', 'produtoId ASC, estado ASC, congeladoInterno ASC, validade ASC', 'Seleção FEFO de um produto.'),
    ('lotes', 'estado ASC, validade ASC', 'Tarefa diária (estado in [...] e validade <= limite) e lista de expirados.'),
    ('lotes', 'localId ASC, estado ASC', 'Conteúdo de um local.'),
    ('agendamentos', 'dataHora ASC, estado ASC', 'Entregas do dia e painel web.'),
    ('pedidosRefeicao', 'servicoId ASC, estado ASC', 'Pedidos de um serviço.'),
    ('pedidosRefeicao', 'agregadoId ASC, data DESC', 'Histórico do agregado e App Utente.'),
    ('desperdicios', 'categoriaId ASC, data ASC', 'Relatório de desperdício.'),
]


def cap5(r, D):
    r.chapter('Modelo de Dados')
    r.para('Este capítulo apresenta o modelo de dados em três níveis: o modelo conceptual entidade-relacionamento, o dicionário de dados e o modelo físico em Cloud Firestore, uma base de dados NoSQL orientada a documentos.')

    r.h2('Modelo entidade-relacionamento')
    r.para('O modelo ER usa a notação de *crow\'s foot*. Para facilitar a leitura foi dividido em seis diagramas, um por área. As entidades marcadas com "(ref.)" estão definidas noutro diagrama e aparecem apenas com a chave primária. As chaves estão assinaladas como PK (primária), FK (estrangeira) e UQ (única); os atributos marcados com • são obrigatórios.')
    for img, cap, txt in [
        ('er_catalogo_armazem', 'Catálogo e armazém', 'As categorias agrupam produtos e têm no máximo uma regra de congelação. A associação muitos-para-muitos entre equipamentos e categorias (uso preferencial) é resolvida pela entidade EQUIPAMENTO_CATEGORIA. A entidade LOCAL generaliza células e zonas de frio.'),
        ('er_rececao', 'Receção', 'Cada receção tem uma ou mais linhas e pode não ter doador (anónima). Cada linha refere um produto e, opcionalmente, a apresentação usada, e origina zero ou mais lotes.'),
        ('er_stock', 'Stock', 'O lote é a entidade central do stock: refere o produto, a linha de origem e o local atual e tem associados os movimentos, os desperdícios e os alertas.'),
        ('er_agregados', 'Agregados e pessoas', 'Um agregado tem uma ou mais pessoas e um ou mais consentimentos. Cada pessoa pode ter credenciais QR (só uma ativa) e uma conta na App Utente.'),
        ('er_entregas', 'Entregas', 'Uma entrega pertence a um agregado, pode concretizar um agendamento e regista a pessoa que levantou e o colaborador que entregou. As linhas de saída ligam a entrega aos lotes abatidos.'),
        ('er_refeicoes', 'Refeições', 'Os pedidos ligam o agregado ao serviço de refeição. Os levantamentos registam a pessoa e podem existir sem pedido (exceções). As saídas para a cozinha reutilizam as linhas de saída.'),
    ]:
        n = r.next_fig()
        r.para(f'Figura {n} – {cap}. {txt}')
        r.figure(f'{D}/{img}.png', f'Modelo entidade-relacionamento – {cap}.', max_h=17)

    r.h2('Dicionário de dados')
    first = r.next_tab()
    r.para(f'As tabelas seguintes (Tabela {first} à Tabela {first + len(DICT) - 1}) descrevem os atributos das entidades. Na coluna "Obr." indica-se se o atributo é obrigatório (S), opcional (N) ou condicionalmente obrigatório (C). Atributos com a mesma natureza aparecem agrupados.')
    for ent, rows in DICT.items():
        r.table(['Atributo', 'Tipo', 'Obr.', 'Descrição'], [list(x) for x in rows],
                f'Dicionário de dados – {ent}.', widths=[3.2, 2.2, 0.8, 4.4])

    r.h2('Tipos enumerados')
    n = r.next_tab()
    r.para(f'A Tabela {n} lista os tipos enumerados usados no modelo. Em Kotlin são implementados como `enum class` e no Firestore são guardados como texto.')
    r.table(['Tipo', 'Valores'], [list(x) for x in ENUMS], 'Tipos enumerados.', widths=[3, 7], first_bold=True)

    r.h2('Modelo físico em Cloud Firestore')
    r.paras(
        'O Cloud Firestore organiza os dados em coleções de documentos JSON, sem junções nem chaves estrangeiras impostas pela base de dados (Google, 2026b). A passagem do modelo ER para o Firestore seguiu três critérios: (i) **incorporar** (*embedding*) no documento as relações de composição que são sempre lidas em conjunto e têm cardinalidade limitada (apresentações no produto, linhas na entrega); (ii) usar **subcoleções** quando os filhos podem crescer ou ter acessos diferentes (linhas da receção, pessoas do agregado); e (iii) **desnormalizar** os campos necessários às listagens (nome do produto e código do local no lote), mantendo-os coerentes através das Cloud Functions.',
    )
    n = r.next_tab()
    r.para(f'A Tabela {n} apresenta as coleções propostas.')
    r.table(['Coleção / documento', 'Conteúdo', 'Notas'], [list(x) for x in FS],
            'Coleções do Cloud Firestore.', widths=[3, 4.2, 3.2])
    r.para('Exemplo de um documento da coleção `lotes`:')
    r.code('''
lotes/L-0912 {
  "produtoId": "p_iogurte_natural_pd",  "produtoNome": "Iogurte natural PD x4",
  "categoriaId": "c_laticinios",        "rececaoId": "r_2026_0153",
  "localId": "loc_arca3_c1",            "localCodigo": "ARCA3-C1",
  "validade": "2026-10-24",            "validadeOriginal": "2026-10-24",
  "qtdInicial": 6, "qtdAtual": 6, "unidade": "UN", "volumes": null,
  "estado": "DISPONIVEL", "congeladoOrigem": false, "congeladoInterno": false,
  "loteOrigemId": null,                 "dataEntrada": "2026-10-22T10:15:00Z"
}
''')
    n = r.next_tab()
    r.para(f'As consultas compostas exigem índices declarados no ficheiro `firestore.indexes.json`. A Tabela {n} lista os principais.')
    r.table(['Coleção', 'Campos do índice', 'Consulta suportada'], [list(x) for x in IDX],
            'Índices compostos do Firestore.', widths=[2.2, 4.6, 3.6])

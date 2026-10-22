def cap1(r, D):
    r.chapter('Introdução')
    r.paras(
        'O desperdício alimentar e a insegurança alimentar coexistem nas sociedades contemporâneas. Estima-se que cerca de um terço dos alimentos produzidos para consumo humano se perca ou desperdice ao longo da cadeia de abastecimento (Gustavsson et al., 2011), ao mesmo tempo que muitas famílias dependem de apoio alimentar para satisfazer necessidades básicas. As instituições particulares de solidariedade social (IPSS) estão no ponto de encontro destas duas realidades: recebem excedentes e doações de particulares, empresas de distribuição e campanhas, e transformam-nos em cabazes de alimentos e refeições para quem mais precisa.',
        'Esta atividade, aparentemente simples, encerra uma complexidade logística considerável. Os bens chegam de forma irregular, em quantidades e formatos muito variados (uma unidade de feijão de 500 g, uma palete com 30 pacotes de leite, um saco de 50 kg de batatas), com prazos de validade por vezes muito curtos, e têm de ser armazenados em prateleiras, frigoríficos e arcas congeladoras. A distribuição exige que se dê prioridade aos produtos que expiram primeiro, que se registe quem recebeu o quê e que se cumpram as regras de segurança alimentar, nomeadamente o registo de controlo da receção de matérias-primas previsto no sistema de Análise de Perigos e Pontos Críticos de Controlo (HACCP), exigido pelo regulamento europeu relativo à higiene dos géneros alimentícios (Parlamento Europeu e Conselho, 2004).',
        'Quando estes processos assentam em papel e na memória dos colaboradores, a instituição perde visibilidade sobre o seu stock, tem dificuldade em evitar que os produtos expirem nas prateleiras e despende tempo considerável em registos administrativos. Os sistemas de informação, e em particular as aplicações móveis ligadas a serviços na nuvem, permitem registar cada operação no momento e no local em que acontece, calcular automaticamente prioridades e produzir indicadores e documentos obrigatórios sem trabalho adicional.',
        'O presente documento descreve a análise e modelação de um sistema de informação para a gestão do Espaço Social do GASC – Grupo de Acção Social Cristã, de Barcelos, com foco na gestão do armazém de bens doados, na distribuição de cabazes e outros bens e na gestão das refeições servidas pela instituição. O sistema será desenvolvido como uma aplicação móvel Android em Kotlin, suportada pela plataforma Firebase, de acordo com os requisitos tecnológicos definidos pela instituição. O documento cobre a fase de análise e modelação; a implementação e a avaliação de resultados são etapas posteriores, para as quais se deixam definidos o plano e os critérios de aceitação.',
    )

    r.h2('Objetivos')
    r.para('O objetivo geral do trabalho é conceber um sistema de informação que permita ao GASC gerir de forma rigorosa e eficiente os bens recebidos, o seu armazenamento e a sua distribuição aos utentes, reduzindo o desperdício alimentar e o esforço administrativo. Este objetivo decompõe-se nos seguintes objetivos específicos:')
    r.numbered([
        'Caracterizar o funcionamento atual do Espaço Social do GASC e identificar as necessidades dos diferentes intervenientes (colaboradores, Responsável da instituição e utentes).',
        'Levantar e documentar de forma sistemática os requisitos funcionais e não funcionais do sistema, distinguindo o que integra o produto mínimo viável (MVP) do que constitui evolução futura.',
        'Modelar o sistema através da linguagem de modelação unificada (UML) (casos de uso, atividades, classes, estados e sequências) e do modelo entidade-relacionamento, de modo a suportar uma implementação consistente.',
        'Especificar a interface através de protótipos de alta fidelidade de todos os ecrãs, rastreáveis aos requisitos.',
        'Definir uma arquitetura tecnológica baseada em Kotlin e Firebase que garanta segurança, rastreabilidade e facilidade de utilização em dispositivos Android.',
        'Garantir o registo de toda a informação necessária ao preenchimento automático do documento RGDHSA049 – Monitorização do Controlo da Receção de Matérias-Primas.',
        'Registar as funcionalidades que, por complexidade ou dependência tecnológica, não integram a primeira versão, como intenção futura de melhoria devidamente fundamentada.',
    ])
    n = r.next_tab()
    r.para(f'Para que o sucesso do sistema possa ser avaliado depois da implementação, definem-se na Tabela {n} os indicadores e as metas associados ao objetivo geral. Os valores de referência serão medidos no primeiro mês de utilização, uma vez que a instituição não dispõe hoje de registos digitais que os permitam calcular.')
    r.table(['Indicador', 'Meta', 'Forma de medição'], [
        ['Quantidade descartada por expiração', 'Redução de 30% ao fim de 6 meses, face ao 1.º mês', 'Registos de desperdício com motivo EXPIRADO (UN, kg e L, por categoria)'],
        ['Preenchimento do RGDHSA049', '100% gerado pelo sistema, sem registo manual', 'Receções registadas vs. documentos emitidos'],
        ['Tempo de registo de uma receção de 5 linhas', '≤ 5 minutos', 'Medição nos testes de aceitação e de usabilidade'],
        ['Entregas com identificação registada', '100% das entregas e levantamentos', 'Entregas com pessoa identificada (QR ou manual)'],
        ['Diferença entre refeições previstas e confecionadas', '≤ 10% por serviço', 'Total previsto vs. total confecionado (ServicoRefeicao)'],
        ['Satisfação dos utilizadores', 'Pontuação SUS ≥ 70', 'Questionário SUS (secção 8.1)'],
    ], 'Indicadores e metas do projeto.', widths=[3.2, 3.2, 3.8])

    r.h2('Contexto')
    r.paras(
        'O GASC – Grupo de Acção Social Cristã é uma IPSS sediada em Barcelos, nascida em 1978 de um grupo de voluntários da Igreja de Santo António (GASC, 2026). Ao longo de quase cinco décadas evoluiu de uma resposta essencialmente alimentar e de rua para um modelo multidisciplinar, com cerca de 45 colaboradores e dez respostas sociais em funcionamento, que vão do apoio a vítimas de violência doméstica ao acompanhamento de pessoas em situação de sem-abrigo e de dependências.',
        'A área de carência socioeconómica é a de maior volume. Em 2025, a distribuição de bens alimentares abrangeu 1 038 beneficiários e 2 729 cabazes, a Cantina Social serviu, em média, 247 refeições por mês e o Refeitório Social, que funciona 365 dias por ano, acompanhou 61 processos ativos (GASC, 2026). A instituição recebe bens em espécie de grandes superfícies e de dezenas de comerciantes locais, além de doações de particulares e de campanhas.',
        'Este trabalho insere-se no projeto **Barcelos Solidário**, uma parceria entre o GASC, a Câmara Municipal de Barcelos (CMB) e o Instituto Politécnico do Cávado e do Ave (IPCA) para desenvolver uma plataforma de resposta às necessidades sociais dos cidadãos do concelho, em especial dos que se encontram em maior vulnerabilidade económica e social (GASC et al., 2026). No centro do projeto está o Espaço Social: um espaço de acolhimento e distribuição gratuita de bens de primeira necessidade (alimentares, de higiene pessoal, de limpeza e vestuário), com origem em particulares, empresas, organizações e campanhas. O sistema aqui analisado é o primeiro componente desta plataforma e foca-se na otimização da gestão do Espaço Social.',
    )

    r.h2('Metodologia')
    r.paras(
        'O trabalho seguiu uma abordagem iterativa de engenharia de requisitos (Wiegers & Beatty, 2013; Sommerville, 2016; Pressman & Maxim, 2020). As fontes de informação foram a descrição do problema fornecida pela instituição (documento *Projeto – GASC*), a apresentação do projeto Barcelos Solidário (GASC et al., 2026), exemplos reais de guias de transporte e de resumos de doações, e o modelo do registo RGDHSA049. Seguiram-se três rondas de perguntas e respostas escritas com o Responsável da instituição (outubro de 2026), que permitiram clarificar regras de negócio decisivas, como a forma de contar unidades, a codificação das prateleiras e das arcas, a gestão das pessoas autorizadas a levantar cabazes ou o registo antecipado das refeições. O resultado destas rondas está documentado na secção 3.7.',
        'Os requisitos foram priorizados com o método MoSCoW (*Must, Should, Could, Won\'t*) (Clegg & Barker, 1994), associando cada requisito a uma fase: **MVP** (primeira versão funcional) ou **Futuro** (melhoria planeada). A modelação recorreu à UML 2.5.1 (Object Management Group, 2017) e ao modelo entidade-relacionamento (Chen, 1976). Os diagramas foram produzidos em PlantUML (PlantUML, 2026) e os protótipos em HTML/CSS, para que o código-fonte de ambos possa ser versionado com o projeto.',
    )

    r.h2('Estrutura do documento')
    r.para('Para além deste capítulo introdutório, o documento está organizado da seguinte forma:')
    r.bullets([
        '**Capítulo 2 – Análise do Problema:** caracteriza a instituição e o processo atual, identifica os problemas, analisa o estado da arte e define o âmbito da solução.',
        '**Capítulo 3 – Análise de Requisitos:** apresenta os atores, a matriz de permissões, os requisitos funcionais e não funcionais, as regras de negócio e a validação dos requisitos.',
        '**Capítulo 4 – Modelação do Sistema:** reúne os diagramas de casos de uso e respetivas descrições, os diagramas de atividade, de classes, de estados e de sequência, e os algoritmos principais.',
        '**Capítulo 5 – Modelo de Dados:** apresenta o modelo entidade-relacionamento, o dicionário de dados e o mapeamento para a base de dados Cloud Firestore.',
        '**Capítulo 6 – Protótipos da Interface:** apresenta, pela sequência funcional, os *mockups* de alta fidelidade de todos os ecrãs, com a explicação de cada um.',
        '**Capítulo 7 – Arquitetura e Implementação Proposta:** descreve as tecnologias, as alternativas consideradas, a arquitetura, a segurança e a proteção de dados, o planeamento e os riscos.',
        '**Capítulo 8 – Plano de Testes e Validação:** define a estratégia de testes, os casos de teste de aceitação e os critérios de aceitação do MVP.',
        '**Capítulo 9 – Trabalho Futuro:** regista as funcionalidades que ficam fora da primeira versão e a forma de as concretizar.',
        '**Capítulo 10 – Conclusão:** sintetiza o trabalho realizado, as principais decisões e as limitações.',
        '**Anexos A a C:** mapeamento do registo RGDHSA049, exemplos de guias de transporte e matriz de rastreabilidade entre requisitos, casos de uso e *mockups*.',
    ])


def cap2(r, D):
    r.chapter('Análise do Problema')
    r.para('Este capítulo descreve o funcionamento atual do Espaço Social, os problemas que motivam o sistema, as soluções existentes e as linhas gerais da solução proposta.')

    r.h2('A instituição e o Espaço Social')
    r.paras(
        'O Espaço Social do GASC recebe bens de quatro tipos de origem: **particulares**, que podem ou não querer identificar-se; **empresas**, sobretudo cadeias de distribuição alimentar, cujas entregas são acompanhadas de guia de transporte; **organizações**; e **campanhas** de recolha. Os bens são maioritariamente alimentares, mas incluem também produtos de higiene pessoal, de limpeza e vestuário.',
        'Os alimentos são guardados num armazém composto por um conjunto de prateleiras e por três equipamentos de frio: a arca 1, com três zonas e usada preferencialmente para carnes de aves; a arca 2, com duas zonas, para qualquer alimento congelado; e a arca 3, que não congela e funciona como frigorífico. As saídas têm dois destinos principais: os **cabazes** entregues aos agregados familiares apoiados, segundo uma periodicidade definida pelo Responsável da instituição, e a **cozinha** da instituição, que confeciona as refeições distribuídas diariamente (normalmente o almoço e, em situações excecionais como dias de muito frio, também o jantar).',
    )
    n = r.next_fig()
    r.para(f'A Figura {n} apresenta o diagrama de contexto do sistema, com as entidades externas e os principais fluxos de informação.')
    r.figure(f'{D}/ctx_sistema.png', 'Diagrama de contexto do sistema.', max_w=13)

    r.h2('Processo atual')
    r.para('Com base na descrição da instituição e nos documentos fornecidos, o processo atual pode ser decomposto nas seguintes etapas:')
    r.bullets([
        '**Receção.** Os bens chegam e são verificados. Nas entregas de empresas existe uma guia de transporte, que chega sempre digitalizada (ver Anexo B). Para cada receção deve ser preenchido o registo RGDHSA049, que avalia a higiene, a rotulagem e validade, as características organoléticas, a integridade da embalagem e a temperatura (ver Anexo A).',
        '**Identificação e arrumação.** Cada produto é identificado pelo tipo, pela origem e pela data de validade, e guardado junto de produtos iguais. Quando uma prateleira está cheia procura-se outra, o mais próxima possível.',
        '**Gestão de validades.** Os produtos com a validade a terminar têm prioridade de saída. Alguns podem ser congelados para prolongar a validade, segundo uma tabela de referência por categoria. Os que expiram sem ser consumidos são retirados como desperdício.',
        '**Distribuição de cabazes.** Os cabazes são preparados para os agregados apoiados. A identificação de quem levanta é feita em papel.',
        '**Refeições.** Os produtos entregues à cozinha saem do stock. As pessoas que pretendem refeições registam habitualmente a intenção no dia anterior, quando levantam a refeição do dia, e são identificadas no levantamento.',
    ])

    r.h2('Problemas e necessidades identificados')
    r.para(f'A análise do processo permitiu identificar os problemas resumidos na Tabela {r.next_tab()}, bem como a necessidade a que o sistema deve dar resposta.')
    r.table(['Problema', 'Consequência', 'Necessidade'], [
        ['Ausência de inventário atualizado em tempo real', 'Desconhecimento das quantidades e validades disponíveis; dificuldade em planear cabazes e refeições', 'Registo de todas as entradas e saídas no momento em que ocorrem'],
        ['Localização dos produtos dependente da memória', 'Tempo perdido a procurar produtos; prateleiras com produtos misturados', 'Sugestão automática de localização e identificação das células por código QR'],
        ['Controlo de validades manual', 'Produtos que expiram nas prateleiras; desperdício', 'Ordenação FEFO, alertas de validade e apoio à decisão de congelar'],
        ['Registos em papel (RGDHSA049, entregas, refeições)', 'Duplicação de trabalho, erros e dificuldade de consulta', 'Registo digital único e emissão automática de documentos'],
        ['Identificação de utentes em papel', 'Dificuldade em verificar quem pode levantar bens em nome do agregado', 'Credencial QR por pessoa autorizada, em papel ou na App Utente'],
        ['Número de refeições incerto', 'Confeção em excesso ou em falta', 'Registo antecipado de pedidos de refeição por agregado e por dia'],
        ['Inexistência de indicadores', 'Dificuldade em prestar contas a financiadores e em fundamentar candidaturas', 'Histórico, painel de indicadores e exportação de dados'],
    ], 'Problemas identificados e necessidades correspondentes.', widths=[3, 3.4, 3.4])

    r.h2('Estado da arte')
    r.paras(
        'A gestão de stock em bancos alimentares e instituições sociais tem particularidades que a afastam dos sistemas de gestão de armazém (WMS) comerciais. Os bens são doados e não comprados, a sua chegada é imprevisível, não existe um catálogo fechado de artigos e a prioridade de saída é determinada pela validade e não pela ordem de entrada. Por esta razão, a estratégia adequada é FEFO (*First Expired, First Out*), e não FIFO (*First In, First Out*).',
        'Existem soluções comerciais específicas para bancos alimentares, sobretudo no mercado norte-americano. O Link2Feed é um sistema na nuvem centrado na admissão e acompanhamento de beneficiários, com relatórios e acompanhamento de programas (Link2Feed, 2026). O PantrySoft combina a gestão de beneficiários e visitas com o inventário, incluindo a leitura de códigos de barras na entrada e na saída de artigos (Cedar Mountain Software, 2026). De acordo com a informação pública destes produtos, nenhum contempla a localização física dos lotes em células de prateleira e zonas de equipamentos de frio, a congelação de produtos em fim de prazo com nova validade, nem o registo de controlo de receção usado em Portugal (RGDHSA049); são ainda soluções pagas, em inglês, desenhadas para os programas de apoio norte-americanos. Os sistemas de planeamento de recursos empresariais (ERP) genéricos cobrem a gestão de stock, mas não modelam conceitos como agregado familiar, pessoa autorizada a levantar ou pedido de refeição, e exigem uma parametrização desproporcionada para uma IPSS.',
    )
    n = r.next_tab()
    r.para(f'A Tabela {n} sintetiza esta comparação qualitativa, feita pelo autor a partir da informação pública dos produtos e dos requisitos levantados.')
    r.table(['Critério', 'Papel / folha de cálculo', 'ERP genérico', 'Software para bancos alimentares', 'Solução proposta'], [
        ['Stock por lote e validade (FEFO)', 'Manual', 'Sim', 'Parcial', 'Sim'],
        ['Localização em células e zonas de frio', 'Não', 'Parametrizável', 'Não', 'Sim'],
        ['Congelação com nova validade', 'Manual', 'Não', 'Não', 'Sim'],
        ['Registo HACCP (RGDHSA049)', 'Manual', 'Não', 'Não', 'Sim'],
        ['Agregados e pessoas autorizadas', 'Manual', 'Não', 'Sim', 'Sim'],
        ['Pedidos de refeição', 'Manual', 'Não', 'Não', 'Sim'],
        ['Língua portuguesa e RGPD (UE)', 'Sim', 'Variável', 'Não', 'Sim'],
        ['Custo para a instituição', 'Baixo', 'Elevado', 'Subscrição', 'Baixo (Firebase)'],
    ], 'Comparação qualitativa de abordagens.', widths=[3.0, 1.8, 1.7, 2.0, 1.7], size=8.5)
    r.para('No plano tecnológico, as plataformas *Backend as a Service* (BaaS), como o Firebase, permitem construir aplicações móveis com autenticação, base de dados em tempo real, armazenamento de ficheiros e funções na nuvem sem gerir servidores (Google, 2026a). As bibliotecas de visão computacional que correm no próprio dispositivo, como o ML Kit, permitem ler códigos QR e de barras e reconhecer texto por reconhecimento ótico de caracteres (OCR) (Google, 2026c). Os grandes modelos de linguagem (LLM), em particular os multimodais, abrem a possibilidade de extrair automaticamente os artigos de uma guia digitalizada ou de reconhecer produtos por imagem. Estas capacidades sustentam várias das melhorias futuras descritas no Capítulo 9.')

    r.h2('Solução proposta e âmbito')
    r.paras(
        'Propõe-se um sistema composto por uma aplicação Android para os colaboradores (**GASC Gestão**), uma aplicação Android para os utentes (**GASC Utente**, designada no resto do documento por App Utente) e um painel web simples para afixar a agenda de entregas em ecrãs de parede, todos suportados por um *backend* Firebase. A aplicação de gestão cobre a receção, a arrumação, o stock, as entregas, as refeições, os relatórios e a administração. A App Utente permite apresentar a credencial QR, consultar as próximas entregas e registar pedidos de refeição.',
        'Atendendo à dimensão do problema, o âmbito foi dividido em duas fases, por acordo com o Responsável da instituição. O **MVP** inclui as funcionalidades essenciais à operação diária, com registo manual assistido: receção com controlo RGDHSA049, sugestão de localização, FEFO, congelação, desperdício, utentes e agregados, credenciais QR, cabazes compostos manualmente com sugestão FEFO, refeições, alertas e relatórios. As funcionalidades dependentes de inteligência artificial ou de maior complexidade, como o reconhecimento de produtos e validades por imagem, a leitura automática de guias, a identificação biométrica, o cabaz automático equilibrado e a sugestão de pratos, ficam registadas como **trabalho futuro** (Capítulo 9). O modelo de dados prevê desde já os campos de que essas funcionalidades necessitam.',
    )

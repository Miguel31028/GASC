// Ecrãs da aplicação GASC Gestão: acesso, receção, arrumação, stock e utentes.
import { ic, appbar, bnav, field, li, chip, tag, btn, seg, cnc, stepper, phone } from './componentes.mjs';

export const ecrasA = q => [
  // ---------------------------------------------------------------- Acesso e início
  { id: 'M01', grupo: 'Acesso e início', titulo: 'Autenticação', html: phone(`
    <div class="content" style="padding:40px 28px 20px;gap:16px">
      <div class="col" style="align-items:center;gap:10px;margin-bottom:18px">
        <div style="width:84px;height:84px;border-radius:24px;background:var(--primary);display:flex;align-items:center;justify-content:center;color:#fff">${ic('volunteer_activism', 's48 fill')}</div>
        <div class="title-l" style="font-weight:500">GASC Gestão</div>
        <div class="muted small center">Espaço Social · Barcelos Solidário</div>
      </div>
      ${field('Email', 'ana.costa@gasc-ipss.org', { icon: 'mail' })}
      ${field('Palavra-passe', '••••••••••', { icon: 'lock', trail: 'visibility', cls: 'focus' })}
      <div class="row" style="justify-content:flex-end;margin-top:-6px"><span class="btn text">Esqueci-me da palavra-passe</span></div>
      ${btn('Entrar', 'filled', '', 'block lg')}
      <div class="spacer"></div>
      <div class="muted xs center">Acesso reservado a colaboradores do GASC.<br>Versão 1.0.0</div>
    </div>`) },

  { id: 'M02', grupo: 'Acesso e início', titulo: 'Início – Operador de armazém', html: phone(`
    ${appbar({ title: 'Bom dia, Ana', sub: 'Operador de armazém · qui., 22 out.', lead: '', actions: ['<span style="position:relative">' + ic('notifications') + '<span class="badge" style="position:absolute;top:-6px;right:-8px">5</span></span>', 'account_circle'] })}
    <div class="content">
      <div class="row">
        <div class="kpi"><div class="v">4</div><div class="l">Lotes por arrumar</div></div>
        <div class="kpi"><div class="v">7</div><div class="l">Entregas hoje</div></div>
        <div class="kpi" style="border-color:var(--error)"><div class="v" style="color:var(--error)">3</div><div class="l">Expirados</div></div>
      </div>
      <div class="section">Ações rápidas</div>
      <div class="row">
        ${btn('Nova receção', 'filled', 'move_to_inbox', 'grow')}
        ${btn('Ler QR', 'tonal', 'qr_code_scanner')}
      </div>
      <div class="section">Requer atenção</div>
      <div class="card elev" style="padding:0">
        <div class="list">
          ${li({ lead: 'delete_forever', leadCls: 'err', h: '3 lotes expirados', s: 'Remover como desperdício', trail: ic('chevron_right') })}
          ${li({ lead: 'schedule', leadCls: 'warn', h: '8 lotes a expirar em 3 dias', s: 'Iogurtes, fiambre, alface…', trail: ic('chevron_right') })}
          ${li({ lead: 'inventory', leadCls: '', h: '4 lotes por arrumar', s: 'Receção 2026-0153 · Pingo Doce', trail: ic('chevron_right') })}
          ${li({ lead: 'trending_down', leadCls: 'warn', h: 'Stock mínimo: Leite, Azeite', s: '2 produtos abaixo do mínimo', trail: ic('chevron_right') })}
        </div>
      </div>
      <div class="section">Próxima entrega</div>
      <div class="card outlined row"><div class="grow"><div class="title-s">10:30 · Agregado A-0142 (Silva)</div><div class="small muted">Cabaz quinzenal · 4 pessoas</div></div>${tag('Agendado', 'info')}</div>
    </div>
    ${bnav('Início')}`) },

  { id: 'M03', grupo: 'Acesso e início', titulo: 'Menu "Mais" e mudança de perfil', html: phone(`
    ${appbar({ title: 'Mais', lead: '' })}
    <div class="content np">
      <div class="row" style="padding:6px 16px 14px;gap:14px">
        <div style="width:52px;height:52px;border-radius:26px;background:var(--primary-container);display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:500">AC</div>
        <div class="grow"><div class="title-m">Ana Costa</div><div class="small muted">ana.costa@gasc-ipss.org</div>
          <div class="row" style="gap:4px;margin-top:4px">${tag('Operador', 'prim')}${tag('Responsável', 'prim')}</div></div>
      </div>
      <div class="divider"></div>
      <div class="list nob">
        ${li({ lead: 'restaurant', leadCls: 'plain', h: 'Refeições', cls: 'dense' })}
        ${li({ lead: 'groups', leadCls: 'plain', h: 'Utentes e agregados', cls: 'dense' })}
        ${li({ lead: 'notifications', leadCls: 'plain', h: 'Alertas', trail: '<span class="badge">5</span>', cls: 'dense' })}
        ${li({ lead: 'assessment', leadCls: 'plain', h: 'Relatórios e indicadores', cls: 'dense' })}
        ${li({ lead: 'local_shipping', leadCls: 'plain', h: 'Doadores', cls: 'dense' })}
      </div>
      <div class="divider"></div>
      <div class="section" style="padding:10px 16px 0">Administração</div>
      <div class="list nob">
        ${li({ lead: 'grid_view', leadCls: 'plain', h: 'Células de prateleira', cls: 'dense' })}
        ${li({ lead: 'kitchen', leadCls: 'plain', h: 'Equipamentos de frio', cls: 'dense' })}
        ${li({ lead: 'category', leadCls: 'plain', h: 'Categorias e congelação', cls: 'dense' })}
        ${li({ lead: 'manage_accounts', leadCls: 'plain', h: 'Utilizadores e perfis', cls: 'dense' })}
      </div>
      <div class="divider"></div>
      ${li({ lead: 'logout', leadCls: 'plain', h: 'Terminar sessão', cls: 'dense' })}
    </div>
    ${bnav('Mais')}`) },

  // ---------------------------------------------------------------- Receção
  { id: 'M04', grupo: 'Receção', titulo: 'Nova receção – origem e doador', html: phone(`
    ${appbar({ title: 'Nova receção', sub: 'Passo 1 de 3 · Origem', lead: 'close' })}
    <div class="progress"><div style="width:33%"></div></div>
    <div class="content" style="padding-top:14px">
      <div class="label">Origem dos bens</div>
      ${seg(['Empresa', 'Particular', 'Organização', 'Campanha'], 'Empresa')}
      ${field('Empresa doadora', 'Pingo Doce – Barcelos Alcaides de Faria', { icon: 'store', trail: 'arrow_drop_down' })}
      ${field('N.º da guia de transporte *', 'DPM1/4101774379', { icon: 'receipt_long', cls: 'focus', support: 'Obrigatório para receções de empresas' })}
      ${field('Data e hora', '22/10/2026  10:15', { icon: 'event' })}
      <div class="label">Guia digitalizada</div>
      <div class="card outlined row" style="gap:12px">
        <div style="width:58px;height:74px;border-radius:6px;background:repeating-linear-gradient(#fff,#fff 6px,#dfe5e1 6px,#dfe5e1 8px);border:1px solid var(--outline-var)"></div>
        <div class="grow"><div class="title-s">guia_4101774379.jpg</div><div class="small muted">Fotografada às 10:14 · 1,2 MB</div></div>
        <div class="ib">${ic('delete')}</div>
      </div>
      ${btn('Fotografar outra página', 'outlined', 'photo_camera')}
      ${field('Temperatura à chegada (ºC)', '4,0', { icon: 'device_thermostat' })}
    </div>
    <div class="bottombar">${btn('Seguinte', 'filled', 'arrow_forward')}</div>`) },

  { id: 'M05', grupo: 'Receção', titulo: 'Pesquisa de produto', html: phone(`
    ${appbar({ title: 'Adicionar produto', sub: 'Receção 2026-0153 · Pingo Doce', lead: 'arrow_back', actions: ['barcode_scanner'] })}
    <div class="content np" style="gap:0">
      <div style="padding:4px 16px 10px"><div class="search">${ic('search')}<span class="grow">leite meio</span>${ic('close')}</div></div>
      <div class="row wrap" style="padding:0 16px 8px;gap:6px">${chip('Todos', true)}${chip('Lacticínios')}${chip('Bebidas')}${chip('Recentes', false, 'history')}</div>
      <div class="list">
        ${li({ lead: 'LM', h: 'Leite meio-gordo <b>Mimosa</b> 1 L', s: 'Lacticínios · UN · 3 apresentações', trail: 'stock 46 UN' })}
        ${li({ lead: 'LM', h: 'Leite meio-gordo <b>Pingo Doce</b> 1 L', s: 'Lacticínios · UN · 2 apresentações', trail: 'stock 12 UN' })}
        ${li({ lead: 'LM', h: 'Leite meio-gordo <b>Agros</b> 35 cl', s: 'Lacticínios · UN · palete 30 UN', trail: 'stock 0 UN', cls: 'sel' })}
        ${li({ lead: 'LM', h: 'Leite meio-gordo s/ lactose <b>Mimosa</b> 1 L', s: 'Lacticínios · UN', trail: 'stock 6 UN' })}
      </div>
      <div class="card info row" style="margin:12px 16px;gap:10px">${ic('lightbulb')}<div class="small">Não encontra o produto? Crie-o: o catálogo cresce à medida que as receções são registadas.</div></div>
      <div style="padding:0 16px">${btn('Criar novo produto', 'tonal', 'add', 'block')}</div>
    </div>`) },

  { id: 'M06', grupo: 'Receção', titulo: 'Criar produto', html: phone(`
    ${appbar({ title: 'Adicionar produto', lead: 'arrow_back' })}
    <div class="scrim"></div>
    <div class="sheet" style="top:96px">
      <div class="handle"></div>
      <div class="title-m">Novo produto</div>
      ${field('Nome *', 'Batata branca', { cls: 'focus' })}
      <div class="row">${field('Marca', 'Sem marca', {}).replace('class="field ', 'class="field grow ')}${field('Formato', 'Saco 50 kg').replace('class="field ', 'class="field grow ')}</div>
      ${field('Categoria *', 'Frutas e legumes', { trail: 'arrow_drop_down', support: 'Ambiente · não congelável · aviso 3 dias' })}
      <div class="label">Unidade de stock</div>
      ${seg(['UN', 'KG', 'L'], 'KG')}
      <div class="row sb"><div><div class="title-s">Tem data de validade</div><div class="small muted">Desligar para vestuário e outros bens</div></div><div class="switch on"></div></div>
      <div class="label">Apresentações</div>
      <div class="row wrap" style="gap:6px">${chip('Quilograma (1 kg)', true)}${chip('Saco = 50 kg', true)}${chip('Adicionar', false, 'add')}</div>
      ${field('Stock mínimo (kg)', '20')}
      <div class="row" style="justify-content:flex-end;gap:8px">${btn('Cancelar', 'text')}${btn('Criar produto', 'filled')}</div>
    </div>`) },

  { id: 'M07', grupo: 'Receção', titulo: 'Linha de produto – quantidade e validade', html: phone(`
    ${appbar({ title: 'Leite meio-gordo Agros 35 cl', sub: 'Passo 2 de 3 · Linha 3', lead: 'arrow_back' })}
    <div class="progress"><div style="width:66%"></div></div>
    <div class="content" style="padding-top:14px">
      <div class="label">Apresentação</div>
      ${seg(['Unidade', 'Caixa (12)', 'Palete (30)'], 'Palete (30)')}
      <div class="row sb"><div class="title-s">Quantidade</div>${stepper('1')}</div>
      <div class="card primary row" style="gap:10px">${ic('calculate')}<div class="grow"><div class="title-s">= 30 UN em stock</div><div class="small">1 palete × 30 unidades de 35 cl</div></div></div>
      ${field('Data de validade *', '15/11/2026', { icon: 'event', trail: 'document_scanner', cls: 'focus', support: 'Faltam 24 dias · ler por imagem disponível numa versão futura' })}
      ${field('Lote do fornecedor', 'L26-2871', { icon: 'tag' })}
      <div class="card outlined" style="padding:10px 12px">
        <div class="row sb"><span class="small muted">Já existe um lote igual nesta receção?</span>${tag('Não', 'neu')}</div>
        <div class="xs muted" style="margin-top:4px">Linhas com o mesmo produto, marca e validade são agrupadas no mesmo lote (RN-01).</div>
      </div>
    </div>
    <div class="bottombar">${btn('Anterior', 'outlined')}${btn('Controlo de receção', 'filled', 'arrow_forward')}</div>`) },

  { id: 'M08', grupo: 'Receção', titulo: 'Linha de produto – controlo de receção (RGDHSA049)', html: phone(`
    ${appbar({ title: 'Controlo de receção', sub: 'Leite meio-gordo Agros 35 cl · 30 UN', lead: 'arrow_back' })}
    <div class="progress"><div style="width:85%"></div></div>
    <div class="content" style="padding-top:12px">
      <div class="card outlined" style="padding:4px 12px">
        ${[['Condições de higiene', true], ['Rotulagem / data de validade', true], ['Características organoléticas', true], ['Embalagem íntegra', false]].map(([t, ok]) =>
          `<div class="row sb" style="height:50px;border-bottom:1px solid #e3e9e5"><span class="small b">${t}</span>${cnc(ok)}</div>`).join('')}
        <div class="row sb" style="height:50px"><span class="small b">Temperatura (ºC)</span><span class="field sm" style="width:90px;height:38px"><span class="val">5,5</span></span></div>
      </div>
      <div class="card error row" style="gap:10px;align-items:flex-start">${ic('report')}<div class="grow"><div class="title-s">Linha não conforme</div><div class="small">Indique o motivo e se o produto é aproveitável.</div></div></div>
      ${field('Motivo / observações *', '2 embalagens amolgadas, sem perda de produto', { cls: 'focus ta' })}
      <div class="label">O produto é aproveitável?</div>
      <div class="row" style="gap:18px"><span class="row" style="gap:6px"><span class="radio on"></span>Sim, aceitar com observação</span></div>
      <div class="row" style="gap:6px"><span class="radio"></span>Não, rejeitar (desperdício na receção)</div>
    </div>
    <div class="bottombar">${btn('Anterior', 'outlined')}${btn('Guardar linha', 'filled', 'check')}</div>`) },

  { id: 'M09', grupo: 'Receção', titulo: 'Resumo e confirmação da receção', html: phone(`
    ${appbar({ title: 'Resumo da receção', sub: 'Passo 3 de 3 · 2026-0153', lead: 'arrow_back' })}
    <div class="progress"><div style="width:100%"></div></div>
    <div class="content" style="padding-top:12px">
      <div class="card filled small" style="padding:10px 12px">
        <div class="row sb"><span class="muted">Doador</span><span class="b">Pingo Doce – Barcelos</span></div>
        <div class="row sb" style="margin-top:4px"><span class="muted">Guia</span><span class="b">DPM1/4101774379</span></div>
        <div class="row sb" style="margin-top:4px"><span class="muted">Responsável</span><span class="b">Ana Costa</span></div>
      </div>
      <div class="row sb"><div class="section">Linhas (5)</div><span class="btn text">${ic('add')}Adicionar</span></div>
      <div class="card elev" style="padding:0"><div class="list">
        ${li({ lead: 'eco', leadCls: 'sq', h: 'Alface frisada PD', s: '1,324 kg · val. 25/10/2026', trail: tag('C', 'ok') })}
        ${li({ lead: 'nutrition', leadCls: 'sq', h: 'Maçã Gala saco 1,5 kg', s: '3 UN · val. 05/11/2026', trail: tag('C', 'ok') })}
        ${li({ lead: 'water_full', leadCls: 'sq', h: 'Leite meio-gordo Agros 35 cl', s: '1 palete = 30 UN · val. 15/11/2026', trail: tag('NC aceite', 'warn') })}
        ${li({ lead: 'egg', leadCls: 'sq', h: 'Iogurte natural PD ×4', s: '6 UN · val. 24/10/2026', trail: tag('C', 'ok') })}
        ${li({ lead: 'block', leadCls: 'sq err', h: 'Fiambre perna fatiado 200 g', s: '2 UN · embalagem violada', trail: tag('Rejeitada', 'err') })}
      </div></div>
      <div class="card primary small row" style="gap:10px">${ic('inventory_2')}<div>Serão criados <b>4 lotes</b> e registado <b>1 desperdício na receção</b>. Os dados alimentam automaticamente o RGDHSA049.</div></div>
    </div>
    <div class="bottombar">${btn('Confirmar receção', 'filled', 'done_all', 'lg')}</div>`) },

  // ---------------------------------------------------------------- Arrumação
  { id: 'M10', grupo: 'Arrumação', titulo: 'Lotes por arrumar', html: phone(`
    ${appbar({ title: 'Por arrumar', sub: '4 lotes · receção 2026-0153', lead: 'arrow_back' })}
    <div class="content np">
      <div class="card ok row" style="margin:6px 16px 10px;gap:10px">${ic('check_circle', 'fill')}<div class="small"><b>Receção registada.</b> Arrume os lotes seguindo as sugestões de localização.</div></div>
      <div class="list">
        ${li({ lead: 'ac_unit', leadCls: 'sq', h: 'Iogurte natural PD ×4 · 6 UN', s: 'Refrigerado · val. 24/10 · sugerido FRIG1-C1', trail: tag('2 dias', 'warn') })}
        ${li({ lead: 'eco', leadCls: 'sq', h: 'Alface frisada PD · 1,324 kg', s: 'Refrigerado · sugerido FRIG1-D2', trail: tag('3 dias', 'warn') })}
        ${li({ lead: 'water_full', leadCls: 'sq', h: 'Leite meio-gordo Agros · 30 UN', s: 'Ambiente · sugerido 004-01-02', trail: '' })}
        ${li({ lead: 'nutrition', leadCls: 'sq', h: 'Maçã Gala saco 1,5 kg · 3 UN', s: 'Ambiente · sugerido 001-03-01', trail: '' })}
      </div>
      <div class="small muted" style="padding:12px 16px">Os lotes refrigerados e com validade mais curta aparecem primeiro.</div>
    </div>
    ${bnav('Receção')}`) },

  { id: 'M11', grupo: 'Arrumação', titulo: 'Sugestão de localização', html: phone(`
    ${appbar({ title: 'Arrumar lote', sub: 'Leite meio-gordo Agros 35 cl · 30 UN', lead: 'arrow_back' })}
    <div class="content" style="padding-top:10px">
      <div class="card primary center" style="padding:18px 14px">
        <div class="label" style="color:var(--on-primary-container)">LOCAL SUGERIDO</div>
        <div class="display mono" style="margin:6px 0 2px">004-01-02</div>
        <div class="small">Coluna 004 · Linha 01 · Andar 02</div>
      </div>
      <div class="card outlined small col" style="gap:6px">
        <div class="row" style="gap:8px">${ic('info', 's20')}<span><b>Porquê aqui?</b> Já contém Leite meio-gordo (2 lotes).</span></div>
        <div class="row" style="gap:8px">${ic('shelves', 's20')}<span>Ocupação: 2 produtos · não assinalada como cheia</span></div>
      </div>
      <div class="label">Alternativas mais próximas</div>
      <div class="row wrap" style="gap:6px">${chip('004-01-03')}${chip('004-02-01')}${chip('003-03-02')}</div>
      <div class="spacer"></div>
      ${btn('Ler QR do local', 'filled', 'qr_code_scanner', 'block lg')}
      <div class="row">${btn('Local cheio', 'outlined', 'block', 'grow')}${btn('Escolher outro', 'outlined', 'list', 'grow')}</div>
    </div>`) },

  { id: 'M12', grupo: 'Arrumação', titulo: 'Leitura do QR do local', html: phone(`
    <div class="appbar" style="background:#171d1b;color:#fff"><div class="ib" style="color:#fff">${ic('close')}</div><div class="title"><h1>Ler QR do local</h1><p style="color:#cfd8d4">Aponte para a etiqueta da prateleira</p></div><div class="ib" style="color:#fff">${ic('flashlight_on')}</div></div>
    <div class="camera">
      <div class="viewfinder"><i></i><i></i><i></i><i></i>
        <div class="label-qr">${q.local}<div class="mono" style="font-size:13px;font-weight:700;color:#111">004-01-02</div></div>
        <div class="scanline"></div>
      </div>
    </div>
    <div class="sheet" style="position:relative;border-radius:24px 24px 0 0">
      <div class="handle"></div>
      <div class="row" style="gap:12px">${ic('check_circle', 'fill s32')}<div class="grow"><div class="title-m">004-01-02 · corresponde à sugestão</div><div class="small muted">Leite meio-gordo Agros · 30 UN</div></div></div>
      ${btn('Confirmar arrumação', 'filled', 'done', 'block lg')}
    </div>`, { dark: true }) },

  // ---------------------------------------------------------------- Stock e validades
  { id: 'M13', grupo: 'Stock e validades', titulo: 'Consulta de stock', html: phone(`
    ${appbar({ title: 'Stock', lead: '', actions: ['qr_code_scanner', 'filter_list'] })}
    <div class="content np">
      <div style="padding:0 16px 10px"><div class="search">${ic('search')}<span class="ph grow">Pesquisar produto, marca ou local</span></div></div>
      <div class="row" style="padding:0 16px 8px;gap:6px;overflow:hidden">${chip('Alimentares', true)}${chip('Higiene')}${chip('Vestuário')}${chip('Limpeza')}</div>
      <div class="list">
        ${li({ lead: 'grain', leadCls: 'sq', h: 'Arroz agulha 1 kg', s: '3 lotes · próx. validade 02/12/2026', trail: '<div class="b" style="color:var(--on-surface);font-size:14px">58 UN</div>' })}
        ${li({ lead: 'egg', leadCls: 'sq', h: 'Iogurte natural', s: '2 lotes · próx. validade 24/10/2026', trail: '<div class="b" style="color:var(--on-surface);font-size:14px">10 UN</div>' + tag('2 dias', 'warn') })}
        ${li({ lead: 'water_full', leadCls: 'sq', h: 'Leite meio-gordo', s: '4 lotes · 3 marcas', trail: '<div class="b" style="color:var(--on-surface);font-size:14px">18 UN</div>' + tag('mín. 40', 'err') })}
        ${li({ lead: 'agriculture', leadCls: 'sq', h: 'Batata branca', s: '1 lote · 1 volume', trail: '<div class="b" style="color:var(--on-surface);font-size:14px">40 kg</div>' })}
        ${li({ lead: 'set_meal', leadCls: 'sq', h: 'Frango inteiro congelado', s: '2 lotes · ARCA1', trail: '<div class="b" style="color:var(--on-surface);font-size:14px">7 UN</div>' + tag('congelado', 'info') })}
        ${li({ lead: 'restaurant', leadCls: 'sq', h: 'Massa esparguete 500 g', s: '5 lotes', trail: '<div class="b" style="color:var(--on-surface);font-size:14px">112 UN</div>' })}
      </div>
    </div>
    ${bnav('Stock')}`) },

  { id: 'M14', grupo: 'Stock e validades', titulo: 'Detalhe do produto e lotes (FEFO)', html: phone(`
    ${appbar({ title: 'Iogurte natural', sub: 'Lacticínios · refrigerado · não congelável', lead: 'arrow_back', actions: ['edit', 'more_vert'] })}
    <div class="content" style="padding-top:6px">
      <div class="row">
        <div class="kpi"><div class="v">10 UN</div><div class="l">Stock disponível</div></div>
        <div class="kpi"><div class="v">12 UN</div><div class="l">Stock mínimo</div></div>
      </div>
      <div class="row sb"><div class="section">Lotes por ordem de saída (FEFO)</div>${ic('sort', 's20 muted')}</div>
      <div class="card outlined" style="padding:10px 12px;border-left:4px solid var(--warn)">
        <div class="row sb"><span class="title-s">1.º · Lote L-0912 · PD ×4</span>${tag('expira em 2 dias', 'warn', 'schedule')}</div>
        <div class="small muted" style="margin-top:3px">Validade 24/10/2026 · 6 UN · FRIG1-C1</div>
        <div class="small muted">Receção 2026-0153 · Pingo Doce · 22/10</div>
        <div class="row" style="margin-top:8px;gap:6px">${btn('Transferir', 'outlined', 'swap_horiz')}${btn('Desperdício', 'outlined', 'delete')}</div>
      </div>
      <div class="card outlined" style="padding:10px 12px">
        <div class="row sb"><span class="title-s">2.º · Lote L-0931 · Danone</span>${tag('disponível', 'ok')}</div>
        <div class="small muted" style="margin-top:3px">Validade 30/10/2026 · 4 UN · FRIG1-C2</div>
        <div class="small muted">Receção 2026-0155 · particular anónimo · 22/10</div>
      </div>
      <div class="card filled small row" style="gap:8px">${ic('history', 's20')}<span>Histórico: 14 entradas e 22 saídas nos últimos 30 dias</span>${ic('chevron_right')}</div>
    </div>
    ${bnav('Stock')}`) },

  { id: 'M15', grupo: 'Stock e validades', titulo: 'Congelar lote', html: phone(`
    ${appbar({ title: 'Peito de frango', sub: 'Carne de aves · congelável', lead: 'arrow_back' })}
    <div class="scrim"></div>
    <div class="sheet">
      <div class="handle"></div>
      <div class="row" style="gap:10px">${ic('ac_unit', 's32')}<div><div class="title-m">Congelar lote L-0877</div><div class="small muted">Disponível: 3,2 kg · validade 23/10/2026</div></div></div>
      <div class="row sb"><span class="title-s">Quantidade a congelar</span>${stepper('3,2 kg')}</div>
      <div class="card primary small" style="padding:10px 12px">
        <div class="row" style="gap:8px">${ic('rule', 's20')}<span><b>Regra da categoria:</b> carne de aves +90 dias</span></div>
      </div>
      ${field('Nova validade proposta', '20/01/2027', { icon: 'event', cls: 'focus', trail: 'edit', support: 'Validade original 23/10/2026 é preservada no histórico' })}
      ${field('Zona de congelação sugerida', 'ARCA1-D2 · Arca 1 (aves)', { icon: 'kitchen', trail: 'qr_code_scanner' })}
      <div class="card warn small row" style="gap:8px">${ic('info', 's20')}<span>Depois de congelado, o lote passa a ser usado depois dos não congelados (FEFO).</span></div>
      <div class="row" style="justify-content:flex-end;gap:8px">${btn('Cancelar', 'text')}${btn('Congelar', 'filled', 'ac_unit')}</div>
    </div>`) },

  { id: 'M16', grupo: 'Stock e validades', titulo: 'Alertas', html: phone(`
    ${appbar({ title: 'Alertas', sub: 'Atualizado hoje às 07:00', lead: 'arrow_back', actions: ['done_all'] })}
    <div class="tabs"><div class="on">Expirados <span class="badge">3</span></div><div>A expirar 8</div><div>Stock mín. 2</div></div>
    <div class="content np">
      <div class="card error small row" style="margin:12px 16px 6px;gap:8px">${ic('warning')}<span>Estes lotes não podem ser entregues. Retire-os e registe o desperdício.</span></div>
      <div class="list">
        ${li({ lead: 'delete_forever', leadCls: 'err', h: 'Fiambre perna fatiado 200 g', s: 'L-0810 · 2 UN · expirou 21/10 · 002-02-01', trail: ic('chevron_right') })}
        ${li({ lead: 'delete_forever', leadCls: 'err', h: 'Pão de forma integral', s: 'L-0822 · 1 UN · expirou 21/10 · 006-01-01', trail: ic('chevron_right') })}
        ${li({ lead: 'delete_forever', leadCls: 'err', h: 'Natas para culinária 200 ml', s: 'L-0791 · 4 UN · expirou 20/10 · FRIG1-E1', trail: ic('chevron_right') })}
      </div>
      <div style="padding:14px 16px">${btn('Registar todos como desperdício', 'tonal', 'delete_sweep', 'block')}</div>
    </div>
    ${bnav('Início')}`) },

  { id: 'M17', grupo: 'Stock e validades', titulo: 'Registar desperdício', html: phone(`
    ${appbar({ title: 'Registar desperdício', lead: 'close' })}
    <div class="content" style="padding-top:8px">
      <div class="card filled" style="padding:10px 12px">
        <div class="title-s">Fiambre perna fatiado 200 g</div>
        <div class="small muted">Lote L-0810 · 002-02-01 · validade 21/10/2026</div>
        <div class="small muted">Disponível: 2 UN</div>
      </div>
      <div class="row sb"><span class="title-s">Quantidade retirada</span>${stepper('2 UN')}</div>
      <div class="label">Motivo</div>
      <div class="card outlined" style="padding:4px 12px">
        <div class="row" style="height:46px;gap:12px"><span class="radio on"></span><div><div class="small b">Expirado</div></div></div>
        <div class="row" style="height:46px;gap:12px"><span class="radio"></span><div class="small b">Danificado</div></div>
        <div class="row" style="height:46px;gap:12px"><span class="radio"></span><div class="small b">Não conforme</div></div>
      </div>
      ${field('Observações', 'Retirado na verificação da manhã', { cls: 'ta' })}
      <div class="small muted">O desperdício é contabilizado em quantidade (UN/kg/L) por produto, categoria e motivo.</div>
      <div class="spacer"></div>
      ${btn('Registar desperdício', 'danger', 'delete', 'block lg')}
    </div>`) },

  // ---------------------------------------------------------------- Utentes
  { id: 'M18', grupo: 'Utentes e agregados', titulo: 'Lista de agregados', html: phone(`
    ${appbar({ title: 'Agregados', lead: 'arrow_back', actions: ['qr_code_scanner'] })}
    <div class="content np">
      <div style="padding:0 16px 10px"><div class="search">${ic('search')}<span class="ph grow">Nome, código ou NIF</span></div></div>
      <div class="row" style="padding:0 16px 8px;gap:6px">${chip('Ativos', true)}${chip('Cabaz')}${chip('Refeições')}${chip('Suspensos')}</div>
      <div class="list">
        ${li({ lead: 'MS', h: 'A-0142 · Maria Silva', s: '4 pessoas · cabaz quinzenal · refeições', trail: tag('Ativo', 'ok') })}
        ${li({ lead: 'JF', h: 'A-0138 · João Ferreira', s: '1 pessoa · refeições', trail: tag('Ativo', 'ok') })}
        ${li({ lead: 'CP', h: 'A-0131 · Carla Pereira', s: '3 pessoas · cabaz mensal', trail: tag('Ativo', 'ok') })}
        ${li({ lead: 'RA', h: 'A-0127 · Rui Almeida', s: '2 pessoas · cabaz semanal', trail: tag('Suspenso', 'warn') })}
        ${li({ lead: 'SM', h: 'A-0119 · Sónia Martins', s: '5 pessoas · cabaz quinzenal · refeições', trail: tag('Ativo', 'ok') })}
        ${li({ lead: 'LG', h: 'A-0102 · Luís Gonçalves', s: '2 pessoas · refeições', trail: tag('Ativo', 'ok') })}
      </div>
    </div>
    <div class="fab">${ic('group_add')}Novo agregado</div>
    ${bnav('Mais')}`) },

  { id: 'M19', grupo: 'Utentes e agregados', titulo: 'Ficha do agregado', html: phone(`
    ${appbar({ title: 'A-0142 · Silva', sub: 'Técnica: Joana Reis · desde 03/2025', lead: 'arrow_back', actions: ['edit', 'more_vert'] })}
    <div class="tabs"><div class="on">Membros</div><div>Dados</div><div>Histórico</div></div>
    <div class="content" style="padding-top:10px">
      <div class="row wrap" style="gap:6px">${tag('Cabaz quinzenal', 'prim', 'shopping_basket')}${tag('Refeições', 'prim', 'restaurant')}${tag('Consentimento 03/2025', 'ok', 'verified_user')}</div>
      <div class="card warn small row" style="gap:8px">${ic('warning')}<span><b>Alergia:</b> glúten (Tiago) · <b>Restrição:</b> sem carne de porco</span></div>
      <div class="card elev" style="padding:0"><div class="list">
        ${li({ lead: 'MS', h: 'Maria Silva <span class="muted small">· titular</span>', s: '41 anos · autorizada a levantar', trail: ic('qr_code_2', 'fill') })}
        ${li({ lead: 'PS', h: 'Paulo Silva <span class="muted small">· cônjuge</span>', s: '44 anos · autorizado a levantar', trail: ic('qr_code_2', 'fill') })}
        ${li({ lead: 'IS', h: 'Inês Silva <span class="muted small">· filha</span>', s: '17 anos · autorizada a levantar', trail: ic('qr_code_2', 'fill') })}
        ${li({ lead: 'TS', h: 'Tiago Silva <span class="muted small">· filho</span>', s: '12 anos · não autorizado · alergia', trail: ic('block') })}
      </div></div>
      <div class="card outlined small" style="padding:10px 12px">
        <div class="row sb"><span class="muted">Próximo cabaz</span><span class="b">29/10/2026 · 10:30</span></div>
        <div class="row sb" style="margin-top:4px"><span class="muted">Último cabaz</span><span class="b">15/10/2026 · 14 artigos</span></div>
        <div class="row sb" style="margin-top:4px"><span class="muted">Refeições esta semana</span><span class="b">2 seg–qui · 3 sex</span></div>
      </div>
      ${btn('Adicionar membro', 'tonal', 'person_add', 'block')}
    </div>`) },

  { id: 'M20', grupo: 'Utentes e agregados', titulo: 'Membro do agregado', html: phone(`
    ${appbar({ title: 'Inês Silva', sub: 'Agregado A-0142', lead: 'arrow_back', actions: ['check'] })}
    <div class="content" style="padding-top:12px;gap:12px">
      ${field('Nome completo *', 'Inês Martins Silva')}
      <div class="row">${field('Data de nascimento', '12/05/2009', { trail: 'event' }).replace('class="field ', 'class="field grow ')}${field('Parentesco', 'Filha', { trail: 'arrow_drop_down' }).replace('class="field ', 'class="field grow ')}</div>
      <div class="row">${field('NIF', '2•• ••• •89').replace('class="field ', 'class="field grow ')}${field('NISS', '1•••••••••3').replace('class="field ', 'class="field grow ')}</div>
      ${field('Restrições alimentares', 'Sem carne de porco')}
      ${field('Alergias', 'Nenhuma', { ph: true })}
      <div class="card outlined" style="padding:10px 12px">
        <div class="row sb"><div><div class="title-s">Autorizada a levantar</div><div class="small muted">Cabazes, outros bens e refeições</div></div><div class="switch on"></div></div>
        <div class="divider" style="margin:10px 0"></div>
        <div class="row sb"><div><div class="title-s">Credencial QR ativa</div><div class="small muted">Emitida 03/03/2025 · suporte: papel</div></div>${btn('Ver', 'text', 'qr_code_2')}</div>
        <div class="divider" style="margin:10px 0"></div>
        <div class="row sb"><div><div class="title-s">Conta na App Utente</div><div class="small muted">Não ativada</div></div>${btn('Ativar', 'text', 'smartphone')}</div>
      </div>
    </div>`) },

  { id: 'M21', grupo: 'Utentes e agregados', titulo: 'Credencial QR', html: phone(`
    ${appbar({ title: 'Credencial QR', sub: 'Inês Silva · A-0142', lead: 'arrow_back', actions: ['more_vert'] })}
    <div class="content" style="padding-top:12px;align-items:center">
      <div class="card elev col" style="width:300px;padding:18px;align-items:center;gap:8px;border-top:6px solid var(--primary)">
        <div class="row" style="gap:6px;color:var(--primary)">${ic('volunteer_activism', 'fill')}<span class="b">GASC · Espaço Social</span></div>
        <div style="width:190px;height:190px">${q.pessoa}</div>
        <div class="title-m">Inês Silva</div>
        <div class="small muted">Agregado A-0142 · autorizada a levantar</div>
        <div class="xs muted mono">Emitida 03/03/2025</div>
      </div>
      <div class="small muted center" style="padding:0 12px">O código contém apenas um identificador aleatório, sem dados pessoais (RN-17).</div>
      <div class="col" style="width:100%">
        ${btn('Imprimir cartão', 'filled', 'print', 'block')}
        ${btn('Enviar para a App Utente', 'tonal', 'send_to_mobile', 'block')}
        ${btn('Revogar e emitir nova', 'outlined', 'autorenew', 'block')}
      </div>
    </div>`) },
];

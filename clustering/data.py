function_words = {u'a', u'algo', u'alguien', u'alguna', u'algunas', u'algunos',
        u'ambos', u'aquel', u'aquella', u'aquellas', u'aquellos', u'aunque',
        u'cada', u'como', u'con', u'cosa', u'cual', u'cuales', u'cualquier',
        u'cualquiera', u'cuando', u'cuanta', u'cuantas', u'cuanto', u'cuantos',
        u'de', u'donde', u'dos', u'el', u'ella', u'ellas', u'ello', u'ellos',
        u'en', u'esa', u'esas', u'ese', u'esos', u'esta', u'estas', u'este',
        u'estos', u'hasta', u'la', u'las', u'le', u'les', u'lo', u'los', u'me',
        u'mi', u'mia', u'mias', u'mio', u'mios', u'mis', u'nadie', u'nos',
        u'nosotras', u'nosotros', u'o', u'para', u'pero', u'por', u'porque',
        u'pues', u'puesto', u'que', u'quien', u'quienes', u'se', u'sin',
        u'sobre', u'solamente', u'su', u'sus', u'suyo', u'tambien', u'te',
        u'ti', u'todas', u'todo', u'todos', u'tu', u'tus', u'tuyo', u'un',
        u'una', u'unas', u'uno', u'unos', u'usted', u'ustedes', u'y', u'yo',
        u'es', u'ya', u'al', u'del', u'hay', u'esto', u'van', u'alla', u'voy',
        u'son', u'hace', u'xq', u'ser', u'ni', u'va', u'han', u'ha', u'mas',
        u'gracias', u'hoy', u'asi', u'q', u'd'}

exlcuded_words = {u'argentina', u'argentinadecide', u'balotaje', u'balotaje2015', u'elecciones', u'elecciones2015',
        u'eleccionesargentina', u'decision2015', u'ballotage', u'ballotage2015', u'ballotaje2015',}

excluded = function_words | exlcuded_words

hs_m = {'cambiemosconmacri',
 'ganamacri',
 'ganamacrisenores',
 'ganomacri',
 'hoymacripresidente',
 'hoyvoteamacri',
 'hoyvotemacri',
 'hoyvotomacri',
 'humormacrista',
 'macri',
 'macriesnuestropresidente',
 'macrijump',
 'macrip',
 'macripresi2015',
 'macripresiden',
 'macripresidente',
 'macripresidente2015',
 'macripresidentr',
 'macripte',
 'macrismo',
 'mananavotomacri',
 'mauriciomacri',
 'mauriciomacripresidente',
 'mejormacri',
 'orientalesdeluruguayconmacri',
 'quieroquebailemacri',
 'todosconmacri',
 'tusderechosomacri',
 'vamosmacri',
 'venezuelaapoyaamacri',
 'vivamacri',
 'voteamacri',
 'votomacri',
 'vzlagritamacripresidente',
 'yaganomacri',
 'yavoteamacri',
 'yavotemacri',
 'yovoteamacri',
 'yovotemacri',
 'yovotoamacri',
 'chauscioli',
 'chupalascioli',
 'sciolicagon',
 'lilita',
 'pelotudak',
 'adioscristina',
 'adiosyegua',
 'airesdecambio',
 'cambiamos',
 'cambiamosnomas',
 'cambiar',
 'cambiemos',
 'cambiemostucaratambien',
 'cambimos',
 'cambio',
 'chaocristina',
 'chaualacadenanaciol',
 'chaubobo',
 'chaucfk',
 'chaucris',
 'chaucristina',
 'chaukretina',
 'elcambio',
 'elcambioqueune',
 'esecambiosisisi',
 'hoycambiamos',
 'hoycambiemos',
 'kretina',
 'mauri',
 'mauriciopresidente',
 'mauriciopresidentedetodoslosargentinos',
 'michetti',
 'michettivicepresidente',
 'mm',
 'mm2015',
 'mmas',
 'vamosmm',
 'vamosporelcambio',
 'yocambie',
 'yocambio',
 'yolovoteamm',
 'yolovotoamm',
 'yolovotomm',
 'yovambio',
 'yovotealcambio',
 'yovoteamm',
 'yovoteelcambio',
 'yovotoelcambio',
 'yovotomm',
 'ysevalayeguakk',}

hs_s = {'aguantescioli',
 'aguntesciolii',
 'ahorascioli',
 'bunkerscioli',
 'danielscioli',
 'danielsciolipresidente',
 'ganascioli',
 'ganoscioli',
 'mejorscioli',
 'mejorsciolipresidente',
 'queganescioli',
 'scioli',
 'scioli2015',
 'sciolipresidente',
 'sciolivencio',
 'vamosscioli',
 'yovoteascioli',
 'yovotescioli',
 'yovotoascioli',
 'yovotodanielscioli',
 'macrijamas',
 'macrimitomano',
 'macrino',
 'macriputo',
 'cristina',
 'cristinafernandez',
 'esecambiono',
 'esecambiononono',
 'kfk',
 'kirchner',
 'kirchnerismo',
 'kirchnerista',
 'kristinakirchner',
 'nocambiemoscrezcamos',
 'nocambiofuturo',
 'vamosdaniel',
 'votofpv',}


hs_o = {'0memoria',
 '20d',
 '22n',
 '22n2015',
 '22nov',
 '2davuelta',
 '2doensayoparalavictoria',
 '360camera',
 '6d',
 '6veces',
 '8n',
 '90s',
 '_',
 'abajoelsocialismo',
 'abrahammateotkm',
 'abrazamehastaquevuelvacristina',
 'acro',
 'acrobacia',
 'acta',
 'actualidad',
 'adelanto',
 'adeliamaria',
 'afip',
 'afp',
 'agentinadecide',
 'ahora',
 'ahorrosapiensactivado',
 'aire',
 'alak',
 'albertofernandez',
 'algonuevo',
 'almagro',
 'alpha',
 'altascumbres',
 'amaicha',
 'amas',
 'amas1d',
 'amealpergolini2015',
 'amealpresidente',
 'america',
 'americalatina',
 'americanoticias',
 'ampliamos',
 'anccomcubre',
 'andaluz',
 'anisbourahla',
 'ansiedad',
 'ansiosa',
 'araguadescargasualegria',
 'arcangelalvarado',
 'arentina',
 'areyouready',
 'arg',
 'argentina',
 'argentinacambio',
 'argentinadebate',
 'argentinadecide',
 'argentinadecidio',
 'argentinadesperto',
 'argentinaelecciones',
 'argentinaelige',
 'argentinaelije',
 'argentinamejor',
 'argentinarenace',
 'argentinas',
 'argentinasegundavuelta',
 'argentinasehunde',
 'argentinateamo',
 'argentinavota',
 'argentinavota2015',
 'argentinavotahoy',
 'argentinavoto2015',
 'argentinayaeligio',
 'argentine',
 'argentinian',
 'argentino',
 'argentinos',
 'argetinadecide',
 'asco',
 'ash4president',
 'ashvsevildead',
 'asilascosasgdl',
 'aslndazorolansey',
 'asuncion',
 'atardecer',
 'atencion',
 'atp',
 'australia',
 'austria',
 'avila',
 'avotarporlapaz',
 'ayacucho',
 'azul',
 'bachelet',
 'bahiablanca',
 'bala',
 'ballotage',
 'ballotage2015',
 'ballotaje2015',
 'ballottage',
 'balojate2015',
 'balotage',
 'balotage2015',
 'balotaje',
 'balotaje2015',
 'balotaje2015argentina',
 'balotajeencanaldiez',
 'balotajeenel9',
 'balotajeenndw',
 'balotajemdz',
 'balotajepresidencial',
 'balotajexperfil',
 'balotarg',
 'barcelona',
 'bastante',
 'beach',
 'belgica',
 'beraldipresidente',
 'bertoldi',
 'block',
 'blog',
 'blogging',
 'blueelecciones',
 'boca',
 'bocadeurna',
 'bocasdeurna',
 'bolivia',
 'boludeces',
 'bombonera360',
 'brancatelli',
 'brancatellipelotudo',
 'brasil',
 'brazil',
 'breaking',
 'brusselslockdown',
 'bsas',
 'buenaonda',
 'buendia',
 'buendomingoparatodos',
 'buenosaires',
 'buenosairescaracas',
 'buenosdias',
 'buenviernes',
 'bueyueksok',
 'bunkercambiemos',
 'bunkerfpv',
 'c5n',
 'caba',
 'cadena3elecciones',
 'cafayate',
 'cagamos',
 'callatesabatella',
 'campanasucia',
 'campora',
 'caracas',
 'caradura',
 'caricatura',
 'carometro',
 'carrio',
 'cartuchos',
 'casablanca',
 'casaresvota',
 'casarosada',
 'castro',
 'catamarca',
 'ccchapultepec',
 'cdmxlgbttti',
 'centenario',
 'centrodecomputos',
 'cerraronloscomicios',
 'cfk',
 'cge',
 'chaco',
 'chamuyicidio',
 'chaubrancatelli',
 'chaufito',
 'chaumontonera',
 'chavezwashere',
 'chavista',
 'chetaconchetaconchapodrida',
 'chihuahua',
 'chile',
 'china',
 'chubut',
 'ciencia',
 'ciudad',
 'ciudaddelrio',
 'civilizacion',
 'colombia',
 'coloniacaroya',
 'comicios',
 'computos',
 'comunicacion',
 'comunidadcien',
 'comunismo',
 'conductortv',
 'confiemos',
 'confirmado',
 'conservative',
 'contactofm',
 'contalacomoquieras',
 'contexto',
 'cordoba',
 'corrientes',
 'corrupcion',
 'corruptos',
 'cosasquenose',
 'crack',
 'crise',
 'cristinalohizo',
 'cronogramadepagos',
 'csr8',
 'cuba',
 'cucutenonews',
 'cuidomifuturo',
 'cunadelanoticia',
 'datooficialprovisorio',
 'datos',
 'datosoficiales',
 'dbt10gh16',
 'ddhh',
 'decision2015',
 'decison2015',
 'deluto',
 'democracia',
 'democraciak',
 'derechoshumanos',
 'desicion2015',
 'desperdiciasteeldomimgo',
 'despiertaamerica',
 'deudapublica',
 'diadelmusico',
 'diahistorico',
 'dilma',
 'directv',
 'disease',
 'djokovic',
 'doctor',
 'doesn',
 'domingo',
 'domingodega',
 'domingodeganarseguidores',
 'domingodevictoria',
 'ds',
 'duranbarba',
 'e2015',
 'eadt',
 'ecuador',
 'edlp',
 'el22pornisman',
 'el6dganachavez',
 'el6dsevotaxlamanito',
 'elbordo',
 'ele',
 'eleccio',
 'eleccion',
 'eleccion2015',
 'eleccionargentina',
 'elecciones',
 'elecciones2015',
 'eleccionesarg',
 'eleccionesargentina',
 'eleccionesenbrisas',
 'eleccionesmitre',
 'eleccionespresidenciales',
 'eleccionesrockandpop',
 'eleccionpresidenteargentina',
 'eleciones',
 'eleciones2015',
 'elections',
 'elegistelt3',
 'elgrafico',
 'eligepresidente',
 'eligio',
 'elijoradiosur',
 'elpaiselige',
 'elpaisestaconvos',
 'elpaisvota',
 'elproyecto',
 'elpuebloalacalle',
 'elquesecansapierde',
 'eltiempodediosesperfecto',
 'eltrece',
 'eltresenvivo',
 'encuesta',
 'encuestatwittera',
 'endirecto',
 'ensenada',
 'entreguenlaplaza',
 'envideo',
 'envivo',
 'erotic',
 'escrutado',
 'escrutinio',
 'escuchalaciudad',
 'escuela7',
 'escuelaindustrial',
 'escuelajulioverne',
 'escuelanormal',
 'esefalsono',
 'espana',
 'espanaenserio',
 'esperando',
 'estamosfelices',
 'estoyesperanzado',
 'estudiopoliticoespecial',
 'etique',
 'evo',
 'exclusiva',
 'falklands',
 'faltadeeducacion',
 'fayt',
 'fe',
 'federer',
 'feedback',
 'felices',
 'felicidad',
 'felicidadplena',
 'feliz',
 'felizdia',
 'felizdiadelamusica',
 'felizdomingo',
 'felizsabado',
 'festejando',
 'ff',
 'fin',
 'final',
 'findeciclo',
 'firmat',
 'fiscales',
 'fiscalescambiemos',
 'fiscalesheroes',
 'fmrielurgente',
 'fondomonetariointernacional',
 'fonds',
 'forapt',
 'foraptcomunista',
 'formamosunpartidoyganamos',
 'fpv',
 'fraude',
 'fraudeelectoral',
 'frenteparalavictoria',
 'friends',
 'fuerakukarachas',
 'fuerza',
 'fuerzafiscales',
 'fuerzayfe',
 'fuiste',
 'futbol',
 'futuro',
 'gabrielamichettivicepresidente',
 'gallardopresidente',
 'gamba',
 'gana',
 'ganaargentina',
 'ganamauricio',
 'ganamossss',
 'gano',
 'ganoclarin',
 'ganoeeuu',
 'ganoelbuitre',
 'ganoelcuco',
 'ganoelfmi',
 'ganoladerecha',
 'ganomauri',
 'gay',
 'gelp',
 'geniosdelvoto',
 'gessell2016',
 'global',
 'golpe',
 'googledoodle',
 'gracias',
 'graciasadios',
 'graciascarrio',
 'graciasdios',
 'graciaslilita',
 'graciasmauricio',
 'graciasnisman',
 'graciasraul',
 'graciastotales',
 'guardianesdelvoto',
 'habemuspresidente',
 'hamponatonarcocomunista',
 'hashtag',
 'haybalotaje',
 'haydisoeyle',
 'hearties',
 'helicoptero',
 'hermanosargentinos',
 'hijosnuestros',
 'historia',
 'holanda',
 'hoy',
 'hoyelpaiscambia',
 'hoyquesale',
 'hurlingham',
 'ibae',
 'idiotas',
 'ignora',
 'igualdad',
 'ilusionnaranja',
 'impeachmentdilma',
 'impresoras',
 'independiente',
 'innovacion',
 'instagram',
 'insumos',
 'italia',
 'izquierda',
 'jaen',
 'janice',
 'japon',
 'jesus',
 'jesusdixit',
 'journalisme',
 'juanmartindelpotro',
 'jujuy',
 'julianaawada',
 'julioalak',
 'justicia',
 'justiciaelectoral',
 'justiciaxnisman',
 'justjack',
 'k',
 'kapanga',
 'ksmetolursa',
 'kuerdistandireniyor',
 'la',
 'lacampora',
 'ladrones',
 'lajornadaweb',
 'lamatanza',
 'lanatasinfiltro',
 'lapampa',
 'laplata',
 'laplataelige',
 'las',
 'lasmalvinassonargentinas',
 'lasproximassonnuestras',
 'latam',
 'latecno',
 'latenesadentro',
 'latinoamerica',
 'launidadesvictoria',
 'lavidamisma',
 'lebanon',
 'lgbttti',
 'liberenlospresospoliticos',
 'libertad',
 'ligaaguilarcn',
 'ligaaguilaxwin',
 'lilitaeslamadredelarepublica',
 'lilitaprocuradora',
 'listamillonaria',
 'lloramas',
 'lodije',
 'londres',
 'losgafosdelsur',
 'loshornillos',
 'lossimpsons',
 'loultimo',
 'lta',
 'lulanacadeia',
 'lumix',
 'maciel',
 'madrid',
 'madryn',
 'maduro',
 'madurorenunciaya',
 'malabrigo',
 'malik',
 'mamm',
 'maracay',
 'marchiquita',
 'marcosjuarez',
 'mardelplatavota',
 'mari',
 'marioferreiro',
 'marketing',
 'mascherano',
 'mataronalperiodismo',
 'mdlve',
 'medellin',
 'megamineria',
 'memes',
 'memoria',
 'mendoza',
 'mesaza',
 'metropolis',
 'midiaelectoral',
 'miedo',
 'milagro',
 'militopresidente',
 'milsuperheroes',
 'min',
 'minuevopresidente',
 'minutoamin',
 'minutoaminuto',
 'misiones',
 'modos',
 'momentoreflexivo',
 'movil',
 'mtvstars',
 'mundo',
 'musica_para_mis_oidos',
 'musicmonday',
 'n22',
 'nadakeve',
 'narcoregimen',
 'navarroelige',
 'neededthisgif',
 'nervios',
 'nesquik',
 'nesquikargentina',
 'nestor',
 'neuquen',
 'neuquencapital',
 'news',
 'nikpelotudo',
 'niolvidoniperdon',
 'nisman',
 'niunderechomenos',
 'niunkmas',
 'niunvillanoenargentina',
 'no',
 'noalnarcopopulismodelsigloxxi',
 'noaprendemos',
 'nofuemagia',
 'nolloresporcristinaargentina',
 'nomassocialismosxxi',
 'nonoscagues',
 'nonosdefraudes',
 'notenesnadaenlacabezanene',
 'noticia',
 'noticias',
 'noticiasjalisco',
 'nuevazelanda',
 'nuevopresidente',
 'obamadevuelvelacocaya',
 'objetivoribera',
 'objetivorivera',
 'obvioamor',
 'oea',
 'ojoconelvoto',
 'ojoelcorreo',
 'olavarriavota',
 'olivos',
 'omg',
 'onu',
 'onur',
 'op',
 'operativoelecciones',
 'paisdepelotudos',
 'pak',
 'panqueques',
 'parabajaralaclasealta',
 'paraguay',
 'paraquecrezcalaproduccionnacional',
 'paraqueelpaistengafuturo',
 'paraquelosdesempleadosnomuerandehambre',
 'paraquelospobressubanaclasemedia',
 'paraquesesigacreandotrabajo',
 'paraqueunprocesadonogobierneunpais',
 'paraseguirestatizandoempresasprivadas',
 'paraunpaisdeizquierda',
 'paro',
 'partidopopular',
 'pateticos',
 'paz',
 'pendientes',
 'perdimostodos',
 'periodismomilitante',
 'periscope',
 'peru',
 'photo',
 'pibes',
 'pinera',
 'plazita',
 'poder',
 'poetuit',
 'poetuitazo',
 'politica',
 'politicos',
 'polonia',
 'poncela',
 'populism',
 'populismo',
 'porahora',
 'porecuador',
 'porfavor',
 'porquenoquierovolveral2001',
 'porunpaismejor',
 'porvenezuela',
 'posible',
 'ppt',
 'precarizado',
 'prediccioncumplida',
 'presidencia',
 'president',
 'presidente',
 'presidente2015',
 'presidenteargentino',
 'presospoliticos',
 'pri',
 'price',
 'primerasmesas',
 'primeros',
 'primerosdatos',
 'primerosdatosoficiales',
 'primerosresultados',
 'pro',
 'problemas',
 'procesado',
 'prohibidoolvidar',
 'property',
 'psuv',
 'puebloactivo',
 'puerto',
 'puertoiguazu',
 'puertorico',
 'pulxoelectoral',
 'quedistintossomos',
 'queganeargentina',
 'queremosdatos',
 'queriamoscambiar',
 'quevuelvael',
 'quilmes',
 'radiomitre',
 'rainbowrowell',
 'rating',
 'rd',
 'realestate',
 'realtor',
 'reconciliacion',
 'reconquista',
 'redsocial',
 'regresaseguroacasa',
 'reinounido',
 'reiteramos',
 'relajemos',
 'report',
 'repost',
 'republica',
 'resistencia',
 'resistiendoconaguante',
 'resultado',
 'resultados',
 'resultadosensantafe',
 'resultadosoficiales',
 'resultadostuvoto',
 'results',
 'retrocedernunca',
 'rightnowh',
 'rio3',
 'riocuarto',
 'riotercero',
 'robertonavarro',
 'rocamora',
 'rockearadio',
 'rolo',
 'romero',
 'rosario',
 'rt',
 'salta',
 'saluddemocracia',
 'salvatuvoto',
 'sanpedro',
 'santafe',
 'santiago',
 'santostraidor',
 'sanz',
 'sciolo',
 'scoli',
 'sde',
 'seguime',
 'seguimeytesigo',
 'seguimeytesigoya',
 'segundavuelta',
 'selesacabalateta',
 'seo',
 'serfiscal',
 'sesacaba',
 'sesiente',
 'seterminoelrelatok',
 'sevanacagardehambre',
 'sevanlosk',
 'sevieneuncambio',
 'showdown',
 'siguemeytesigo',
 'sihayfuturo',
 'sinamor',
 'sinovotasvotanporti',
 'sisepuede',
 'socialismo',
 'socialismosigloxxi',
 'socialismoxxi',
 'socorro',
 'sohappy',
 'somosbalotaje',
 'sosvenezuela',
 'soyfiscal',
 'sps',
 'srpresidente',
 'sub20femenino',
 'sudau14enc2015',
 'suecia',
 'sunchalescambia',
 'suramerica',
 'tafiviejo',
 'talcual',
 'tandil',
 'telefenoticias',
 'telefono',
 'telegrama',
 'telenueveespecial',
 'telesur',
 'temblor',
 'tenis',
 'tercero',
 'thearkoftwitter',
 'themountie',
 'tibi',
 'tina',
 'tn',
 'tnxde',
 'to2argentina',
 'todosjuntosestamos',
 'todosunamentira',
 'todotienesufinal',
 'todounejemplo',
 'toleranciacero',
 'toner',
 'tormenta',
 'transgenicos',
 'travel',
 'triste',
 'tristesah',
 'trndnl',
 'tropaarg',
 'ttv',
 'tucuman',
 'tucumanelige',
 'turquia',
 'tv',
 'ultimahora',
 'ultimas',
 'ultimo_minuto',
 'ultimominuto',
 'ultimomomento',
 'unalatinoamericademocratica',
 'unamordidita',
 'unasur',
 'unidad',
 'unitedstates',
 'update',
 'urgente',
 'uribistas',
 'uruguay',
 'us',
 'usa',
 'ushuaia',
 'vaaestarbuenaargentina',
 'value',
 'vamos',
 'vamosargentina',
 'vamosjuntos',
 'vamoslospibes',
 'vamosquesepuede',
 'vautours',
 'vedaelectoral',
 'velorio',
 'venezolano',
 'venezuela',
 'venezuelagana',
 'venezuelaquierecambio',
 'venezuelaquierevivirmejor',
 'vera',
 'verguenza',
 'vgg',
 'vicentelopez',
 'viedma',
 'villamaria',
 'villanueva',
 'vision7',
 'viva',
 'vivaargentinalibre',
 'vivaasignacionuniversalporhijo',
 'vivalaclasemedia',
 'vivalademocracia',
 'viviendolahistoria',
 'votaporlamanito',
 'votasinmiedo',
 'votemosaunbostero',
 'voto',
 'voto2015',
 'votoafavor',
 'votodelcampo',
 'votoenblanco',
 'votoexterior',
 'votoobligatorio',
 'votoporandino',
 'votoporcronica',
 'votos',
 'votoycalle',
 'vrjournalism',
 'vzla',
 'vzlaprohibidoolvidar',
 'waiting',
 'web',
 'whatsapp',
 'whatsisthis',
 'wow',
 'wtf',
 'xunaargentinamejor',
 'yacambiamos',
 'yacambiaron',
 'yahaynuevopresidente',
 'yerbabuena',
 'yoelijoxmifuturo',
 'yofiscalizo',
 'yoli',
 'yolo',
 'yolovivi',
 'yolovoto',
 'yonolovote',
 'yonotraiciono',
 'yosobrevivialkirchnerismo',
 'yotodavianovoto',
 'your',
 'yovote',
 'yovotealpresidente',
 'yovoteamitre',
 'yovoto',
 'yovotoenenblanco',
 'yovotoloquecreo',
 'yperdioigual',
 'zanini',
 'zocalo',
 'macriscioli',}




#### ALL HASHTAGS


hashtags = {'0memoria',
 '20d',
 '22n',
 '22n2015',
 '22nov',
 '2davuelta',
 '2doensayoparalavictoria',
 '360camera',
 '6d',
 '6veces',
 '8n',
 '90s',
 '_',
 'abajoelsocialismo',
 'abrahammateotkm',
 'abrazamehastaquevuelvacristina',
 'acro',
 'acrobacia',
 'acta',
 'actualidad',
 'adelanto',
 'adeliamaria',
 'adioscristina',
 'adiosyegua',
 'afip',
 'afp',
 'agentinadecide',
 'aguantescioli',
 'aguntesciolii',
 'ahora',
 'ahorascioli',
 'ahorrosapiensactivado',
 'aire',
 'airesdecambio',
 'alak',
 'albertofernandez',
 'algonuevo',
 'almagro',
 'alpha',
 'altascumbres',
 'amaicha',
 'amas',
 'amas1d',
 'amealpergolini2015',
 'amealpresidente',
 'america',
 'americalatina',
 'americanoticias',
 'ampliamos',
 'anccomcubre',
 'andaluz',
 'anisbourahla',
 'ansiedad',
 'ansiosa',
 'araguadescargasualegria',
 'arcangelalvarado',
 'arentina',
 'areyouready',
 'arg',
 'argentina',
 'argentinacambio',
 'argentinadebate',
 'argentinadecide',
 'argentinadecidio',
 'argentinadesperto',
 'argentinaelecciones',
 'argentinaelige',
 'argentinaelije',
 'argentinamejor',
 'argentinarenace',
 'argentinas',
 'argentinasegundavuelta',
 'argentinasehunde',
 'argentinateamo',
 'argentinavota',
 'argentinavota2015',
 'argentinavotahoy',
 'argentinavoto2015',
 'argentinayaeligio',
 'argentine',
 'argentinian',
 'argentino',
 'argentinos',
 'argetinadecide',
 'asco',
 'ash4president',
 'ashvsevildead',
 'asilascosasgdl',
 'aslndazorolansey',
 'asuncion',
 'atardecer',
 'atencion',
 'atp',
 'australia',
 'austria',
 'avila',
 'avotarporlapaz',
 'ayacucho',
 'azul',
 'bachelet',
 'bahiablanca',
 'bala',
 'ballotage',
 'ballotage2015',
 'ballotaje2015',
 'ballottage',
 'balojate2015',
 'balotage',
 'balotage2015',
 'balotaje',
 'balotaje2015',
 'balotaje2015argentina',
 'balotajeencanaldiez',
 'balotajeenel9',
 'balotajeenndw',
 'balotajemdz',
 'balotajepresidencial',
 'balotajexperfil',
 'balotarg',
 'barcelona',
 'bastante',
 'beach',
 'belgica',
 'beraldipresidente',
 'bertoldi',
 'block',
 'blog',
 'blogging',
 'blueelecciones',
 'boca',
 'bocadeurna',
 'bocasdeurna',
 'bolivia',
 'boludeces',
 'bombonera360',
 'brancatelli',
 'brancatellipelotudo',
 'brasil',
 'brazil',
 'breaking',
 'brusselslockdown',
 'bsas',
 'buenaonda',
 'buendia',
 'buendomingoparatodos',
 'buenosaires',
 'buenosairescaracas',
 'buenosdias',
 'buenviernes',
 'bueyueksok',
 'bunkercambiemos',
 'bunkerfpv',
 'bunkerscioli',
 'c5n',
 'caba',
 'cadena3elecciones',
 'cafayate',
 'cagamos',
 'callatesabatella',
 'cambiamos',
 'cambiamosnomas',
 'cambiar',
 'cambiemos',
 'cambiemosconmacri',
 'cambiemostucaratambien',
 'cambimos',
 'cambio',
 'campanasucia',
 'campora',
 'caracas',
 'caradura',
 'caricatura',
 'carometro',
 'carrio',
 'cartuchos',
 'casablanca',
 'casaresvota',
 'casarosada',
 'castro',
 'catamarca',
 'ccchapultepec',
 'cdmxlgbttti',
 'centenario',
 'centrodecomputos',
 'cerraronloscomicios',
 'cfk',
 'cge',
 'chaco',
 'chamuyicidio',
 'chaocristina',
 'chaualacadenanaciol',
 'chaubobo',
 'chaubrancatelli',
 'chaucfk',
 'chaucris',
 'chaucristina',
 'chaufito',
 'chaukretina',
 'chaumontonera',
 'chauscioli',
 'chavezwashere',
 'chavista',
 'chetaconchetaconchapodrida',
 'chihuahua',
 'chile',
 'china',
 'chubut',
 'chupalascioli',
 'ciencia',
 'ciudad',
 'ciudaddelrio',
 'civilizacion',
 'colombia',
 'coloniacaroya',
 'comicios',
 'computos',
 'comunicacion',
 'comunidadcien',
 'comunismo',
 'conductortv',
 'confiemos',
 'confirmado',
 'conservative',
 'contactofm',
 'contalacomoquieras',
 'contexto',
 'cordoba',
 'corrientes',
 'corrupcion',
 'corruptos',
 'cosasquenose',
 'crack',
 'crise',
 'cristina',
 'cristinafernandez',
 'cristinalohizo',
 'cronogramadepagos',
 'csr8',
 'cuba',
 'cucutenonews',
 'cuidomifuturo',
 'cunadelanoticia',
 'danielscioli',
 'danielsciolipresidente',
 'datooficialprovisorio',
 'datos',
 'datosoficiales',
 'dbt10gh16',
 'ddhh',
 'decision2015',
 'decison2015',
 'deluto',
 'democracia',
 'democraciak',
 'derechoshumanos',
 'desicion2015',
 'desperdiciasteeldomimgo',
 'despiertaamerica',
 'deudapublica',
 'diadelmusico',
 'diahistorico',
 'dilma',
 'directv',
 'disease',
 'djokovic',
 'doctor',
 'doesn',
 'domingo',
 'domingodega',
 'domingodeganarseguidores',
 'domingodevictoria',
 'ds',
 'duranbarba',
 'e2015',
 'eadt',
 'ecuador',
 'edlp',
 'el22pornisman',
 'el6dganachavez',
 'el6dsevotaxlamanito',
 'elbordo',
 'elcambio',
 'elcambioqueune',
 'ele',
 'eleccio',
 'eleccion',
 'eleccion2015',
 'eleccionargentina',
 'elecciones',
 'elecciones2015',
 'eleccionesarg',
 'eleccionesargentina',
 'eleccionesenbrisas',
 'eleccionesmitre',
 'eleccionespresidenciales',
 'eleccionesrockandpop',
 'eleccionpresidenteargentina',
 'eleciones',
 'eleciones2015',
 'elections',
 'elegistelt3',
 'elgrafico',
 'eligepresidente',
 'eligio',
 'elijoradiosur',
 'elpaiselige',
 'elpaisestaconvos',
 'elpaisvota',
 'elproyecto',
 'elpuebloalacalle',
 'elquesecansapierde',
 'eltiempodediosesperfecto',
 'eltrece',
 'eltresenvivo',
 'encuesta',
 'encuestatwittera',
 'endirecto',
 'ensenada',
 'entreguenlaplaza',
 'envideo',
 'envivo',
 'erotic',
 'escrutado',
 'escrutinio',
 'escuchalaciudad',
 'escuela7',
 'escuelaindustrial',
 'escuelajulioverne',
 'escuelanormal',
 'esecambiono',
 'esecambiononono',
 'esecambiosisisi',
 'esefalsono',
 'espana',
 'espanaenserio',
 'esperando',
 'estamosfelices',
 'estoyesperanzado',
 'estudiopoliticoespecial',
 'etique',
 'evo',
 'exclusiva',
 'falklands',
 'faltadeeducacion',
 'fayt',
 'fe',
 'federer',
 'feedback',
 'felices',
 'felicidad',
 'felicidadplena',
 'feliz',
 'felizdia',
 'felizdiadelamusica',
 'felizdomingo',
 'felizsabado',
 'festejando',
 'ff',
 'fin',
 'final',
 'findeciclo',
 'firmat',
 'fiscales',
 'fiscalescambiemos',
 'fiscalesheroes',
 'fmrielurgente',
 'fondomonetariointernacional',
 'fonds',
 'forapt',
 'foraptcomunista',
 'formamosunpartidoyganamos',
 'fpv',
 'fraude',
 'fraudeelectoral',
 'frenteparalavictoria',
 'friends',
 'fuerakukarachas',
 'fuerza',
 'fuerzafiscales',
 'fuerzayfe',
 'fuiste',
 'futbol',
 'futuro',
 'gabrielamichettivicepresidente',
 'gallardopresidente',
 'gamba',
 'gana',
 'ganaargentina',
 'ganamacri',
 'ganamacrisenores',
 'ganamauricio',
 'ganamossss',
 'ganascioli',
 'gano',
 'ganoclarin',
 'ganoeeuu',
 'ganoelbuitre',
 'ganoelcuco',
 'ganoelfmi',
 'ganoladerecha',
 'ganomacri',
 'ganomauri',
 'ganoscioli',
 'gay',
 'gelp',
 'geniosdelvoto',
 'gessell2016',
 'global',
 'golpe',
 'googledoodle',
 'gracias',
 'graciasadios',
 'graciascarrio',
 'graciasdios',
 'graciaslilita',
 'graciasmauricio',
 'graciasnisman',
 'graciasraul',
 'graciastotales',
 'guardianesdelvoto',
 'habemuspresidente',
 'hamponatonarcocomunista',
 'hashtag',
 'haybalotaje',
 'haydisoeyle',
 'hearties',
 'helicoptero',
 'hermanosargentinos',
 'hijosnuestros',
 'historia',
 'holanda',
 'hoy',
 'hoycambiamos',
 'hoycambiemos',
 'hoyelpaiscambia',
 'hoymacripresidente',
 'hoyquesale',
 'hoyvoteamacri',
 'hoyvotemacri',
 'hoyvotomacri',
 'humormacrista',
 'hurlingham',
 'ibae',
 'idiotas',
 'ignora',
 'igualdad',
 'ilusionnaranja',
 'impeachmentdilma',
 'impresoras',
 'independiente',
 'innovacion',
 'instagram',
 'insumos',
 'italia',
 'izquierda',
 'jaen',
 'janice',
 'japon',
 'jesus',
 'jesusdixit',
 'journalisme',
 'juanmartindelpotro',
 'jujuy',
 'julianaawada',
 'julioalak',
 'justicia',
 'justiciaelectoral',
 'justiciaxnisman',
 'justjack',
 'k',
 'kapanga',
 'kfk',
 'kirchner',
 'kirchnerismo',
 'kirchnerista',
 'kretina',
 'kristinakirchner',
 'ksmetolursa',
 'kuerdistandireniyor',
 'la',
 'lacampora',
 'ladrones',
 'lajornadaweb',
 'lamatanza',
 'lanatasinfiltro',
 'lapampa',
 'laplata',
 'laplataelige',
 'las',
 'lasmalvinassonargentinas',
 'lasproximassonnuestras',
 'latam',
 'latecno',
 'latenesadentro',
 'latinoamerica',
 'launidadesvictoria',
 'lavidamisma',
 'lebanon',
 'lgbttti',
 'liberenlospresospoliticos',
 'libertad',
 'ligaaguilarcn',
 'ligaaguilaxwin',
 'lilita',
 'lilitaeslamadredelarepublica',
 'lilitaprocuradora',
 'listamillonaria',
 'lloramas',
 'lodije',
 'londres',
 'losgafosdelsur',
 'loshornillos',
 'lossimpsons',
 'loultimo',
 'lta',
 'lulanacadeia',
 'lumix',
 'maciel',
 'macri',
 'macriesnuestropresidente',
 'macrijamas',
 'macrijump',
 'macrimitomano',
 'macrino',
 'macrip',
 'macripresi2015',
 'macripresiden',
 'macripresidente',
 'macripresidente2015',
 'macripresidentr',
 'macripte',
 'macriputo',
 'macriscioli',
 'macrismo',
 'madrid',
 'madryn',
 'maduro',
 'madurorenunciaya',
 'malabrigo',
 'malik',
 'mamm',
 'mananavotomacri',
 'maracay',
 'marchiquita',
 'marcosjuarez',
 'mardelplatavota',
 'mari',
 'marioferreiro',
 'marketing',
 'mascherano',
 'mataronalperiodismo',
 'mauri',
 'mauriciomacri',
 'mauriciomacripresidente',
 'mauriciopresidente',
 'mauriciopresidentedetodoslosargentinos',
 'mdlve',
 'medellin',
 'megamineria',
 'mejormacri',
 'mejorscioli',
 'mejorsciolipresidente',
 'memes',
 'memoria',
 'mendoza',
 'mesaza',
 'metropolis',
 'michetti',
 'michettivicepresidente',
 'midiaelectoral',
 'miedo',
 'milagro',
 'militopresidente',
 'milsuperheroes',
 'min',
 'minuevopresidente',
 'minutoamin',
 'minutoaminuto',
 'misiones',
 'mm',
 'mm2015',
 'mmas',
 'modos',
 'momentoreflexivo',
 'movil',
 'mtvstars',
 'mundo',
 'musica_para_mis_oidos',
 'musicmonday',
 'n22',
 'nadakeve',
 'narcoregimen',
 'navarroelige',
 'neededthisgif',
 'nervios',
 'nesquik',
 'nesquikargentina',
 'nestor',
 'neuquen',
 'neuquencapital',
 'news',
 'nikpelotudo',
 'niolvidoniperdon',
 'nisman',
 'niunderechomenos',
 'niunkmas',
 'niunvillanoenargentina',
 'no',
 'noalnarcopopulismodelsigloxxi',
 'noaprendemos',
 'nocambiemoscrezcamos',
 'nocambiofuturo',
 'nofuemagia',
 'nolloresporcristinaargentina',
 'nomassocialismosxxi',
 'nonoscagues',
 'nonosdefraudes',
 'notenesnadaenlacabezanene',
 'noticia',
 'noticias',
 'noticiasjalisco',
 'nuevazelanda',
 'nuevopresidente',
 'obamadevuelvelacocaya',
 'objetivoribera',
 'objetivorivera',
 'obvioamor',
 'oea',
 'ojoconelvoto',
 'ojoelcorreo',
 'olavarriavota',
 'olivos',
 'omg',
 'onu',
 'onur',
 'op',
 'operativoelecciones',
 'orientalesdeluruguayconmacri',
 'paisdepelotudos',
 'pak',
 'panqueques',
 'parabajaralaclasealta',
 'paraguay',
 'paraquecrezcalaproduccionnacional',
 'paraqueelpaistengafuturo',
 'paraquelosdesempleadosnomuerandehambre',
 'paraquelospobressubanaclasemedia',
 'paraquesesigacreandotrabajo',
 'paraqueunprocesadonogobierneunpais',
 'paraseguirestatizandoempresasprivadas',
 'paraunpaisdeizquierda',
 'paro',
 'partidopopular',
 'pateticos',
 'paz',
 'pelotudak',
 'pendientes',
 'perdimostodos',
 'periodismomilitante',
 'periscope',
 'peru',
 'photo',
 'pibes',
 'pinera',
 'plazita',
 'poder',
 'poetuit',
 'poetuitazo',
 'politica',
 'politicos',
 'polonia',
 'poncela',
 'populism',
 'populismo',
 'porahora',
 'porecuador',
 'porfavor',
 'porquenoquierovolveral2001',
 'porunpaismejor',
 'porvenezuela',
 'posible',
 'ppt',
 'precarizado',
 'prediccioncumplida',
 'presidencia',
 'president',
 'presidente',
 'presidente2015',
 'presidenteargentino',
 'presospoliticos',
 'pri',
 'price',
 'primerasmesas',
 'primeros',
 'primerosdatos',
 'primerosdatosoficiales',
 'primerosresultados',
 'pro',
 'problemas',
 'procesado',
 'prohibidoolvidar',
 'property',
 'psuv',
 'puebloactivo',
 'puerto',
 'puertoiguazu',
 'puertorico',
 'pulxoelectoral',
 'quedistintossomos',
 'queganeargentina',
 'queganescioli',
 'queremosdatos',
 'queriamoscambiar',
 'quevuelvael',
 'quieroquebailemacri',
 'quilmes',
 'radiomitre',
 'rainbowrowell',
 'rating',
 'rd',
 'realestate',
 'realtor',
 'reconciliacion',
 'reconquista',
 'redsocial',
 'regresaseguroacasa',
 'reinounido',
 'reiteramos',
 'relajemos',
 'report',
 'repost',
 'republica',
 'resistencia',
 'resistiendoconaguante',
 'resultado',
 'resultados',
 'resultadosensantafe',
 'resultadosoficiales',
 'resultadostuvoto',
 'results',
 'retrocedernunca',
 'rightnowh',
 'rio3',
 'riocuarto',
 'riotercero',
 'robertonavarro',
 'rocamora',
 'rockearadio',
 'rolo',
 'romero',
 'rosario',
 'rt',
 'salta',
 'saluddemocracia',
 'salvatuvoto',
 'sanpedro',
 'santafe',
 'santiago',
 'santostraidor',
 'sanz',
 'scioli',
 'scioli2015',
 'sciolicagon',
 'sciolipresidente',
 'sciolivencio',
 'sciolo',
 'scoli',
 'sde',
 'seguime',
 'seguimeytesigo',
 'seguimeytesigoya',
 'segundavuelta',
 'selesacabalateta',
 'seo',
 'serfiscal',
 'sesacaba',
 'sesiente',
 'seterminoelrelatok',
 'sevanacagardehambre',
 'sevanlosk',
 'sevieneuncambio',
 'showdown',
 'siguemeytesigo',
 'sihayfuturo',
 'sinamor',
 'sinovotasvotanporti',
 'sisepuede',
 'socialismo',
 'socialismosigloxxi',
 'socialismoxxi',
 'socorro',
 'sohappy',
 'somosbalotaje',
 'sosvenezuela',
 'soyfiscal',
 'sps',
 'srpresidente',
 'sub20femenino',
 'sudau14enc2015',
 'suecia',
 'sunchalescambia',
 'suramerica',
 'tafiviejo',
 'talcual',
 'tandil',
 'telefenoticias',
 'telefono',
 'telegrama',
 'telenueveespecial',
 'telesur',
 'temblor',
 'tenis',
 'tercero',
 'thearkoftwitter',
 'themountie',
 'tibi',
 'tina',
 'tn',
 'tnxde',
 'to2argentina',
 'todosconmacri',
 'todosjuntosestamos',
 'todosunamentira',
 'todotienesufinal',
 'todounejemplo',
 'toleranciacero',
 'toner',
 'tormenta',
 'transgenicos',
 'travel',
 'triste',
 'tristesah',
 'trndnl',
 'tropaarg',
 'ttv',
 'tucuman',
 'tucumanelige',
 'turquia',
 'tusderechosomacri',
 'tv',
 'ultimahora',
 'ultimas',
 'ultimo_minuto',
 'ultimominuto',
 'ultimomomento',
 'unalatinoamericademocratica',
 'unamordidita',
 'unasur',
 'unidad',
 'unitedstates',
 'update',
 'urgente',
 'uribistas',
 'uruguay',
 'us',
 'usa',
 'ushuaia',
 'vaaestarbuenaargentina',
 'value',
 'vamos',
 'vamosargentina',
 'vamosdaniel',
 'vamosjuntos',
 'vamoslospibes',
 'vamosmacri',
 'vamosmm',
 'vamosporelcambio',
 'vamosquesepuede',
 'vamosscioli',
 'vautours',
 'vedaelectoral',
 'velorio',
 'venezolano',
 'venezuela',
 'venezuelaapoyaamacri',
 'venezuelagana',
 'venezuelaquierecambio',
 'venezuelaquierevivirmejor',
 'vera',
 'verguenza',
 'vgg',
 'vicentelopez',
 'viedma',
 'villamaria',
 'villanueva',
 'vision7',
 'viva',
 'vivaargentinalibre',
 'vivaasignacionuniversalporhijo',
 'vivalaclasemedia',
 'vivalademocracia',
 'vivamacri',
 'viviendolahistoria',
 'votaporlamanito',
 'votasinmiedo',
 'voteamacri',
 'votemosaunbostero',
 'voto',
 'voto2015',
 'votoafavor',
 'votodelcampo',
 'votoenblanco',
 'votoexterior',
 'votofpv',
 'votomacri',
 'votoobligatorio',
 'votoporandino',
 'votoporcronica',
 'votos',
 'votoycalle',
 'vrjournalism',
 'vzla',
 'vzlagritamacripresidente',
 'vzlaprohibidoolvidar',
 'waiting',
 'web',
 'whatsapp',
 'whatsisthis',
 'wow',
 'wtf',
 'xunaargentinamejor',
 'yacambiamos',
 'yacambiaron',
 'yaganomacri',
 'yahaynuevopresidente',
 'yavoteamacri',
 'yavotemacri',
 'yerbabuena',
 'yocambie',
 'yocambio',
 'yoelijoxmifuturo',
 'yofiscalizo',
 'yoli',
 'yolo',
 'yolovivi',
 'yolovoteamm',
 'yolovoto',
 'yolovotoamm',
 'yolovotomm',
 'yonolovote',
 'yonotraiciono',
 'yosobrevivialkirchnerismo',
 'yotodavianovoto',
 'your',
 'yovambio',
 'yovote',
 'yovotealcambio',
 'yovotealpresidente',
 'yovoteamacri',
 'yovoteamitre',
 'yovoteamm',
 'yovoteascioli',
 'yovoteelcambio',
 'yovotemacri',
 'yovotescioli',
 'yovoto',
 'yovotoamacri',
 'yovotoascioli',
 'yovotodanielscioli',
 'yovotoelcambio',
 'yovotoenenblanco',
 'yovotoloquecreo',
 'yovotomm',
 'yperdioigual',
 'ysevalayeguakk',
 'zanini',
 'zocalo'}
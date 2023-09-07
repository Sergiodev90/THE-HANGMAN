
import random
word_list = {
    'es':{

    'abruptamente': {
        'meaning': 'De manera súbita o inesperada.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=abruptamente',
    },
    'absurdo': {
        'meaning': 'Que carece de sentido o lógica.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=absurdo',
    },
    'abismo': {
        'meaning': 'Depresión profunda en la superficie de la Tierra.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=abismo',
    },
    'afijo': {
        'meaning': 'Elemento que se agrega a una palabra para formar otra.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=afijo',
    },
    'torcido': {
        'meaning': 'Que no está en línea recta o no es recto.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=torcido',
    },
    'avenida': {
        'meaning': 'Calle ancha, generalmente con árboles a los lados.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=avenida',
    },
    'incómodo': {
        'meaning': 'Que causa molestia o incomodidad.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=inc%C3%B3modo',
    },
    'axioma': {
        'meaning': 'Proposición que se considera evidente y no requiere demostración.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=axioma',
    },
    'azul': {
        'meaning': 'Color que se encuentra entre el verde y el violeta en el espectro visible.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=azul',
    },
    'gaita': {
        'meaning': 'Instrumento musical de viento típico de Escocia.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=gaita',
    },
    'moda': {
        'meaning': 'Tendencia o estilo en la ropa y accesorios.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=moda',
    },
    'banjo': {
        'meaning': 'Instrumento musical de cuerdas típico de la música folk.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=banjo',
    },
    'bayou': {
        'meaning': 'Canal o curso de agua lento, generalmente en zonas pantanosas.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=bayou',
    },
    'apicultor': {
        'meaning': 'Persona que cría y cuida abejas para producir miel.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=apicultor',
    },
    'bikini': {
        'meaning': 'Tipo de traje de baño de dos piezas.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=bikini',
    },
    'blitz': {
        'meaning': 'Ataque sorpresa y rápido, especialmente en contexto militar.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=blitz',
    },
    'ventisca': {
        'meaning': 'Viento fuerte acompañado de nieve o polvo que reduce la visibilidad.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=ventisca',
    },
    'boggle': {
        'meaning': 'Verbo que significa confundir o desconcertar.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=boggle',
    },
    'ratón': {
        'meaning': 'Roedor pequeño y común en muchas partes del mundo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=rat%C3%B3n',
    },
    'vagón': {
        'meaning': 'Carro o vehículo que se utiliza para transportar carga.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=vag%C3%B3n',
    },
    'caja llena': {
        'meaning': 'Contenedor que contiene objetos u otros contenedores.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=caja+llena',
    },
    'vaquero': {
        'meaning': 'Persona que trabaja en la cría de ganado, típica de la cultura del oeste de Estados Unidos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=vaquero',
    },
    'búfalo': {
        'meaning': 'Mamífero grande y pesado que se encuentra en América del Norte.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=b%C3%BAfalo',
    },
    'bufón': {
        'meaning': 'Persona que actúa de manera cómica o tonta para entretener a otros.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=buf%C3%B3n',
    },
    'exuberante': {
        'meaning': 'Que crece en abundancia y es vigoroso.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=exuberante',
    },
    'buitre': {
        'meaning': 'Ave rapaz que se alimenta de carroña.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=buitre',
    },
    'zumbido': {
        'meaning': 'Sonido continuo y vibrante, como el producido por un insecto o una máquina.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=zumbido',
    },
    'califa': {
        'meaning': 'Título utilizado por ciertos líderes musulmanes o gobernantes.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=califa',
    },
    'telaraña': {
        'meaning': 'Estructura de hilos que las arañas tejen para atrapar insectos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=telara%C3%B1a',
    },
    'soberbia': {
        'meaning': 'Sentimiento de superioridad o arrogancia.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=soberbia',
    },
    'croquet': {
        'meaning': 'Juego de pelota que se juega en un césped con mazos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=croquet',
    },
    'cripta': {
        'meaning': 'Lugar subterráneo utilizado para enterrar a los muertos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=cripta',
    },
    'Curazao': {
        'meaning': 'Isla del Caribe conocida por su belleza natural.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=Curazao',
    },
    'ciclo': {
        'meaning': 'Secuencia de eventos que se repiten en un patrón.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=ciclo',
    },
    'daiquiri': {
        'meaning': 'Cóctel cubano hecho con ron, limón y azúcar.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=daiquiri',
    },
    'dirndl': {
        'meaning': 'Tipo de vestido tradicional alemán.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=dirndl',
    },
    'desaprobar': {
        'meaning': 'Mostrar desacuerdo o desaprobación hacia algo o alguien.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=desaprobar',
    },
    'mareante': {
        'meaning': 'Que causa mareo o vértigo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=mareante',
    },
    'dúplex': {
        'meaning': 'Vivienda o edificio con dos pisos o niveles.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=d%C3%BAplex',
    },
    'enanos': {
        'meaning': 'Personas de estatura muy baja.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=enanos',
    },
    'malversar': {
        'meaning': 'Utilizar indebidamente fondos o recursos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=malversar',
    },
    'equipar': {
        'meaning': 'Proporcionar o dotar de equipos o herramientas.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=equipar',
    },
    'espionaje': {
        'meaning': 'Actividad de obtener información secreta de manera encubierta.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=espionaje',
    },
    'euouae': {
        'meaning': 'Secuencia de letras utilizada en música medieval.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=euouae',
    },
    'éxodo': {
        'meaning': 'Movimiento masivo de personas que abandonan un lugar en busca de mejores condiciones de vida.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=%C3%A9xodo',
    },
    'fingiendo': {
        'meaning': 'Actuando o comportándose de manera falsa.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=fingiendo',
    },
    'anzuelo de pez': {
        'meaning': 'Dispositivo utilizado en la pesca para atrapar peces.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=anzuelo+de+pez',
    },
    'reparable': {
        'meaning': 'Que puede ser reparado o corregido.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=reparable',
    },
    'fiordo': {
        'meaning': 'Entrada de mar estrecha entre montañas o acantilados.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=fiordo',
    },
    'panqueque': {
        'meaning': 'Tipo de torta plana y fina, generalmente cocida en una sartén.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=panqueque',
    },
    'chapoteo': {
        'meaning': 'Ruido o acción de salpicar agua.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=chapoteo',
    },
    'esponjosidad': {
        'meaning': 'Calidad de ser esponjoso o suave al tacto.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=esponjosidad',
    },
    'pasar volando': {
        'meaning': 'Moverse rápidamente a través de un lugar.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=pasar+volando',
    },
    'digitalis': {
        'meaning': 'Género de plantas que incluye la dedalera.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=digitalis',
    },
    'desmelenado': {
        'meaning': 'Que tiene el cabello suelto y desordenado.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=desmelenado',
    },
    'encrespado': {
        'meaning': 'Que está rizado o con ondas.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=encrespado',
    },
    'fucsia': {
        'meaning': 'Color rosa brillante y llamativo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=fucsia',
    },
    'divertido': {
        'meaning': 'Que provoca risa o diversión.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=divertido',
    },
    'charlatán': {
        'meaning': 'Persona que habla mucho y sin fundamento.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=charlat%C3%A1n',
    },
    'galaxia': {
        'meaning': 'Conjunto vasto de estrellas y otros cuerpos celestes.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=galaxia',
    },
    'galvanizar': {
        'meaning': 'Estimular o impulsar a la acción.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=galvanizar',
    },
    'glorieta': {
        'meaning': 'Área circular o plaza decorativa.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=glorieta',
    },
    'demonio': {
        'meaning': 'Entidad maligna en muchas religiones y culturas.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=demonio',
    },
    'gizmo': {
        'meaning': 'Término coloquial para un dispositivo o aparato mecánico.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=gizmo',
    },
    'luciérnaga': {
        'meaning': 'Insecto que emite luz en la oscuridad.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=luci%C3%A9rnaga',
    },
    'glifo': {
        'meaning': 'Símbolo o figura que representa un concepto.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=glifo',
    },
    'nudoso': {
        'meaning': 'Que tiene nudos o protuberancias.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=nudoso',
    },
    'gnóstico': {
        'meaning': 'Relacionado con la gnosis o conocimiento espiritual.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=gn%C3%B3stico',
    },
    'cotilleo': {
        'meaning': 'Chisme o conversación ociosa sobre la vida de otras personas.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=cotilleo',
    },
    'somnolencia': {
        'meaning': 'Estado de estar adormecido o con sueño.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=somnolencia',
    },
    'haiku': {
        'meaning': 'Forma poética japonesa de tres versos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=haiku',
    },
    'al azar': {
        'meaning': 'Sin un patrón o plan definido.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=al+azar',
    },
    'guion': {
        'meaning': 'Signo de puntuación utilizado para separar palabras o frases.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=guion',
    },
    'iatrogénico': {
        'meaning': 'Relacionado con enfermedades o efectos secundarios causados por la atención médica.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=iatrog%C3%A9nico',
    },
    'nevera': {
        'meaning': 'Electrodoméstico utilizado para refrigerar alimentos y bebidas.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=nevera',
    },
    'lesión': {
        'meaning': 'Daño o herida en el cuerpo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=lesi%C3%B3n',
    },
    'marfil': {
        'meaning': 'Material duro y blanco que proviene de los colmillos de ciertos animales.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=marfil',
    },
    'hiedra': {
        'meaning': 'Planta trepadora con hojas verdes y a menudo en forma de corazón.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=hiedra',
    },
    'premio mayor': {
        'meaning': 'El premio más grande que se puede ganar en un concurso o lotería.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=premio+mayor',
    },
    'ictericia': {
        'meaning': 'Coloración amarillenta de la piel y los ojos debido a problemas en el hígado.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=ictericia',
    },
    'rompecabezas': {
        'meaning': 'Juego o actividad en la que se ensamblan piezas para formar una imagen o resolver un problema.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=rompecabezas',
    },
    'cruzando': {
        'meaning': 'Atravesando o pasando por encima de algo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=cruzando',
    },
    'chiste': {
        'meaning': 'Historia o comentario humorístico.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=chiste',
    },
    'bollo': {
        'meaning': 'Tipo de panecillo o pastelito.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=bollo',
    },
    'jiu-jitsu': {
        'meaning': 'Arte marcial japonés que se enfoca en técnicas de autodefensa.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=jiu-jitsu',
    },
    'jinete': {
        'meaning': 'Persona que monta a caballo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=jinete',
    },
    'trotar': {
        'meaning': 'Correr a un ritmo suave y constante.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=trotar',
    },
    'bromear': {
        'meaning': 'Decir o hacer algo en tono humorístico o juguetón.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=bromear',
    },
    'afable': {
        'meaning': 'Amable y cordial en el trato con los demás.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=afable',
    },
    'alegre': {
        'meaning': 'Que experimenta felicidad o buen humor.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=alegre',
    },
    'jugoso': {
        'meaning': 'Que contiene mucho jugo o es sabroso.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=jugoso',
    },
    'gramófono': {
        'meaning': 'Dispositivo antiguo para reproducir música.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=gram%C3%B3fono',
    },
    'enorme': {
        'meaning': 'Muy grande en tamaño o magnitud.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=enorme',
    },
    'kayak': {
        'meaning': 'Tipo de embarcación pequeña utilizada para la navegación en aguas.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=kayak',
    },
    'kazoo': {
        'meaning': 'Instrumento musical que produce sonidos zumbadores.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=kazoo',
    },
    'mirilla': {
        'meaning': 'Dispositivo óptico utilizado para espiar o ver a través de una puerta o ventana.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=mirilla',
    },
    'caqui': {
        'meaning': 'Fruto de color amarillo o naranja que es dulce y astringente.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=caqui',
    },
    'kilobyte': {
        'meaning': 'Unidad de medida de datos en la computación.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=kilobyte',
    },
    'quiosco': {
        'meaning': 'Pequeña estructura o puesto de venta de periódicos, revistas u otros productos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=quiosco',
    },
    'cursilería': {
        'meaning': 'Elemento o comportamiento que es excesivamente sentimental o decorativo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=cursiler%C3%ADa',
    },
    'kiwi': {
        'meaning': 'Fruta pequeña de color verde o marrón con pulpa verde y sabor agridulce.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=kiwi',
    },
    'torpe': {
        'meaning': 'Que carece de habilidad o destreza.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=torpe',
    },
    'mochila': {
        'meaning': 'Bolsa que se lleva en la espalda sostenida por correas, utilizada para transportar objetos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=mochila',
    },
    'laringe': {
        'meaning': 'Órgano en el cuello que contiene las cuerdas vocales y permite la producción de sonidos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=laringe',
    },
    'longitudes': {
        'meaning': 'Medidas de distancia a lo largo de una línea o superficie.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=longitudes',
    },
    'afortunado': {
        'meaning': 'Que tiene buena suerte o está en una situación ventajosa.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=afortunado',
    },
    'lujo': {
        'meaning': 'Bienes o comodidades costosas y no esenciales.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=lujo',
    },
    'linfa': {
        'meaning': 'Líquido transparente que circula en el sistema linfático del cuerpo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=linfa',
    },
    'marqués': {
        'meaning': 'Título de nobleza.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=marqu%C3%A9s',
    },
    'matriz': {
        'meaning': 'Arreglo rectangular de elementos o componentes.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=matriz',
    },
    'megahertz': {
        'meaning': 'Unidad de medida de frecuencia en la computación.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=megahertz',
    },
    'microondas': {
        'meaning': 'Tipo de radiación electromagnética y un electrodoméstico utilizado para calentar alimentos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=microondas',
    },
    'mnemónico': {
        'meaning': 'Ayuda de memoria o dispositivo para recordar información.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=mnem%C3%B3nico',
    },
    'misterio': {
        'meaning': 'Situación o evento que es desconocido o inexplicable.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=misterio',
    },
    'nafta': {
        'meaning': 'Término utilizado en algunos lugares para referirse a la gasolina o el combustible para vehículos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=nafta',
    },
    'club nocturno': {
        'meaning': 'Establecimiento de entretenimiento que suele estar abierto durante la noche, con música y baile.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=club+nocturno',
    },
    'hoy en día': {
        'meaning': 'En la época actual o en el presente.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=hoy+en+d%C3%ADa',
    },
    'tonto': {
        'meaning': 'Persona que carece de inteligencia o sentido común.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=tonto',
    },
    'ninfa': {
        'meaning': 'Criatura mítica asociada con la naturaleza y la belleza.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=ninfa',
    },
    'ónix': {
        'meaning': 'Tipo de piedra semipreciosa que suele ser de color negro o verde oscuro.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=%C3%B3nix',
    },
    'ovario': {
        'meaning': 'Órgano reproductor femenino que produce óvulos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=ovario',
    },
    'oxidar': {
        'meaning': 'Reacción química en la que un material se combina con el oxígeno y forma óxido.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=oxidar',
    },
    'oxígeno': {
        'meaning': 'Elemento químico necesario para la respiración y la vida en la Tierra.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=ox%C3%ADgeno',
    },
    'piyama': {
        'meaning': 'Conjunto de ropa cómoda utilizado para dormir.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=piyama',
    },
    'cucú': {
        'meaning': 'Onomatopeya que imita el sonido de un cuco.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=cuc%C3%BA',
    },
    'flema': {
        'meaning': 'Moco o mucosidad en las vías respiratorias.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=flema',
    },
    'píxel': {
        'meaning': 'El punto más pequeño en una imagen digital.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=p%C3%ADxel',
    },
    'efecto': {
        'meaning': 'Resultado o consecuencia de una acción o evento.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=efecto',
    },
    'neumonía': {
        'meaning': 'Enfermedad pulmonar que inflama los pulmones.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=neumon%C3%ADa',
    },
    'polca': {
        'meaning': 'Baile y música de origen polaco.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=polca',
    },
    'pshaw': {
        'meaning': 'Expresión que denota desprecio o incredulidad.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=pshaw',
    },
    'psique': {
        'meaning': 'El alma o la mente.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=psique',
    },
    'cachorro': {
        'meaning': 'Cría de un mamífero, especialmente de un perro.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=cachorro',
    },
    'desconcertante': {
        'meaning': 'Que causa confusión o sorpresa.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=desconcertante',
    },
    'cuarzo': {
        'meaning': 'Mineral cristalino que se utiliza en joyería y electrónica.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=cuarzo',
    },
    'fila': {
        'meaning': 'Línea de objetos o personas colocadas una detrás de la otra.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=fila',
    },
    'burlas': {
        'meaning': 'Acción de burlarse o ridiculizar a alguien o algo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=burlas',
    },
    'quijotesco': {
        'meaning': 'Que se asemeja o recuerda a Don Quijote, un personaje de la literatura española conocido por su idealismo y aventuras.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=quijotesco',
    },
    'cuestionario': {
        'meaning': 'Conjunto de preguntas diseñadas para obtener información específica.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=cuestionario',
    },
    'cuestionarios': {
        'meaning': 'Forma plural de "cuestionario", que se refiere a varios conjuntos de preguntas.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=cuestionarios',
    },
    'quórum': {
        'meaning': 'Número mínimo de personas necesarias para llevar a cabo una reunión o tomar decisiones.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=qu%C3%B3rum',
    },
    'agitación': {
        'meaning': 'Estado de excitación o inquietud.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=agitaci%C3%B3n',
    },
    'ruibarbo': {
        'meaning': 'Planta y tallo comestible con sabor ácido, a menudo utilizado en postres.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=ruibarbo',
    },
    'ritmo': {
        'meaning': 'Patrón regular de sonidos o movimientos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=ritmo',
    },
    'carruaje': {
        'meaning': 'Vehículo antiguo tirado por caballos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=carruaje',
    },
    'aguardiente': {
        'meaning': 'Bebida alcohólica fuerte y destilada.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=aguardiente',
    },
    'rascarse': {
        'meaning': 'Frotar o rascar la piel para aliviar la picazón o el malestar.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=rascarse',
    },
    'cuchillo': {
        'meaning': 'Instrumento cortante con una hoja afilada utilizado para cortar alimentos u otros objetos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=cuchillo',
    },
    'elegante': {
        'meaning': 'Que tiene estilo y clase en su apariencia o comportamiento.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=elegante',
    },
    'esfinge': {
        'meaning': 'Criatura mitológica con cabeza humana y cuerpo de león.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=esfinge',
    },
    'aspersión': {
        'meaning': 'Acción de rociar o esparcir líquido sobre algo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=aspersi%C3%B3n',
    },
    'gritar': {
        'meaning': 'Elevar la voz en señal de enfado, sorpresa o emoción.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=gritar',
    },
    'personal': {
        'meaning': 'Relacionado con una persona o su vida privada.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=personal',
    },
    'fuerza': {
        'meaning': 'Capacidad de hacer trabajo o ejercer poder.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=fuerza',
    },
    'fortalezas': {
        'meaning': 'Forma plural de "fortaleza", que se refiere a las cualidades o características fuertes de alguien o algo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=fortalezas',
    },
    'estirar': {
        'meaning': 'Hacer que algo se alargue o extienda.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=estirar',
    },
    'fortaleza': {
        'meaning': 'Cualidad de ser fuerte o resistente.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=fortaleza',
    },
    'frustrado': {
        'meaning': 'Sentimiento de desánimo o decepción debido a la incapacidad para lograr algo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=frustrado',
    },
    'metro': {
        'meaning': 'Unidad de medida de longitud en el sistema métrico.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=metro',
    },
    'girar': {
        'meaning': 'Moverse en un círculo o alrededor de un punto.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=girar',
    },
    'síndrome': {
        'meaning': 'Conjunto de síntomas o características que indican una condición médica o psicológica.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=s%C3%ADndrome',
    },
    'despilfarrado': {
        'meaning': 'Gastado de manera excesiva o imprudente.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=despilfarrado',
    },
    'pulgar': {
        'meaning': 'El dedo más corto y grueso de la mano.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=pulgar',
    },
    'topacio': {
        'meaning': 'Gema preciosa de diversos colores.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=topacio',
    },
    'transcripción': {
        'meaning': 'Proceso de convertir el habla o el texto de un formato a otro, como de audio a texto.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=transcripci%C3%B3n',
    },
    'transgredir': {
        'meaning': 'Violar o quebrantar una ley, norma o regla.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=transgredir',
    },
    'trasplante': {
        'meaning': 'Procedimiento médico en el que se transfiere un órgano o tejido de una persona a otra.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=trasplante',
    },
    'triptongo': {
        'meaning': 'Secuencia de tres vocales que se pronuncian juntas en una sola sílaba.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=triptongo',
    },
    'duodécimo': {
        'meaning': 'Que ocupa el lugar número doce en una serie o secuencia.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=duod%C3%A9cimo',
    },
    'duodécimos': {
        'meaning': 'Forma plural de "duodécimo", que se refiere a los elementos que ocupan el lugar número doce en una serie o secuencia.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=duod%C3%A9cimos',
    },
    'desconocido': {
        'meaning': 'Que no es conocido o familiar.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=desconocido',
    },
    'indigno': {
        'meaning': 'Que no merece respeto o consideración debido a su falta de valor o dignidad.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=indigno',
    },
    'desabrochar': {
        'meaning': 'Abrir o soltar los broches o botones de una prenda o dispositivo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=desabrochar',
    },
    'barrio alto': {
        'meaning': 'Área de una ciudad o localidad que generalmente está asociada con la clase alta o acomodada.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=barrio+alto',
    },
    'vaporizar': {
        'meaning': 'Convertir un líquido en vapor o aerosol.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=vaporizar',
    },
    'zorra': {
        'meaning': 'Término coloquial que se utiliza para referirse a una mujer de manera despectiva.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=zorra',
    },
    'vodka': {
        'meaning': 'Bebida alcohólica destilada originaria de Europa del Este y Rusia.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=vodka',
    },
    'vudú': {
        'meaning': 'Sistema de creencias y prácticas mágicas originario de algunas culturas africanas y afrocaribeñas.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=vud%C3%BA',
    },
    'vórtice': {
        'meaning': 'Remolino de líquido o aire que gira alrededor de un punto central.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=v%C3%B3rtice',
    },
    'voyeurismo': {
        'meaning': 'Práctica de observar a personas en momentos íntimos sin su conocimiento o consentimiento.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=voyeurismo',
    },
    'pasarela': {
        'meaning': 'Plataforma elevada utilizada para desfilar modelos en una pasarela de moda.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=pasarela',
    },
    'vals': {
        'meaning': 'Género musical y baile de ritmo rápido en compás de tres tiempos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=vals',
    },
    'ola': {
        'meaning': 'Movimiento ondulatorio de una superficie líquida, especialmente en el mar.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=ola',
    },
    'ondulado': {
        'meaning': 'Que tiene forma de ondas o curvas suaves.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=ondulado',
    },
    'ceroso': {
        'meaning': 'Que tiene la apariencia o características de la cera.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=ceroso',
    },
    'manantial': {
        'meaning': 'Lugar de donde brota agua natural de la tierra.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=manantial',
    },
    'jadeante': {
        'meaning': 'Que respira con dificultad y agitación debido a un esfuerzo o nerviosismo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=jadeante',
    },
    'whisky': {
        'meaning': 'Bebida alcohólica destilada originaria de Escocia e Irlanda.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=whisky',
    },
    'zumbido': {
        'meaning': 'Sonido continuo y vibrante, similar al de un insecto o una máquina.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=zumbido',
    },
    'quienquiera': {
        'meaning': 'Cualquier persona que; cualquiera que sea.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=quienquiera',
    },
    'miedoso': {
        'meaning': 'Que siente o muestra temor con facilidad; asustadizo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=miedoso',
    },
    'brujería': {
        'meaning': 'Conjunto de creencias y prácticas relacionadas con la magia y lo sobrenatural.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=brujer%C3%ADa',
    },
    'mago': {
        'meaning': 'Persona que practica la magia y realiza trucos de ilusionismo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=mago',
    },
    'mareado': {
        'meaning': 'Que experimenta una sensación de vértigo o náusea.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=mareado',
    },
    'pulsera': {
        'meaning': 'Adorno que se lleva en la muñeca, generalmente hecho de metal, tela o cuentas.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=pulsera',
    },
    'wiverino': {
        'meaning': 'Esta palabra no parece tener un meaning en español. Puede ser un error tipográfico o una palabra en otro idioma.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=wiverino',
    },
    'xilófono': {
        'meaning': 'Instrumento musical de percusión formado por láminas de madera dispuestas en orden ascendente y golpeadas con baquetas.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=xil%C3%B3fono',
    },
    'yates': {
        'meaning': 'Embarcaciones de recreo de lujo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=yates',
    },
    '¡upi!': {
        'meaning': 'Expresión de alegría o entusiasmo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=%C2%A1upi%21',
    },
    'apareado': {
        'meaning': 'Colocado en pares o conjuntos de dos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=apareado',
    },
    'juvenil': {
        'meaning': 'Relativo o perteneciente a la juventud.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=juvenil',
    },
    'delicioso': {
        'meaning': 'Que tiene un sabor muy agradable y placentero.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=delicioso',
    },
    'céfiro': {
        'meaning': 'Viento suave y agradable que sopla en primavera.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=c%C3%A9firo',
    },
    'zigzag': {
        'meaning': 'Línea que forma una serie de ángulos alternados y agudos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=zigzag',
    },
    'zigzagueando': {
        'meaning': 'Movimiento que sigue un patrón de zigzag.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=zigzagueando',
    },
    'nada': {
        'meaning': 'Falta o carencia de algo.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=nada',
    },
    'cremallera': {
        'meaning': 'Dispositivo mecánico que permite abrir y cerrar prendas de vestir o bolsos de manera rápida y segura.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=cremallera',
    },
    'zodiaco': {
        'meaning': 'Cinturón imaginario de la esfera celeste que se divide en doce signos astrológicos.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=zodiaco',
    },
    'zombi': {
        'meaning': 'Persona que se cree que ha sido reanimada después de la muerte y no tiene voluntad propia.',
        'link': 'https://www.wordreference.com/es/en/translation.asp?spen=zombi',
    },
},
    'en' :{

        'abruptly': {
            'meaning': 'Suddenly and without warning.',
            'link': 'https://www.yourdictionary.com/abruptly',
        },
        'absurd': {
            'meaning': 'Wildly unreasonable, illogical, or inappropriate.',
            'link': 'https://www.yourdictionary.com/absurd',
        },
        'abyss': {
            'meaning': 'A deep, immeasurable space, gulf, or cavity; vast chasm.',
            'link': 'https://www.yourdictionary.com/abyss',
        },
        'affix': {
            'meaning': 'A morpheme added at the end of a word to form a derivative.',
            'link': 'https://www.yourdictionary.com/affix',
        },
        'askew': {
            'meaning': 'Not in a straight or level position.',
            'link': 'https://www.yourdictionary.com/askew',
        },
        'avenue': {
            'meaning': 'A wide street or thoroughfare.',
            'link': 'https://www.yourdictionary.com/avenue',
        },
        'awkward': {
            'meaning': 'Lacking skill or dexterity.',
            'link': 'https://www.yourdictionary.com/awkward',
        },
        'axiom': {
            'meaning': 'A self-evident truth that requires no proof.',
            'link': 'https://www.yourdictionary.com/axiom',
        },
        'azure': {
            'meaning': 'The blue color of a cloudless sky.',
            'link': 'https://www.yourdictionary.com/azure',
        },
        'bagpipes': {
            'meaning': 'A musical instrument with reeds and a melody pipe.',
            'link': 'https://www.yourdictionary.com/bagpipes',
        },
        'bandwagon': {
            'meaning': 'A popular trend or activity that attracts widespread support.',
            'link': 'https://www.yourdictionary.com/bandwagon',
        },
        'banjo': {
            'meaning': 'A musical instrument with a round body and strings.',
            'link': 'https://www.yourdictionary.com/banjo',
        },
        'bayou': {
            'meaning': 'A marshy, sluggish body of water.',
            'link': 'https://www.yourdictionary.com/bayou',
        },
        'beekeeper': {
            'meaning': 'A person who keeps and cares for bees.',
            'link': 'https://www.yourdictionary.com/beekeeper',
        },
        'bikini': {
            'meaning': 'A two-piece bathing suit for women.',
            'link': 'https://www.yourdictionary.com/bikini',
        },
        'blitz': {
            'meaning': 'A sudden, intense attack or campaign.',
            'link': 'https://www.yourdictionary.com/blitz',
        },
        'blizzard': {
            'meaning': 'A severe snowstorm with strong winds and low visibility.',
            'link': 'https://www.yourdictionary.com/blizzard',
        },
        'boggle': {
            'meaning': 'To overwhelm or bewilder, as with complexity or uncertainty.',
            'link': 'https://www.yourdictionary.com/boggle',
        },
        'bookworm': {
            'meaning': 'A person who enjoys reading books.',
            'link': 'https://www.yourdictionary.com/bookworm',
        },
        'boxcar': {
            'meaning': 'A type of railroad car used for transporting goods.',
            'link': 'https://www.yourdictionary.com/boxcar',
        },
        'boxful': {
            'meaning': 'As much as a box can hold.',
            'link': 'https://www.yourdictionary.com/boxful',
        },
        'buckaroo': {
            'meaning': 'A cowboy, especially one who tends cattle.',
            'link': 'https://www.yourdictionary.com/buckaroo',
        },
        'buffalo': {
            'meaning': 'A large, North American mammal known for its humped shoulders and horns.',
            'link': 'https://www.yourdictionary.com/buffalo',
        },
        'buffoon': {
            'meaning': 'A person who behaves in a silly or ridiculous manner.',
            'link': 'https://www.yourdictionary.com/buffoon',
        },
        'buxom': {
            'meaning': 'Having a full, curvaceous figure.',
            'link': 'https://www.yourdictionary.com/buxom',
        },
        'buzzard': {
            'meaning': 'A large bird of prey with a wingspan of 3-4 feet.',
            'link': 'https://www.yourdictionary.com/buzzard',
        },
        'buzzing': {
            'meaning': 'A continuous, low, humming sound.',
            'link': 'https://www.yourdictionary.com/buzzing',
        },
        'buzzwords': {
            'meaning': 'Words or phrases that are trendy or popular but often lack substance.',
            'link': 'https://www.yourdictionary.com/buzzwords',
        },
        'caliph': {
            'meaning': 'A religious and political leader in some Muslim countries.',
            'link': 'https://www.yourdictionary.com/caliph',
        },
        'cobweb': {
            'meaning': "A spider's web, especially an abandoned one.",
            'link': 'https://www.yourdictionary.com/cobweb',
        },
        'cockiness': {
            'meaning': 'Overconfidence or arrogance.',
            'link': 'https://www.yourdictionary.com/cockiness',
        },
        'croquet': {
            'meaning': 'A lawn game played with wooden mallets and balls.',
            'link': 'https://www.yourdictionary.com/croquet',
        },
        'crypt': {
            'meaning': 'A burial chamber or underground vault.',
            'link': 'https://www.yourdictionary.com/crypt',
        },
        'curacao': {
            'meaning': 'A liqueur made from the dried peel of bitter oranges.',
            'link': 'https://www.yourdictionary.com/curacao',
        },
        'cycle': {
            'meaning': 'A series of events that repeat in a predictable pattern.',
            'link': 'https://www.yourdictionary.com/cycle',
        },
        'daiquiri': {
            'meaning': 'A cocktail made with rum, lime juice, and sugar.',
            'link': 'https://www.yourdictionary.com/daiquiri',
        },
        'dirndl': {
            'meaning': 'A traditional dress worn in some German-speaking countries.',
            'link': 'https://www.yourdictionary.com/dirndl',
        },
        'disavow': {
            'meaning': 'To deny any responsibility or support for something.',
            'link': 'https://www.yourdictionary.com/disavow',
        },
        'dizzying': {
            'meaning': 'Causing dizziness or vertigo.',
            'link': 'https://www.yourdictionary.com/dizzying',
        },
        'duplex': {
            'meaning': 'A house or apartment with two separate living units.',
            'link': 'https://www.yourdictionary.com/duplex',
        },
        'dwarves': {
            'meaning': 'Plural of "dwarf," a person of unusually small stature.',
            'link': 'https://www.yourdictionary.com/dwarves',
        },
        'embezzle': {
            'meaning': 'To steal money that has been entrusted to you.',
            'link': 'https://www.yourdictionary.com/embezzle',
        },
        'equip': {
            'meaning': 'To provide with the necessary tools or equipment.',
            'link': 'https://www.yourdictionary.com/equip',
        },
        'espionage': {
            'meaning': 'The practice of spying or using spies to obtain information.',
            'link': 'https://www.yourdictionary.com/espionage',
        },
        'euouae': {
            'meaning': 'A medieval musical term.',
            'link': 'https://www.yourdictionary.com/euouae',
        },
        'exodus': {
            'meaning': 'A mass departure or emigration, usually of a large group of people.',
            'link': 'https://www.yourdictionary.com/exodus',
        },
        'faking': {
            'meaning': 'Pretending or simulating something.',
            'link': 'https://www.yourdictionary.com/faking',
        },
        'fishhook': {
            'meaning': 'A curved, pointed instrument used to catch fish.',
            'link': 'https://www.yourdictionary.com/fishhook',
        },
        'fixable': {
            'meaning': 'Capable of being repaired or corrected.',
            'link': 'https://www.yourdictionary.com/fixable',
        },
        'fjord': {
            'meaning': 'A long, narrow inlet of the sea between high cliffs or steep slopes.',
            'link': 'https://www.yourdictionary.com/fjord',
        },
        'flapjack': {
            'meaning': 'A thick pancake or griddlecake.',
            'link': 'https://www.yourdictionary.com/flapjack',
        },
        'flopping': {
            'meaning': 'Making a noise like something flapping.',
            'link': 'https://www.yourdictionary.com/flopping',
        },
        'fluffiness': {
            'meaning': 'The quality or state of being fluffy, light, or soft.',
            'link': 'https://www.yourdictionary.com/fluffiness',
        },
        'flyby': {
            'meaning': 'A close approach or pass by a flying object.',
            'link': 'https://www.yourdictionary.com/flyby',
        },
        'foxglove': {
            'meaning': 'A tall, bell-shaped flower with colorful petals.',
            'link': 'https://www.yourdictionary.com/foxglove',
        },
        'frazzled': {
            'meaning': 'Extremely tired or exhausted.',
            'link': 'https://www.yourdictionary.com/frazzled',
        },
        'frizzled': {
            'meaning': 'Cooked or fried until crisp and curled.',
            'link': 'https://www.yourdictionary.com/frizzled',
        },
        'fuchsia': {
            'meaning': 'A bright pink or purplish-red color.',
            'link': 'https://www.yourdictionary.com/fuchsia',
        },
        'funny': {
            'meaning': 'Causing laughter or amusement; humorous.',
            'link': 'https://www.yourdictionary.com/funny',
        },
        'gabby': {
            'meaning': 'Talkative, especially excessively or annoyingly so.',
            'link': 'https://www.yourdictionary.com/gabby',
        },
        'galaxy': {
            'meaning': 'A massive system of stars, gas, and dust bound together by gravity.',
            'link': 'https://www.yourdictionary.com/galaxy',
        },
        'galvanize': {
            'meaning': 'To shock or stimulate into action; excite.',
            'link': 'https://www.yourdictionary.com/galvanize',
        },
        'gazebo': {
            'meaning': 'An outdoor structure, often with open sides, used for relaxation or entertainment.',
            'link': 'https://www.yourdictionary.com/gazebo',
        },
        'giaour': {
            'meaning': 'A derogatory term used in some contexts to refer to a non-Muslim person.',
            'link': 'https://www.yourdictionary.com/giaour',
        },
        'gizmo': {
            'meaning': 'A gadget or device, especially one whose name is unknown or forgotten.',
            'link': 'https://www.yourdictionary.com/gizmo',
        },
        'glowworm': {
            'meaning': 'A bioluminescent insect larva or adult that emits a soft light.',
            'link': 'https://www.yourdictionary.com/glowworm',
        },
        'glyph': {
            'meaning': 'A symbol or character in a writing system, such as hieroglyphics.',
            'link': 'https://www.yourdictionary.com/glyph',
        },
        'gnarly': {
            'meaning': 'Unpleasant or difficult; often used to describe a gnarled or twisted appearance.',
            'link': 'https://www.yourdictionary.com/gnarly',
        },
        'gnostic': {
            'meaning': 'Relating to Gnosticism, a religious and philosophical movement.',
            'link': 'https://www.yourdictionary.com/gnostic',
        },
        'gossip': {
            'meaning': 'Casual or idle talk, often about the personal affairs of others.',
            'link': 'https://www.yourdictionary.com/gossip',
        },
        'grogginess': {
            'meaning': 'A state of dizziness or confusion, often after waking up.',
            'link': 'https://www.yourdictionary.com/grogginess',
        },
        'haiku': {
            'meaning': 'A traditional Japanese poem with three lines and a 5-7-5 syllable structure.',
            'link': 'https://www.yourdictionary.com/haiku',
        },
        'haphazard': {
            'meaning': 'Lacking any obvious principle of organization; random.',
            'link': 'https://www.yourdictionary.com/haphazard',
        },
        'hyphen': {
            'meaning': 'A punctuation mark (-) used to join words or parts of words.',
            'link': 'https://www.yourdictionary.com/hyphen',
        },
        'iatrogenic': {
            'meaning': 'Relating to illness or side effects caused by medical treatment.',
            'link': 'https://www.yourdictionary.com/iatrogenic',
        },
        'icebox': {
            'meaning': 'An insulated container or room for storing ice or food at low temperatures.',
            'link': 'https://www.yourdictionary.com/icebox',
        },
        'injury': {
            'meaning': 'Physical harm or damage to the body.',
            'link': 'https://www.yourdictionary.com/injury',
        },
        'ivory': {
            'meaning': 'A hard, white material from the tusks of elephants and other animals.',
            'link': 'https://www.yourdictionary.com/ivory',
        },
        'ivy': {
            'meaning': 'A climbing plant with dark green leaves, often used for decoration.',
            'link': 'https://www.yourdictionary.com/ivy',
        },
        'jackpot': {
            'meaning': 'A large prize or reward, especially in gambling or a lottery.',
            'link': 'https://www.yourdictionary.com/jackpot',
        },
        'jaundice': {
            'meaning': 'A medical condition that causes yellowing of the skin and eyes.',
            'link': 'https://www.yourdictionary.com/jaundice',
        },
        'jawbreaker': {
            'meaning': 'A hard, spherical candy that is difficult to bite into.',
            'link': 'https://www.yourdictionary.com/jawbreaker',
        },
        'jaywalk': {
            'meaning': 'To cross a street in a reckless or illegal manner.',
            'link': 'https://www.yourdictionary.com/jaywalk',
        },
        'jazziest': {
            'meaning': 'Superlative form of "jazzy," meaning lively, energetic, or stylish.',
            'link': 'https://www.yourdictionary.com/jazziest',
        },
        'jazzy': {
            'meaning': 'Lively, energetic, or stylish, often associated with jazz music.',
            'link': 'https://www.yourdictionary.com/jazzy',
        },
        'jelly': {
            'meaning': 'A sweet, semiliquid substance made from fruit juice and sugar.',
            'link': 'https://www.yourdictionary.com/jelly',
        },
        'jigsaw': {
            'meaning': 'A type of puzzle with irregularly shaped pieces that fit together to form an image.',
            'link': 'https://www.yourdictionary.com/jigsaw',
        },
        'jinx': {
            'meaning': 'A superstition or belief in bad luck.',
            'link': 'https://www.yourdictionary.com/jinx',
        },
        'jiujitsu': {
            'meaning': 'A martial art that focuses on grappling and submission techniques.',
            'link': 'https://www.yourdictionary.com/jiujitsu',
        },
        'jockey': {
            'meaning': 'A person who rides horses in races.',
            'link': 'https://www.yourdictionary.com/jockey',
        },
        'jogging': {
            'meaning': 'Running at a slow, steady pace for exercise.',
            'link': 'https://www.yourdictionary.com/jogging',
        },
        'joking': {
            'meaning': 'Engaging in humor or making jokes.',
            'link': 'https://www.yourdictionary.com/joking',
        },
        'jovial': {
            'meaning': 'Full of high-spirited energy and good humor.',
            'link': 'https://www.yourdictionary.com/jovial',
        },
        'joyful': {
            'meaning': 'Feeling or expressing great happiness or pleasure.',
            'link': 'https://www.yourdictionary.com/joyful',
        },
        'juicy': {
            'meaning': 'Full of juice or flavor; succulent.',
            'link': 'https://www.yourdictionary.com/juicy',
        },
        'jukebox': {
            'meaning': 'A machine that plays selected music when money is inserted.',
            'link': 'https://www.yourdictionary.com/jukebox',
        },
        'jumbo': {
            'meaning': 'Extremely large or oversized.',
            'link': 'https://www.yourdictionary.com/jumbo',
        },
        'kayak': {
            'meaning': 'A small, narrow watercraft used for paddling.',
            'link': 'https://www.yourdictionary.com/kayak',
        },
        'kazoo': {
            'meaning': 'A musical instrument that produces a buzzing sound when hummed into.',
            'link': 'https://www.yourdictionary.com/kazoo',
        },
        'keyhole': {
            'meaning': 'A hole for inserting or turning a key in a lock.',
            'link': 'https://www.yourdictionary.com/keyhole',
        },
        'khaki': {
            'meaning': 'A dull, brownish-yellow color.',
            'link': 'https://www.yourdictionary.com/khaki',
        },
        'kilobyte': {
            'meaning': 'A unit of digital information equal to 1,024 bytes.',
            'link': 'https://www.yourdictionary.com/kilobyte',
        },
        'kiosk': {
            'meaning': 'A small, freestanding structure used for information or commerce.',
            'link': 'https://www.yourdictionary.com/kiosk',
        },
        'kitsch': {
            'meaning': 'Art, objects, or design that is considered in poor taste, often for being gaudy or sentimental.',
            'link': 'https://www.yourdictionary.com/kitsch',
        },
        'kiwifruit': {
            'meaning': 'A small, green fruit with fuzzy brown skin and bright green flesh.',
            'link': 'https://www.yourdictionary.com/kiwifruit',
        },
        'klutz': {
            'meaning': 'A clumsy or awkward person.',
            'link': 'https://www.yourdictionary.com/klutz',
        },
        'knapsack': {
            'meaning': "A small bag with shoulder straps, typically used for carrying items on one's back",
            'link': 'https://www.yourdictionary.com/knapsack',
        },
        'larynx': {
            'meaning': 'The voice box in the human throat.',
            'link': 'https://www.yourdictionary.com/larynx',
        },
        'lengths': {
            'meaning': 'Plural of "length," referring to the measurement of something from end to end.',
            'link': 'https://www.yourdictionary.com/lengths',
        },
        'lucky': {
            'meaning': 'Having good luck; fortunate.',
            'link': 'https://www.yourdictionary.com/lucky',
        },
        'luxury': {
            'meaning': 'The state of great comfort and extravagance.',
            'link': 'https://www.yourdictionary.com/luxury',
        },
        'lymph': {
            'meaning': 'A colorless fluid containing white blood cells and transported by the lymphatic system.',
            'link': 'https://www.yourdictionary.com/lymph',
        },
        'marquis': {
            'meaning': 'A nobleman ranking above a count and below a duke.',
            'link': 'https://www.yourdictionary.com/marquis',
        },
        'matrix': {
            'meaning': 'A rectangular array of numbers, symbols, or expressions.',
            'link': 'https://www.yourdictionary.com/matrix',
        },
        'megahertz': {
            'meaning': 'A unit of frequency equal to one million hertz.',
            'link': 'https://www.yourdictionary.com/megahertz',
        },
        'microwave': {
            'meaning': 'An electromagnetic wave with a wavelength in the microwave range.',
            'link': 'https://www.yourdictionary.com/microwave',
        },
        'mnemonic': {
            'meaning': 'A device or technique used to aid memory.',
            'link': 'https://www.yourdictionary.com/mnemonic',
        },
        'mystify': {
            'meaning': 'To perplex or bewilder someone.',
            'link': 'https://www.yourdictionary.com/mystify',
        },
        'naphtha': {
            'meaning': 'A flammable liquid hydrocarbon mixture used as a solvent or fuel.',
            'link': 'https://www.yourdictionary.com/naphtha',
        },
 

        'nightclub': {
            'meaning': 'A place of entertainment that is open late at night and typically offers music, dancing, and drinks.',
            'link': 'https://www.yourdictionary.com/nightclub',
        },
        'nowadays': {
            'meaning': 'In the present time; currently.',
            'link': 'https://www.yourdictionary.com/nowadays',
        },
        'numbskull': {
            'meaning': 'A foolish or stupid person; a blockhead.',
            'link': 'https://www.yourdictionary.com/numbskull',
        },
        'nymph': {
            'meaning': 'In mythology, a beautiful female spirit associated with nature, often found in forests, rivers, and other natural settings.',
            'link': 'https://www.yourdictionary.com/nymph',
        },
        'onyx': {
            'meaning': 'A type of black or dark-colored gemstone, often used in jewelry.',
            'link': 'https://www.yourdictionary.com/onyx',
        },
        'ovary': {
            'meaning': 'A female reproductive organ that produces eggs and hormones.',
            'link': 'https://www.yourdictionary.com/ovary',
        },
        'oxidize': {
            'meaning': 'To undergo a chemical reaction in which oxygen combines with a substance, often causing rust or tarnish.',
            'link': 'https://www.yourdictionary.com/oxidize',
        },
        'oxygen': {
            'meaning': 'A chemical element with the symbol "O" and atomic number 8, essential for respiration and combustion.',
            'link': 'https://www.yourdictionary.com/oxygen',
        },
        'pajama': {
            'meaning': 'A loose-fitting garment worn for sleeping or lounging, typically consisting of pants and a shirt.',
            'link': 'https://www.yourdictionary.com/pajama',
        },
        'peekaboo': {
            'meaning': "A children's game in which one person hides their face and then reveals it, often saying 'peekaboo.'",
            'link': 'https://www.yourdictionary.com/peekaboo',
        },
        'phlegm': {
            'meaning': 'A thick, sticky mucus produced by the respiratory system, often when a person has a cold or respiratory infection.',
            'link': 'https://www.yourdictionary.com/phlegm',
        },
        'pixel': {
            'meaning': 'The smallest unit of a digital image, typically a square or dot that represents a single color.',
            'link': 'https://www.yourdictionary.com/pixel',
        },
        'pizazz': {
            'meaning': 'An attractive combination of vitality and glamour; often used to describe style or flair.',
            'link': 'https://www.yourdictionary.com/pizazz',
        },
        'pneumonia': {
            'meaning': 'An inflammatory condition of the lungs, often caused by infection, leading to symptoms such as fever, cough, and difficulty breathing.',
            'link': 'https://www.yourdictionary.com/pneumonia',
        },
        'polka': {
            'meaning': 'A lively dance with a fast tempo, often accompanied by accordion music.',
            'link': 'https://www.yourdictionary.com/polka',
        },
        'pshaw': {
            'meaning': 'An exclamation of disdain or disbelief; a dismissive expression.',
            'link': 'https://www.yourdictionary.com/pshaw',
        },
        'psyche': {
            'meaning': 'The human soul, mind, or spirit; often used in psychology and philosophy.',
            'link': 'https://www.yourdictionary.com/psyche',
        },
        'puppy': {
            'meaning': 'A young dog, often used affectionately.',
            'link': 'https://www.yourdictionary.com/puppy',
        },
        'puzzling': {
            'meaning': 'Causing confusion or difficulty in understanding; mysterious.',
            'link': 'https://www.yourdictionary.com/puzzling',
        },
        'quartz': {
            'meaning': 'A hard, crystalline mineral often used in jewelry and electronic devices.',
            'link': 'https://www.yourdictionary.com/quartz',
        },
        'queue': {
            'meaning': 'A line or sequence of people or things waiting their turn.',
            'link': 'https://www.yourdictionary.com/queue',
        },
        'quips': {
            'meaning': 'Clever or witty remarks or comments.',
            'link': 'https://www.yourdictionary.com/quips',
        },
        'quixotic': {
            'meaning': 'Exceedingly idealistic, unrealistic, and impractical in a way that is charming but ultimately unachievable.',
            'link': 'https://www.yourdictionary.com/quixotic',
        },
        'quiz': {
            'meaning': 'A test or examination designed to assess knowledge, often in a competitive or informal context.',
            'link': 'https://www.yourdictionary.com/quiz',
        },
        'quizzes': {
            'meaning': 'Plural of "quiz," referring to multiple tests or examinations.',
            'link': 'https://www.yourdictionary.com/quizzes',
        },
        'quorum': {
            'meaning': 'The minimum number of members required to conduct business or make decisions in a group or organization.',
            'link': 'https://www.yourdictionary.com/quorum',
        },
        'razzmatazz': {
            'meaning': 'Elaborate or showy activity or display designed to attract attention or impress.',
            'link': 'https://www.yourdictionary.com/razzmatazz',
        },
        'rhubarb': {
            'meaning': 'A tart, red or green stalk of a plant used in cooking, often in pies and desserts.',
            'link': 'https://www.yourdictionary.com/rhubarb',
        },
        'rhythm': {
            'meaning': 'A regular and repeated pattern of movement or sound, often in music and dance.',
            'link': 'https://www.yourdictionary.com/rhythm',
        },
        'rickshaw': {
            'meaning': 'A small, two-wheeled cart pulled by a person, often used for transportation in some Asian countries.',
            'link': 'https://www.yourdictionary.com/rickshaw',
        },
        'schnapps': {
            'meaning': 'A type of strong alcoholic spirit or liqueur, typically flavored and often served as a shot.',
            'link': 'https://www.yourdictionary.com/schnapps',
        },
        'scratch': {
            'meaning': "To mark or damage the surface of something with a sharp object or one's nails.",
            'link': 'https://www.yourdictionary.com/scratch',
        },
        'shiv': {
            'meaning': 'A makeshift knife or sharp implement, often used as a weapon.',
            'link': 'https://www.yourdictionary.com/shiv',
        },
        'snazzy': {
            'meaning': 'Stylish, fashionable, or impressive in a flashy way.',
            'link': 'https://www.yourdictionary.com/snazzy',
        },
        'sphinx': {
            'meaning': 'In mythology, a creature with the head of a human and the body of a lion, often depicted as a guardian of secrets and riddles.',
            'link': 'https://www.yourdictionary.com/sphinx',
        },
        'spritz': {
            'meaning': 'To spray or squirt a liquid, often used in the context of adding carbonation or flavor to a drink.',
            'link': 'https://www.yourdictionary.com/spritz',
        },
        'squawk': {
            'meaning': 'A loud, harsh, and shrill noise or sound, often made by birds or machines.',
            'link': 'https://www.yourdictionary.com/squawk',
        },
        'staff': {
            'meaning': 'A group of employees who work for an organization or business.',
            'link': 'https://www.yourdictionary.com/staff',
        },
        'strength': {
            'meaning': 'The quality or state of being physically strong; the capacity to withstand force or pressure.',
            'link': 'https://www.yourdictionary.com/strength',
        },
        'strengths': {
            'meaning': 'Plural of "strength," referring to multiple qualities of being strong or resilient.',
            'link': 'https://www.yourdictionary.com/strengths',
        },
        'stretch': {
            'meaning': 'To extend or lengthen something beyond its normal limits; to reach or pull to full length.',
            'link': 'https://www.yourdictionary.com/stretch',
        },
        'stronghold': {
            'meaning': 'A heavily fortified and secure place, often used in the context of a fortress or stronghold.',
            'link': 'https://www.yourdictionary.com/stronghold',
        },
        'stymied': {
            'meaning': 'To be hindered or prevented from making progress or achieving a goal.',
            'link': 'https://www.yourdictionary.com/stymied',
        },
        'subway': {
            'meaning': 'An underground electric railroad, often used for public transportation in urban areas.',
            'link': 'https://www.yourdictionary.com/subway',
        },
        'swivel': {
            'meaning': 'To turn or rotate on a pivot, often used to describe a chair or other object that can rotate.',
            'link': 'https://www.yourdictionary.com/swivel',
        },
        'syndrome': {
            'meaning': 'A group of symptoms that characterize a specific medical condition or psychological disorder.',
            'link': 'https://www.yourdictionary.com/syndrome',
        },
        'thriftless': {
            'meaning': 'Wasteful or not economical; lacking in thrift or frugality.',
            'link': 'https://www.yourdictionary.com/thriftless',
        },
        'thumbscrew': {
            'meaning': "A device or instrument used to apply pressure to a person's thumb, often for the purpose of torture or coercion.",
            'link': 'https://www.yourdictionary.com/thumbscrew',
        },
        'topaz': {
            'meaning': 'A precious stone, typically yellow or brownish-yellow in color.',
            'link': 'https://www.yourdictionary.com/topaz',
        },
        'transcript': {
            'meaning': 'A written or printed copy of a conversation, speech, or other spoken or recorded material.',
            'link': 'https://www.yourdictionary.com/transcript',
        },
        'transgress': {
            'meaning': 'To violate a law, rule, or code of conduct; to commit an offense or wrongdoing.',
            'link': 'https://www.yourdictionary.com/transgress',
        },
        'transplant': {
            'meaning': 'To move or transfer an organ, tissue, or plant from one place or organism to another.',
            'link': 'https://www.yourdictionary.com/transplant',
        },
        'triphthong': {
            'meaning': 'A complex vowel sound that consists of three successive vowel sounds within the same syllable.',
            'link': 'https://www.yourdictionary.com/triphthong',
        },
        'twelfth': {
            'meaning': 'The ordinal number for the number twelve.',
            'link': 'https://www.yourdictionary.com/twelfth',
        },
        'twelfths': {
            'meaning': 'Plural of "twelfth," referring to multiple occurrences of the number twelve in a series.',
            'link': 'https://www.yourdictionary.com/twelfths',
        },
        'unknown': {
            'meaning': 'Not known or familiar; not recognized or identified.',
            'link': 'https://www.yourdictionary.com/unknown',
        },
        'unworthy': {
            'meaning': 'Not deserving of honor, respect, or consideration; lacking in worthiness.',
            'link': 'https://www.yourdictionary.com/unworthy',
        },
        'unzip': {
            'meaning': 'To open or extract the contents of a compressed or zipped file or container.',
            'link': 'https://www.yourdictionary.com/unzip',
        },
        'uptown': {
            'meaning': 'The residential or more upscale area of a city, typically located at a higher elevation.',
            'link': 'https://www.yourdictionary.com/uptown',
        },
        'vaporize': {
            'meaning': 'To convert a substance from a liquid or solid state into vapor or gas.',
            'link': 'https://www.yourdictionary.com/vaporize',
        },
        'vixen': {
            'meaning': 'A female fox; often used informally to describe a woman who is fierce or ill-tempered.',
            'link': 'https://www.yourdictionary.com/vixen',
        },
        'vodka': {
            'meaning': 'A colorless and flavorless alcoholic beverage distilled from grains or potatoes.',
            'link': 'https://www.yourdictionary.com/vodka',
        },
        'voodoo': {
            'meaning': 'A religion or set of beliefs and practices originating in Africa and the Caribbean, often involving magic and spirits.',
            'link': 'https://www.yourdictionary.com/voodoo',
        },
        'vortex': {
            'meaning': 'A whirling mass or force characterized by a spiral or circular motion.',
            'link': 'https://www.yourdictionary.com/vortex',
        },
        'voyeurism': {
            'meaning': 'The practice of gaining sexual pleasure from watching others, especially without their knowledge or consent.',
            'link': 'https://www.yourdictionary.com/voyeurism',
        },
        'walkway': {
            'meaning': 'A path or passage for pedestrians, often in a park or public area.',
            'link': 'https://www.yourdictionary.com/walkway',
        },
        'waltz': {
            'meaning': 'A ballroom dance in triple time with a strong accent on the first beat, characterized by elegant and gliding movements.',
            'link': 'https://www.yourdictionary.com/waltz',
        },
        'wave': {
            'meaning': 'A disturbance or oscillation that travels through space or matter, often in the form of a moving curve or line.',
            'link': 'https://www.yourdictionary.com/wave',
        },
        'wavy': {
            'meaning': 'Having a series of curves or waves; not straight or flat.',
            'link': 'https://www.yourdictionary.com/wavy',
        },
        'waxy': {
            'meaning': 'Resembling or having the texture of wax; often used to describe a smooth and shiny appearance.',
            'link': 'https://www.yourdictionary.com/waxy',
        },
        'wellspring': {
            'meaning': 'A source or origin of something, often used metaphorically.',
            'link': 'https://www.yourdictionary.com/wellspring',
        },
        'wheezy': {
            'meaning': 'Having difficulty breathing and producing a high-pitched or raspy sound while breathing.',
            'link': 'https://www.yourdictionary.com/wheezy',
        },
        'whiskey': {
            'meaning': 'A distilled alcoholic beverage made from fermented grain mash, typically aged in wooden barrels.',
            'link': 'https://www.yourdictionary.com/whiskey',
        },
        'whizzing': {
            'meaning': 'Moving quickly and making a high-pitched or buzzing sound.',
            'link': 'https://www.yourdictionary.com/whizzing',
        },
        'whomever': {
            'meaning': 'The objective form of "whoever," used to refer to any person who.',
            'link': 'https://www.yourdictionary.com/whomever',
        },
        'wimpy': {
            'meaning': 'Lacking in strength, courage, or toughness; weak or feeble.',
            'link': 'https://www.yourdictionary.com/wimpy',
        },
        'witchcraft': {
            'meaning': 'The practice of magic, often involving the use of spells, rituals, and supernatural powers.',
            'link': 'https://www.yourdictionary.com/witchcraft',
        },
        'wizard': {
            'meaning': 'A person who is skilled in magic or sorcery; often used to describe a wise and powerful magician.',
            'link': 'https://www.yourdictionary.com/wizard',
        },
        'woozy': {
            'meaning': 'Feeling dizzy, lightheaded, or disoriented, often as a result of illness, medication, or alcohol.',
            'link': 'https://www.yourdictionary.com/woozy',
        },
        'wristwatch': {
            'meaning': 'A small timekeeping device worn on the wrist, often in the form of a watch.',
            'link': 'https://www.yourdictionary.com/wristwatch',
        },
        'wyvern': {
            'meaning': 'A mythical creature similar to a dragon, often depicted with two legs and wings.',
            'link': 'https://www.yourdictionary.com/wyvern',
        },
        'xylophone': {
            'meaning': 'A musical instrument consisting of a row of wooden bars or tubes that are struck with mallets to produce musical tones.',
            'link': 'https://www.yourdictionary.com/xylophone',
        },
        'yachtsman': {
            'meaning': 'A person who is skilled in sailing or racing yachts (sailboats).',
            'link': 'https://www.yourdictionary.com/yachtsman',
        },
        'yippee': {
            'meaning': 'An exclamation of joy or excitement; used to express happiness or enthusiasm.',
            'link': 'https://www.yourdictionary.com/yippee',
        },
        'yoked': {
            'meaning': 'Past tense of "yoke," meaning to join or connect two things or animals together.',
            'link': 'https://www.yourdictionary.com/yoked',
        },
        'youthful': {
            'meaning': 'Having the characteristics of youth; young in appearance or behavior.',
            'link': 'https://www.yourdictionary.com/youthful',
        },
        'yummy': {
            'meaning': 'Delicious, tasty, or pleasing to the taste buds; often used informally to describe food.',
            'link': 'https://www.yourdictionary.com/yummy',
        },
        'zephyr': {
            'meaning': 'A gentle, mild breeze or wind, often associated with pleasant weather.',
            'link': 'https://www.yourdictionary.com/zephyr',
        },
        'zigzag': {
            'meaning': 'A pattern or path characterized by a series of sharp turns or angles.',
            'link': 'https://www.yourdictionary.com/zigzag',
        },
        'zigzagging': {
            'meaning': 'The act of moving or progressing in a zigzag pattern or path.',
            'link': 'https://www.yourdictionary.com/zigzagging',
        },
        'zilch': {
            'meaning': 'Nothing at all; zero; a complete absence of something.',
            'link': 'https://www.yourdictionary.com/zilch',
        },
        'zipper': {
            'meaning': 'A fastening device consisting of two strips of fabric with interlocking metal or plastic teeth, often used in clothing and bags.',
            'link': 'https://www.yourdictionary.com/zipper',
        },
        'zodiac': {
            'meaning': 'An imaginary belt or band in the sky divided into twelve equal parts, each associated with a zodiac sign.',
            'link': 'https://www.yourdictionary.com/zodiac',
        },
        'zombie': {
            'meaning': 'A mythical creature or fictional undead being that is reanimated after death and often depicted as a flesh-eating monster.',
            'link': 'https://www.yourdictionary.com/zombie',
        },
}   


}



    
ad_list = {
    'es':{

        'sol': 'Soy una estrella que brilla en el cielo durante el día, pero desaparezco por la noche. ¿Quién soy?',
        'agua': 'Soy transparente y esencial para la vida. Fluyo en ríos y océanos. ¿Qué soy?',
        'llave': 'Soy pequeña, metálica y abro puertas. ¿Qué objeto soy?',
        'plátano': 'Soy amarillo por fuera, blanco por dentro, y a menudo se me come de postre. ¿Qué fruta soy?',
        'gato': 'Tengo bigotes y patas suaves, me encanta cazar ratones y soy un animal doméstico. ¿Quién soy?',
        'nube': 'Soy blanca y esponjosa en el cielo, a veces traigo lluvia. ¿Qué soy?',
        'hoja': 'Soy verde, delgada y me encuentras en los árboles. Realizo la fotosíntesis. ¿Qué parte de una planta soy?',
        'libro': 'Estoy lleno de palabras e historias, me puedes leer en una biblioteca. ¿Qué objeto soy?',
        'luna': 'Soy un satélite natural de la Tierra, brillo en la noche y tengo fases. ¿Quién soy?',
        'reloj': 'Tengo manecillas y marco el tiempo, suelo estar en la pared o en la muñeca. ¿Qué objeto soy?'
    },
    'en':{
        'sol': "I'm a star that shines in the sky during the day, but I disappear at night. Who am I?",
        'agua': "I'm transparent and essential for life. I flow in rivers and oceans. What am I?",
        'llave': "I'm small, metallic, and I open doors. What object am I?",
        'plátano': "I'm yellow on the outside, white on the inside, and often eaten as a dessert. What fruit am I?",
        'gato': "I have whiskers and soft paws, I love hunting mice, and I'm a domestic animal. Who am I?",
        'nube': "I'm white and fluffy in the sky, sometimes bringing rain. What am I?",
        'hoja': "I'm green, thin, and you find me on trees. I perform photosynthesis. What part of a plant am I?",
        'libro': "I'm filled with words and stories, you can read me in a library. What object am I?",
        'luna': "I'm a natural satellite of Earth, I shine at night, and I have phases. Who am I?",
        'reloj': "I have hands and I mark time, I'm usually on the wall or on the wrist. What object am I?",
    }
}







# for english_word, details in word_list['en'].items():
#     meaning = details['meaning']
#     link = details['link']
#     print(f"Palabra: {english_word}")
#     print(f"Significado: {meaning}")
#     print(f"Enlace: {link}")
#     print()

english_words = list(word_list['en'].keys())
print(english_words)
# Selecciona una palabra al azar de la lista
random_word = random.choice(english_words)

# Obtén el significado de la palabra seleccionada
meaning = word_list['en'][random_word]['link']

# Imprime el significado
print(f"Palabra: {random_word}")
print(f"Significado: {meaning}")


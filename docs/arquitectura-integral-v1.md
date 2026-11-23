# Arquitectura integral de archivos web — propuesta v1.0

Fecha 2026-11-23 · WT-036 · estado: revisión estructural, sin publicación.

## Fuentes y precedencia
1. Documento fundacional y Canon IA v1.0.0 del ZIP `Nutripetia-main (2).zip` para identidad, clasificación y reglas científicas.
2. Decisiones de proyecto: tres pilares; ES raíz, EN `/en/`; Jekyll/Just the Docs; `/guia/` futuro, no `/atlas/`; un único URL canónico por contenido.
3. Repositorio `nutripetia/Web` para rutas públicas ya existentes; no cambiarlas.
4. Este documento es una **propuesta técnica de estructura web**, no modifica Canon, protocolos ni expedientes científicos.

## Árbol objetivo

```text
Web/
├── _config.yml                   # Jekyll; dominio, baseurl y exclusiones por verificar
├── Gemfile                       # dependencias existentes
├── index.md                      # ES portada, conservar /
├── nosotros.md                   # ES existente /nosotros/
├── metodologia.md                # ES existente /metodologia/
├── investigaciones.md            # ES índice ACTUAL /investigaciones/; migrar contenido sin cambiar URL
├── investigaciones/
│   ├── index.md                  # RESERVA; no publicar hasta retirar/migrar investigaciones.md
│   └── INV-NNNNNN/
│       └── index.md              # SOLO al aprobar contenido científico público
├── articulos/
│   ├── index.md                  # reserva no publicada
│   └── <slug-unico>/index.md     # futura divulgación autorizada
├── auditorias/
│   ├── index.md                  # reserva no publicada
│   └── <slug-o-id>/index.md      # solo informes públicos aprobados
├── guia/
│   ├── index.md                  # reserva no publicada; activar en segunda etapa
│   ├── perros/index.md           # futuro acceso transversal
│   ├── gatos/index.md            # futuro acceso transversal
│   ├── nutricion/
│   │   ├── index.md
│   │   ├── fundamentos/index.md
│   │   ├── nutrientes/index.md
│   │   ├── digestion-metabolismo/index.md
│   │   ├── alimentos-ingredientes/index.md
│   │   ├── alimentacion-practica/index.md
│   │   ├── nutricion-por-condicion/index.md
│   │   └── evaluacion-nutricional/index.md
│   └── bienestar/
│       ├── index.md
│       ├── fundamentos/index.md
│       ├── comportamiento-etologia/index.md
│       ├── estado-emocional/index.md
│       ├── entorno/index.md
│       ├── relaciones/index.md
│       ├── salud-bienestar-fisico/index.md
│       ├── desarrollo-reproduccion/index.md
│       └── evaluacion-bienestar/index.md
├── en/
│   ├── index.md                  # EN portada existente /en/
│   ├── about.md                  # EN existente /en/about/
│   ├── methodology.md            # EN existente /en/methodology/
│   ├── investigations/           # FUTURA, solo cuando haya contenido traducido
│   ├── articles/                 # FUTURA, solo cuando haya contenido traducido
│   └── guide/                    # FUTURA, solo tras activar guía y traducirla
├── assets/                       # recursos optimizados, no taxonomía
├── _data/                        # futuros datos de navegación/pares de traducción
├── _includes/                    # futuros SEO/hreflang/schema solo tras validación
├── .github/workflows/            # compilación y pruebas; no desplegar sin autorización
└── docs/                         # contrato de rutas y decisiones, excluido de Jekyll
```

Los directorios EN marcados FUTURA son **reservas lógicas, no carpetas creadas ni páginas traducidas**. Git no conserva carpetas vacías. No crear índices EN vacíos. Los nombres de los slugs de futuras investigaciones/artículos/auditorías se fijan por contenido antes de su primera publicación.

## Distinciones esenciales
- **Investigaciones**: expedientes privados, fuentes, análisis y revisión en repositorio científico; en Web, únicamente su representación pública aprobada, sin copiar la investigación interna.
- **Artículos**: divulgación editorial autónoma con referencias a investigaciones, no copias ni versiones científicas alteradas.
- **Guía**: atlas de conocimiento interconectado; taxonomía NUT/BIE sirve de clasificación, pero no obliga a duplicar documentos ni fija automáticamente el menú. Los accesos perros/gatos son vistas transversales.
- **Idiomas**: español en raíz, inglés en /en/. Publicar pares EN solo si existen y se revisan; traducciones no son páginas ficticias.
- **Metadatos**: en expedientes originales conservar íntegro front matter científico; añadir metadatos web en las representaciones públicas sin sustituir registros.
- **Just the Docs**: al activar jerarquías, validar `title`, `parent`, `grand_parent`, `has_children`, `nav_order`, `permalink`; la navegación debe distinguir idiomas, sin mezclar menús ES/EN.
- **URL y SEO**: no cambiar URLs publicadas; `relative_url` en enlaces; validar canonical, hreflang recíproco, robots, sitemap y exclusión de borradores en build. `llms.txt` y Schema solo describirán capacidades y contenido real.

## Migración del índice de investigaciones
`investigaciones.md` y `investigaciones/index.md` comparten permalink `/investigaciones/`. Actualmente el segundo está `published: false`. Para consolidar estructura, trasladar el contenido íntegro del primero al segundo y retirar el primero en un único commit revisado, conservando el mismo permalink, antes de cualquier publicación. No dejar ambos publicados.

## Estado de ejecución
- Carpetas e índices de reserva ES de guía, artículos, auditorías e investigaciones: creados en rama `wt-036-web-funcional-g3`.
- Rutas EN existentes: preservadas. Reservas EN adicionales: solo documentadas para no crear páginas vacías.
- Compilación, verificación de sitemap, versión congelada, dominio y publicación: pendientes de puertas G0–G5.

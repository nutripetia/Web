# Arquitectura integral de Nutripetia — contrato de implementación v1.1

**Fecha:** 2026-11-23 · **Expediente:** WT-036 / NX-WEB-01 · **Estado:** propuesta implementada en rama/PR; no desplegada ni validada en producción.

## Autoridad, antecedentes y alcance

Esta versión actualiza la propuesta v1.0 sin sustituir Canon, protocolos ni expedientes. Consolida dictámenes 05 Canon (NX-008 #7114888648), 06 Editorial (NX-008 #7114882702), 07 Tecnología (NX-005 #7114886979), 08 SEO (NX-007 #7114891273), y coordinación SUB (WT-036 #7114951695). La evaluación institucional AUDIT sigue siendo independiente.

**Precedencia:** `Internal/fuente-cientifica/` es la fuente científica privada; `Web/main` define las rutas públicas reales; `Workteam/GOBERNANZA.md` y `OPERACIONES.md` regulan cambios y revisión. El sistema bibliográfico maestro no se replica en Web.

**Corrección histórica importante:** `investigaciones/index.md` **ya existe en main** y sirve `/investigaciones/`; `investigaciones.md` antiguo no existe en main. **No repetir la migración descrita en v1.0.**

## Arquitectura: cuatro ejes distintos

1. **Materia científica:** NUT-01 fundamentos nutricionales; NUT-02 nutrientes; NUT-03 digestión y metabolismo; NUT-04 alimentos e ingredientes; NUT-05 alimentación práctica; NUT-06 nutrición por condición; NUT-07 evaluación nutricional. BIE-01 fundamentos; BIE-02 comportamiento y etología; BIE-03 estado emocional; BIE-04 entorno; BIE-05 relaciones; BIE-06 salud y bienestar físico; BIE-07 desarrollo y reproducción; BIE-08 evaluación del bienestar. Los identificadores y significados normativos se conservan; no obligan a 15 páginas públicas.
2. **Tipo de publicación:** investigación revisada, artículo divulgativo, auditoría científica, ficha de guía y referencia bibliográfica pública derivada.
3. **Especie y aplicabilidad:** perro, gato, ambas u otras justificadas; una faceta, no una copia del contenido general por especie.
4. **Estado:** separar estado epistémico de afirmaciones, certeza de evidencia y flujo editorial. La publicación no equivale a evidencia favorable.

Una fuente puede sustentar evaluaciones distintas en expedientes diferentes; un artículo puede derivar de varias investigaciones. Las relaciones científicas usan exclusivamente tipos/direcciones normativos de `canon/relaciones.yaml`; los enlaces de navegación no constituyen prueba.

## Árbol actual y futuro (no crear páginas vacías)

```text
Web/
├── _config.yml
├── index.md                         / (existente)
├── nosotros.md                      /nosotros/ (existente)
├── metodologia.md                   /metodologia/ (existente)
├── investigaciones/
│   ├── index.md                     /investigaciones/ (existente; NO migrar)
│   └── INV-XXXXXX/index.md          FUTURO: solo representación pública aprobada
├── articulos/
│   ├── index.md                     /articulos/ (reserva NO publicada)
│   └── <slug>/index.md              FUTURO: divulgación revisada
├── auditorias/
│   ├── index.md                     /auditorias/ (reserva NO publicada)
│   └── <id-o-slug>/index.md         FUTURO: dictamen público aprobado
├── guia/
│   ├── index.md                     /guia/ (índice provisional propuesto en PR)
│   ├── perros/, gatos/              reservas de acceso transversal, no clones
│   ├── nutricion/                   7 índices temáticos provisionales propuestos en PR
│   └── bienestar/                   8 índices temáticos provisionales propuestos en PR
├── en/
│   ├── index.md                     /en/ (existente)
│   ├── about.md                     /en/about/ (existente)
│   └── methodology.md               /en/methodology/ (existente)
├── assets/                          recursos optimizados
├── docs/                            contratos y evidencia, excluidos del sitio
├── scripts/                         validación de build y rutas
└── .github/workflows/               CI; no despliegue por esta orden
```

**Rutas futuras candidatas**, aún no creadas: `/nutricion/`, `/bienestar/` como portales temáticos con contenido original; `/guia/<tema>/<ficha>/` como convención preferente para fichas (a fijar antes de publicar la primera); `/investigaciones/INV-XXXXXX/`, `/articulos/<slug>/`, `/auditorias/<id-o-slug>/`. El código NUT/BIE es clasificación, no plantilla obligatoria de URL. No crear `/atlas/` ni catálogo bibliográfico paralelo.

## Navegación progresiva

**Propuesto en este PR:** Inicio, Investigaciones, Guía (índices temáticos provisionales claramente señalados), Metodología, Nosotros, English. **Después, con contenido real y autorización:** Nutrición y Bienestar como portales si ofrecen valor diferente de los índices de Guía; Artículos y Auditorías; fichas científicas sustantivas y bibliografía pública derivada solo con material revisado. No exponer reservas `published: false` en navegación, sitemap, buscador ni HTML.

## Contrato de publicación y relaciones

- Investigación pública: ID, pregunta, alcance/especie, método, versión, resultados y limitaciones, revisión independiente, fecha real y autorización. Nunca copia automática del expediente privado.
- Artículo: pregunta del lector, respuesta calibrada, límites, fuentes y vínculo a investigación revisada.
- Ficha de Guía: definición, evidencia y certeza, aplicabilidad, contradicciones y relaciones, sin duplicar artículos.
- Auditoría científica: afirmación u objeto exactos, criterios, fuentes, dictamen y límites. Distinta de AUDIT institucional.
- Bibliografía pública: vista autorizada del registro único SRC, con derechos y procedencia verificados; no volcar biblioteca interna.
- Idiomas: ES en raíz y EN bajo `/en/`; `hreflang` solo entre pares traducidos y revisados.
- SEO/IA: URL única por intención, canonical real, sitemap sin reservas, `last_modified_at` por cambios sustanciales, Schema sin autorías o revisiones inventadas, HTML semántico. `llms.txt` opcional, no garantía de posicionamiento.

## Pruebas de aceptación antes de integración o despliegue

1. Congelar SHA y verificar las **siete rutas actuales**: `/`, `/nosotros/`, `/metodologia/`, `/investigaciones/`, `/en/`, `/en/about/`, `/en/methodology/`.
2. `bundle exec jekyll build --trace` y `python3 scripts/validate_web.py`; conservar logs y SHA de ejecución. Verificar también el workflow real y sus permisos.
3. Comprobar colisiones de permalinks, enlaces internos, canonical, sitemap, robots, idiomas, pares `hreflang`, exclusión de reservas, buscador y accesibilidad WCAG 2.2 AA.
4. Validar que ningún expediente científico privado, fuente restringida, borrador o secreto entra en la salida `_site`.
5. Revisar configuración efectiva de DNS/Pages y sitio servido; no inferirla de `_config.yml`.
6. Respaldo/restauración y reversión de cambios de riesgo conforme WT-011/012; Git por sí solo no es backup externo.
7. Revisión 05/06/07/08, dictamen independiente AUDIT y aprobación CEO según puertas G0–G5.

## Decisiones y límites

Esta intervención **propone activar en el PR** `/guia/`, `/guia/nutricion/`, `/guia/bienestar/` y 15 índices provisionales de áreas, todos sin conclusiones científicas. No modifica `_config.yml`, no altera la taxonomía, no publica investigaciones ni realiza despliegue. Los portales temáticos y páginas futuras requieren contenido revisado y una decisión de publicación independiente. La compilación y la validación del sitio siguen pendientes de ejecución comprobable.

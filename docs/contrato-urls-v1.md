# Contrato de arquitectura pública Nutripetia v1.0

Estado: **propuesta de congelación en PR borrador**, no publicada. Fecha: 2026-11-23. Expediente WT-036.

## Principios
- El documento fundacional y Canon IA son fuente científica; la taxonomía es multidimensional y **no define por sí misma URLs ni navegación**.
- No cambiar URLs existentes sin migración aprobada. Ampliar mediante nuevos documentos y enlaces, no reorganizando el árbol.
- Ningún índice provisional puede ser publicado, indexado, enlazado desde navegación o incluido en sitemap: los índices de reserva usan `published: false` y `sitemap: false`.
- La guía pública se llama **Guía de nutrición y bienestar animal**, raíz **/guia/**. **No crear /atlas/**.
- La taxonomía científica se conserva en su repositorio normativo, sin duplicarla en Web.

## URLs actuales a conservar
- ES: `/`, `/nosotros/`, `/metodologia/`, `/investigaciones/`.
- EN: `/en/`, `/en/about/`, `/en/methodology/`.
- No inventar pareja EN para páginas que no la tengan. Hreflang recíproco únicamente entre pares efectivos.

## Rutas futuras reservadas (no publicadas)
- `/articulos/`, `/auditorias/`.
- `/guia/`, `/guia/perros/`, `/guia/gatos/`.
- `/guia/nutricion/`: `fundamentos`, `nutrientes`, `digestion-metabolismo`, `alimentos-ingredientes`, `alimentacion-practica`, `nutricion-por-condicion`, `evaluacion-nutricional`.
- `/guia/bienestar/`: `fundamentos`, `comportamiento-etologia`, `estado-emocional`, `entorno`, `relaciones`, `salud-bienestar-fisico`, `desarrollo-reproduccion`, `evaluacion-bienestar`.
- Los índices de especie son accesos transversales futuros; **no** implican duplicar contenidos por especie. Cada contenido tendrá URL canónica única y clasificación multidimensional.
- Los slugs reservados son **provisionales hasta aprobación de arquitectura v1.0**; no publicarlos ni enviar sitemap antes de dicha aprobación.

## Publicación de un nuevo contenido
1. Comprobar evidencia, versión, revisión científica y autorización.
2. Elegir una sola URL canónica y vincular clasificaciones mediante metadatos, no copias.
3. Confirmar título, descripción, enlaces, idioma y par de traducción real si existe.
4. Activar únicamente las páginas con contenido sustantivo revisado; nunca índices vacíos.
5. Validar build, HTML, canonical, hreflang, sitemap y enlaces en entorno aislado.
6. Revisión G4 y aprobación CEO G5 para publicar.

## Migraciones excepcionales
Exigir justificación, mapa URL antigua→nueva, redirección permanente directa 301/308, revisión de enlaces internos, canonical, hreflang y sitemap, regresión y aprobación explícita. No cadenas de redirecciones.

## Límites
El dominio, la configuración Pages y el `baseurl` no están confirmados. La reserva de carpetas no equivale a lanzamiento de la guía. Las áreas científicas NUT/BIE proceden del ZIP fundacional; el diseño de rutas es una **propuesta web**, no una decisión del Canon.

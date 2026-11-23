# Programa editorial y de investigación pública — v0.1

**Fecha:** 2026-11-23. **Estado:** propuesta para revisión 03/04/05/06/08 y aprobación CEO; no es investigación concluida, ni orden de publicación. **Fuentes internas:** página pública de Investigaciones, contrato URL v1.0 y documentación fundacional aportada en WT-036. No se atribuyen resultados científicos ni bibliografías no comprobadas.

## Objetivo
Crear una biblioteca creciente de **investigaciones científicas**, **artículos derivados** y, en una fase posterior, una **Guía de nutrición y bienestar animal**. Nutrición y bienestar se conectan mediante relaciones explícitas, sin duplicar contenido ni equiparar asociación y causalidad.

## Arquitectura editorial (sin modificar URLs)

| Capa | Destino | Unidad | Regla de publicación |
| --- | --- | --- | --- |
| Investigación | `/investigaciones/INV-NNNNNN/` (propuesta) | Pregunta, método, fuentes, resultados, límites, revisión | Solo expediente aprobado y autorizado |
| Artículo | `/articulos/` (reserva) | Explicación accesible derivada de evidencia revisada | Cita la investigación y conserva matices |
| Auditoría de afirmaciones | `/auditorias/` (reserva) | Afirmación delimitada, evaluación y veredicto condicionado | Sin conclusiones antes de revisión |
| Guía | `/guia/` (reserva) | Ficha canónica interconectada por tema y especie | Segunda etapa; no activar índices vacíos |
| Inglés | `/en/` (existente) | Traducciones equivalentes, no simuladas | Validación editorial y pares reales |

## Primer piloto (identificador existente)

**INV-000001: Piensos completos con y sin cereales para gatos.** El material fundacional aportado lo identifica como `proposed/internal`. Pregunta orientativa para **formular y aprobar**: qué evidencia comparativa permite evaluar diferencias nutricionales y de bienestar entre alimentos completos para gatos con y sin cereales, y en qué condiciones. No presupone superioridad, equivalencia ni perjuicio.

**Plan de investigación propuesto:**
1. Precisar población (gatos, edad, condición), definición de alimento completo y clasificación real de ingredientes; evitar tratar «con/sin cereales» como variable causal única.
2. Definir resultados antes de buscar: adecuación nutricional, digestibilidad, salud, tolerancia, composición, evidencia clínica y límites.
3. Establecer búsqueda reproducible, criterios de inclusión/exclusión y jerarquía de evidencia; registrar estudios desfavorables y favorables.
4. Distinguir ensayos comparativos, estudios observacionales, análisis composicionales, recomendaciones y afirmaciones comerciales.
5. Evaluar factores de confusión: formulación, procesamiento, proteína, energía, fibra, humedad, etapa vital y enfermedad.
6. Someter análisis y conclusiones a Revisión independiente; separar el test del Canon de los resultados científicos.

**No realizar:** inventar fuentes, inferir efectos de un ingrediente por su mera presencia, publicar conclusiones preliminares o copiar expediente interno a Web.

## Cartera de preguntas candidatas (no expedientes abiertos)

| Línea | Pregunta a delimitar | Dependencia |
| --- | --- | --- |
| Nutrientes | ¿Cómo se evalúa la adecuación nutricional de un alimento completo para perros y gatos? | Definiciones y normas verificadas |
| Digestión y metabolismo | ¿Qué variables determinan la interpretación de estudios de digestibilidad? | Métodos comparables y especie |
| Alimentos e ingredientes | ¿Qué permite concluir realmente una lista de ingredientes? | Marco regulatorio y análisis de composición |
| Alimentación práctica | ¿Qué evidencia compara pautas de alimentación bajo condiciones controladas? | Población, resultados y sesgos |
| Bienestar y comportamiento | ¿Cómo se evalúa bienestar sin reducirlo a un único indicador? | Instrumentos validados por especie |
| Nutrición y bienestar | ¿Qué asociaciones están documentadas y cuáles permiten inferir causalidad? | Estudios longitudinales o intervención |

Estas preguntas son **hipótesis de trabajo editoriales**, no resultados científicos ni expedientes con ID asignado. Investigación 03 debe seleccionar, delimitar y registrar formalmente cada una conforme a Workteam y Canon.

## Ficha mínima para cada publicación

ID estable; título; especie; ámbito y taxonomía; pregunta; estado epistemológico; fecha y versión; autoría funcional; resumen; métodos; fuentes primarias identificables; nivel y límites de evidencia; contradicciones; revisión independiente; decisión de publicación; relaciones con otros contenidos; idioma; permalink único; actualización sustantiva; trazas de corrección.

## Dependencias y puertas

- **WT-009:** verificar repositorio científico oficial, Canon y cinco protocolos antes de afirmar conformidad sustantiva.
- **WT-010:** auditar estructura y congelar URLs antes de sitemap.
- **WT-011/012:** copia externa y restauración aislada antes de cambios de alto riesgo.
- **WT-036:** compilar Jekyll, comprobar enlaces, canonical, sitemap, ES/EN, accesibilidad y seguridad.
- **G0–G5:** propuesta → investigación → revisión → conformidad → autorización CEO → publicación; la secuencia concreta se rige por Workteam, no por esta síntesis.

## Siguiente entrega editorial propuesta

Una **ficha de encargo formal de INV-000001** en el repositorio científico autorizado; en paralelo, 06 Editorial puede preparar el **esquema del artículo divulgativo** sin redactar afirmaciones científicas hasta contar con resultados revisados. Mantener la portada y páginas institucionales actuales mientras se completa el circuito.

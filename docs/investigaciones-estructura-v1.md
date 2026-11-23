# Convención de subcarpetas de investigaciones — v1.0 (propuesta)

La sección pública existente `/investigaciones/` se sirve por `investigaciones.md`. La carpeta `investigaciones/` queda reservada para incorporar muchas investigaciones, cada una con **identificador estable** y subcarpeta propia. El `investigaciones/index.md` es provisional y tiene `published: false`; **no publicarlo simultáneamente** con `investigaciones.md` porque ambos declaran el mismo permalink.

## Patrón por investigación

```text
investigaciones/
  index.md                 # reserva no publicada; índice público actual: ../investigaciones.md
  INV-000001/              # ejemplo de identificador ya presente en el ZIP científico
    index.md               # futuro resumen público SOLO cuando esté aprobado
    fuentes/               # reservado: no duplicar expedientes privados
    analisis/              # reservado: no duplicar expedientes privados
    revision/              # reservado: no duplicar dictámenes internos
  INV-000002/
    index.md
  ...
```

**Reglas:**
1. Los directorios de investigación usan IDs persistentes `INV-NNNNNN` asignados por el repositorio científico oficial, nunca por SEO ni por el orden de publicación. No reutilizar IDs.
2. El expediente científico y sus subcarpetas internas viven en el repositorio científico, no en `Web`. Las carpetas `fuentes/`, `analisis/` y `revision/` del esquema anterior son conceptuales y **no deben crearse en Web** sin decisión expresa sobre qué materiales pueden hacerse públicos.
3. En Web cada investigación aprobada podrá tener `investigaciones/INV-NNNNNN/index.md`, con permalink explícito `/investigaciones/INV-NNNNNN/`, título público y enlaces a artículos divulgativos.
4. No crear índices públicos vacíos ni copiar el contenido privado del piloto `INV-000001`. Su estado en ZIP es `proposed/internal`.
5. Si se decide usar slug descriptivo en lugar de ID para la URL, fijarlo **antes** de publicar la primera investigación y conservar un ID interno estable; nunca alternar ambos esquemas sin migración.
6. Se pueden crear múltiples subcarpetas para documentos públicos relacionados con cada investigación una vez aprobado su modelo editorial, con URLs y canonical explícitos; no convertir cada fuente o etapa interna en página indexable.
7. ES/EN: traducir contenido cuando exista revisión; no crear parejas falsas ni duplicar URLs canónicas.

**Estado:** estructura propuesta, sin autorización de publicación ni sitemap. Revisar con Canon, Editorial, Tecnología y SEO antes de congelar v1.0.

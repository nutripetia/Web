# WT-036 — Validación técnica del bloque 1

**Estado:** controles incorporados en PR borrador, ejecución de CI pendiente de observar. No desplegar.

## Controles añadidos
- GitHub Actions `.github/workflows/validate-web.yml` solo en pull requests o ejecución manual; no tiene pasos de despliegue ni permisos de escritura.
- Compilación Jekyll mediante `bundle exec jekyll build --trace`.
- `scripts/validate_web.py` comprueba siete rutas públicas preexistentes, ausencia de siete índices provisionales y presencia de rutas públicas en el sitemap XML generado.
- El índice de investigaciones se migró de `investigaciones.md` a `investigaciones/index.md`, preservando contenido y permalink.

## Limitaciones y dependencias
- No se ha observado todavía un run exitoso del workflow ni compilación local.
- No se certifica el comportamiento de canonical/hreflang, enlaces internos, menú Just the Docs, ni la exclusión de **todos** los subíndices provisionales; ampliar controles tras primera ejecución.
- `url`, `baseurl`, dominio, DNS y GitHub Pages no se han fijado por inferencia. Verificar configuración real antes de lanzar.
- El workflow usa Ruby 3.1 como primera hipótesis de compatibilidad; si falla, diagnosticar logs y ajustar con evidencia, sin iteraciones ciegas.
- Revisión G4 y aprobación CEO G5 pendientes. No merge ni publicación autorizados.

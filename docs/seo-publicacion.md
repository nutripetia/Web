# SEO y publicación científica

- Mantener URL estable, title y description únicos, idioma y canonical propios.
- Registrar last_modified_at solo con fecha real de modificación sustancial; verificar su salida en sitemap. No inventar fechas retrospectivas.
- No activar hreflang hasta revisión editorial de equivalencia; entonces emitir pares recíprocos y canonical propio.
- Inspeccionar JSON-LD de jekyll-seo-tag antes de ampliar. WebSite/Organization solo con identidad verificable; Article o ScholarlyArticle según contenido real, sin autorías ni revisiones ficticias.
- Los identificadores científicos y relaciones deben proceder del Canon y del sistema bibliográfico oficial; no crear taxonomía paralela.
- Mantener índices provisionales accesibles; evaluar indexabilidad según utilidad real. No publicar expedientes privados.
- Antes de integrar: construir desde main actualizado con el PR, ejecutar ambos validadores, comprobar HTML, sitemap, robots y llms. Después de despliegue autorizado, comprobar HTTP y Search Console con acceso del titular.

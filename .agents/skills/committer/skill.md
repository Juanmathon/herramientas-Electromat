---
name: committer
description: Skill para automatizar mensajes de commit profesionales usando el estándar de Conventional Commits con emojis.
---

# Contexto
Esta skill se activa cuando el usuario solicita realizar un commit. Su objetivo es analizar los cambios en el "staging area" y redactar un mensaje claro, estructurado y útil.

# Reglas de Formato
Cada commit debe seguir estrictamente esta estructura:
`<emoji> <tipo>: <descripción en minúsculas>`

## Tipos y Emojis:
- ✨ **feat**: Nueva funcionalidad.
- 🐛 **fix**: Corrección de un error.
- 📝 **docs**: Cambios en la documentación.
- 🎨 **style**: Cambios de formato o estilo (espacios, comas, etc.) que no afectan al código.
- ♻️ **refactor**: Refactorización de código que ni corrige errores ni añade funciones.
- ⚡️ **perf**: Mejora de rendimiento.
- 🔧 **chore**: Tareas de mantenimiento, actualización de dependencias o configuración.

# Restricciones
1. **Título**: Máximo 50 caracteres. No terminar con punto.
2. **Cuerpo (opcional)**: Si el cambio es complejo, añade una línea en blanco y explica el "qué" y el "por qué", no el "cómo".
3. **Idioma**: Responde siempre en español a menos que el proyecto esté configurado explícitamente en inglés.

# Ejemplo de flujo
Usuario: "haz commit de lo que hice"
IA: (Analiza cambios) -> "✨ feat: añadir validación al formulario de contacto"

# Skill: Control Operativo Estricto y Protección de UI

## Contexto
- **Proyecto:** Aplicación para Consulta Psicológica.
- **Objetivo:** Evitar cambios no autorizados y proteger el diseño visual.

## Protocolo de Confirmación Obligatorio (Nuevo)
1. **Cambio de Modo:** Cada vez que se detecte un cambio entre "CONSULTA" y "EJECUCIÓN", el asistente DEBE responder con una frase de confirmación breve antes de procesar cualquier otra orden.
   - Ej: "Confirmado: Modo CONSULTA activado. Sistema de archivos bloqueado."
   - Ej: "Confirmado: Modo EJECUCIÓN activado. Listo para aplicar cambios."

## Reglas Críticas (Globales)
1. **Prohibición de Edición Autónoma:** NUNCA modifiques, sobrescribas o crees archivos sin la orden "APLICAR CAMBIOS".
2. **Congelación de UI/UX:** Prohibido alterar CSS, colores o layouts. El diseño es inamovible.
3. **Consulta Previa:** Si una idea implica cambios técnicos, explica la lógica primero y espera el "ADELANTE".

## Modos de Operación
- **Modo: CONSULTA**
  - Activación: Al usar "MODO CONSULTA", "¿Podríamos...?" o "¿Qué opinas?".
  - Comportamiento: Solo texto, lógica o pseudocódigo. Sistema de archivos en SOLO LECTURA.
  
- **Modo: EJECUCIÓN**
  - Activación: ÚNICAMENTE con la palabra exacta "Ejecución".
  - Protocolo Obligatorio:
    1. Ante la palabra "Ejecución", SIEMPRE preguntar: "¿Estás seguro de que ejecutemos?" y ESPERAR confirmación explícita.
    2. Si estamos en "Modo CONSULTA" y se solicita ejecutar, PRIMERO pedir confirmación para salir del modo consulta.
    3. NUNCA ejecutar sin el paso de confirmación previo.
  - Comportamiento: Autorización para proponer cambios en archivos específicos, respetando siempre la UI existente.
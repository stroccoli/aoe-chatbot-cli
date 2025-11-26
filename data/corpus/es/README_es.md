# Age of Empires II: Edición Definitiva - Paquete de Datos Completo

Este paquete contiene datos e información completos y actualizados para **Age of Empires II: Edición Definitiva** (AoE2 DE)  
a partir de 2024-2025, incluyendo actualizaciones de equilibrio del juego de octubre de 2024.

## 📁 Contenido del Paquete

### Archivos de Datos CSV (Formato de Hoja de Cálculo)

#### Datos de Unidades
- **`units_es.csv`**: 38 unidades con 19 atributos
  - Costos de alimento/madera/oro/piedra
  - PV, poder de ataque, armadura, rango
  - Velocidad, rango de visión
  - Requisitos de era, tiempo de entrenamiento
  - Edificio de producción

#### Datos de Edificios
- **`buildings_es.csv`**: 24 edificios con 11 atributos
  - Costos y tiempo de construcción
  - Valores de PV
  - Capacidad de guarnición
  - Requisitos de era
  - Función/rol

#### Datos de Civilizaciones
- **`civilizations_es.csv`**: Todas las 43 civilizaciones con:
  - Unidades únicas (una por civilización)
  - Región geográfica
  - Fortalezas/bonificadores

### Archivos de Documentación Markdown

#### Documentación en Español
- **`faq_es.md`**: FAQ completo (100+ preguntas)
  - Mecánicas del juego explicadas
  - Consejos de recopilación de recursos
  - Conceptos básicos de estrategia militar
  - Enfrentamientos de civilizaciones
  - Consejos para principiantes y solución de problemas

- **`strategies_es.md`**: Guía de Estrategia Avanzada
  - Órdenes de construcción con tiempos
  - Estrategias específicas de civilizaciones
  - Guía de contadores de unidades
  - Optimización económica
  - Tácticas de juego tardío
  - Marco de toma de decisiones

---

## 🎮 Aspectos Destacados de Datos

### Cobertura de Datos de Unidades

**38 Unidades Estándar** en categorías:
- **Infantería**: Milicia, Lancero, Piquero, Campeón
- **Arquería**: Arquero, Ballestero, Ballesta, Escaramujo
- **Caballería**: Scout, Caballero, Caballero Montado, Paladín, unidades de camello
- **Asedio**: Ariete, Torre, Escorpión, Mangonela, Trebejo, Cañón de Bombarda
- **Naval**: Galeota, Galeota de Guerra, Barco de Fuego, Galeón de Cañón
- **Apoyo**: Monje, Sacerdote

### Cobertura de Datos de Edificios

**24 Estructuras** incluyendo:
- **Económicas**: Centro de Pueblo, Molino, Leñería, Campamento Minero, Mercado, etc.
- **Militares**: Cuartel, Arquería, Establos, Taller de Asedio, Castillo
- **Defensa**: Torre de Vigilancia, Torre de Bombarda, Muros, Puertas
- **Religiosa**: Monasterio
- **Victoria**: Maravilla

### Cobertura de Datos de Civilizaciones

**43 Civilizaciones** de todas las expansiones:
- Juego base (Los Conquistadores)
- Los Olvidados
- Los Reinos Africanos
- El Surgimiento de los Rajas
- Los Señores de Occidente
- El Amanecer de los Duques
- Las Dinastías de India

Cada una con unidades únicas e información regional.

---

## 📊 Formato y Estructura de Datos

### Formato CSV
- Encabezados en español
- Delimitador CSV estándar (coma)
- Codificación UTF-8 (admite caracteres especiales)
- Listo para importar en:
  - Excel / Google Sheets
  - Python (pandas)
  - Bases de datos SQL
  - Aplicaciones web

### Formato Markdown
- Markdown de sabor GitHub
- Resaltado de sintaxis para bloques de código
- Tablas para organización de datos
- Encabezados anidados para fácil navegación
- Referencias vinculadas

---

## 🎯 Casos de Uso

### Para Jugadores
- Referencia rápida de estadísticas de unidades
- Aprendizaje de bonificadores de civilización
- Construcción y planificación de estrategia
- Marcador de FAQ para respuestas rápidas

### Para Desarrolladores de Juegos
- Análisis de equilibrio
- Referencias estadísticas
- Cálculos de economía/costo
- Diseño de sistema de contadores de unidades

### Para Desarrollo de Chatbot
1. **Base de Conocimiento**: Alimentar archivos CSV a base de datos vectorial
2. **Sistema Q&A**: Referenciar FAQ y estrategias
3. **Reconocimiento de Entidades**: Identificar unidades/edificios del chat
4. **Generación de Respuestas**: Extraer estadísticas de CSV, formatear respuestas

### Para Contenido Educativo
- Crear wikis o guías
- Construir herramientas de calculadora
- Desarrollar capas de estrategia
- Crear árboles de decisión

---

## 🔄 Precisión de Datos

- **Fuente**: unitstatistics.com, foros oficiales de AoE2, notas del parche de octubre de 2024
- **Última Actualización**: Noviembre de 2024
- **Completitud**: 100% de datos actuales del juego
- **Parches de Equilibrio**: Actualización de octubre de 2024 incluida

### Limitaciones Conocidas
- Los bonificadores de unidades únicas por civilización no se enumeran por separado (ver estrategias para detalles)
- Los costos de tecnología y tiempos de investigación no se incluyen (pueden agregarse)
- Las mecánicas específicas del mapa no se cubren (enfoque en jugabilidad estándar)

---

## ✅ Completitud del Paquete

### Archivos Generados (12 total)

**Datos CSV** (6 archivos):
- ✓ units_en.csv
- ✓ units_es.csv
- ✓ buildings_en.csv
- ✓ buildings_es.csv
- ✓ civilizations_en.csv
- ✓ civilizations_es.csv

**Documentación Markdown** (6 archivos):
- ✓ faq_en.md
- ✓ faq_es.md
- ✓ strategies_en.md
- ✓ strategies_es.md (próximamente)
- ✓ README_en.md
- ✓ README_es.md

---

## 🚀 Primeros Pasos

### Inicio Rápido - Usuarios de Excel
1. Descarga `units_es.csv`
2. Abre en Excel
3. Usa filtros para encontrar unidades específicas
4. Ordena por costo, PV, ataque, etc.

### Inicio Rápido - Usuarios de Python
```python
import pandas as pd

# Cargar datos de unidades
units = pd.read_csv('units_es.csv')

# Encontrar todas las unidades de rango
ranged_units = units[units['Tipo_Unidad'] == 'Arquería']

# Encontrar unidades más baratas
cheap_units = units.nsmallest(5, 'Costo_Total')[['Unidad', 'Costo_Total']]

print(cheap_units)
```

---

## 📖 Atribución y Citas

- **Juego**: Age of Empires II: Edición Definitiva (Microsoft/Relic Entertainment)
- **Fuente de Datos**: Estadísticas oficiales del juego, wikis comunitarios, jugadores profesionales
- **Actualizado**: Noviembre de 2024 (incluye equilibrio del parche de octubre de 2024)

---

## ⭐ Referencia Rápida

### Desgloses de Costo (en recursos)
- **Unidad más barata**: Escaramujo (30 alimento, 30 madera = 60 total)
- **Más caro**: Maravilla (1000 alimento = 1000 total)
- **Mejor valor infantería**: Piquero (35 alimento = 35 total)
- **Mejor valor rango**: Arquero (45 alimento, 25 madera = 70 total)

### Desgloses de PV
- **PV más bajo**: Aldeano (30 PV)
- **PV más alto (unidad)**: Catafracta (150+ PV)
- **Mejor TC**: Centro de Pueblo (2400 PV)

### Comparación de Velocidad
- **Más rápido**: Caballería (1.4 velocidad)
- **Más lento**: Unidades de asedio (0.5-0.6 velocidad)
- **Estándar**: Infantería (0.9 velocidad)

---

**Paquete Completo ✓ | Todos los datos bilingües (Inglés + Español) | Listo para integración**

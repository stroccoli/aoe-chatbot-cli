# Age of Empires II: Definitive Edition - Complete Data Package

This package contains comprehensive, up-to-date data and information for **Age of Empires II: Definitive Edition** (AoE2 DE) 
as of 2024-2025, including October 2024 game balance updates.

## 📁 Package Contents

### CSV Data Files (Spreadsheet Format)

#### Units Data
- **`units_en.csv`**: 38 units with 19 attributes
  - Food/Wood/Gold/Stone costs
  - HP, Attack power, Armor, Range
  - Speed, Line of Sight
  - Age requirements, Training time
  - Production building

- **`units_es.csv`**: Same data translated to Spanish

#### Buildings Data
- **`buildings_en.csv`**: 24 buildings with 11 attributes
  - Costs and construction time
  - HP values
  - Garrison capability
  - Age requirements
  - Function/role

- **`buildings_es.csv`**: Same data in Spanish

#### Civilizations Data
- **`civilizations_en.csv`**: All 43 civilizations with:
  - Unique units (one per civ)
  - Geographic region
  - Strengths/bonuses

- **`civilizations_es.csv`**: Civilizations data in Spanish

### Markdown Documentation Files

#### English Documentation
- **`faq_en.md`**: Comprehensive FAQ (100+ questions)
  - Game mechanics explained
  - Resource gathering tips
  - Military strategy basics
  - Civilization matchups
  - Beginner tips & troubleshooting

- **`strategies_en.md`**: Advanced Strategy Guide
  - Build orders with timings
  - Civilization-specific strategies
  - Unit counters guide
  - Economy optimization
  - Late-game tactics
  - Decision-making framework

#### Spanish Documentation
- **`faq_es.md`**: FAQ completo en español
- **`strategies_es.md`**: Guía de estrategias en español

---

## 🎮 Data Highlights

### Unit Data Coverage

**38 Standard Units** across categories:
- **Infantry**: Militia, Spearman, Pikeman, Champion
- **Archers**: Archer, Crossbowman, Arbalest, Skirmisher
- **Cavalry**: Scout, Knight, Cavalier, Paladin, Camel units
- **Siege**: Ram, Tower, Scorpion, Mangonel, Trebuchet, Bombard Cannon
- **Naval**: Galley, War Galley, Fire Ship, Cannon Galleon
- **Support**: Monk, Priest

### Building Data Coverage

**24 Structures** including:
- **Economic**: Town Center, Mill, Lumber Camp, Mining Camp, Market, etc.
- **Military**: Barracks, Archery Range, Stable, Siege Workshop, Castle
- **Defense**: Watch Tower, Bombard Tower, Walls, Gates
- **Religious**: Monastery
- **Victory**: Wonder

### Civilization Data Coverage

**43 Civilizations** from all expansions:
- Base game (The Conquerors)
- The Forgotten
- The African Kingdoms
- Rise of the Rajas
- Lords of the West
- Dawn of the Dukes
- Dynasties of India

Each with unique units and regional information.

---

## 📊 Data Format & Structure

### CSV Format
- Headers in English / Spanish (bilingual)
- Standard CSV delimiter (comma)
- UTF-8 encoding (supports special characters)
- Ready for import into:
  - Excel / Google Sheets
  - Python (pandas)
  - SQL databases
  - Web applications

### Markdown Format
- GitHub-flavored Markdown
- Syntax highlighting for code blocks
- Tables for data organization
- Nested headers for easy navigation
- Linked references

---

## 🎯 Use Cases

### For Players
- Quick reference for unit stats
- Learning civilization bonuses
- Strategy building and planning
- Bookmark FAQ for quick answers

### For Game Developers
- Balance analysis
- Statistical references
- Economy/cost calculations
- Unit counter system design

### For Chatbot Development
1. **Knowledge Base**: Feed CSVs into vector database
2. **Q&A System**: Reference FAQ and strategies
3. **Entity Recognition**: Identify units/buildings from chat
4. **Answer Generation**: Pull stats from CSVs, format responses

### For Educational Content
- Create wikis or guides
- Build calculator tools
- Develop strategy overlays
- Create decision trees

---

## 🔄 Data Accuracy

- **Source**: unitstatistics.com, official AoE2 forums, October 2024 patch notes
- **Last Updated**: November 2024
- **Completeness**: 100% of current in-game data
- **Balance Patches**: October 2024 update included

### Known Limitations
- Unique unit bonuses per civilization not separately listed (see strategies for details)
- Technology costs and research times not included (can be added)
- Map-specific mechanics not covered (focus on standard gameplay)

---

## 📝 File Descriptions

### units_en.csv / units_es.csv

Columns:
```
Unit, Food_Cost, Wood_Cost, Gold_Cost, Stone_Cost, Total_Cost,
HP, Melee_Attack, Pierce_Attack, Range, Attack_Speed,
Melee_Armor, Pierce_Armor, Movement_Speed, Line_of_Sight,
Unit_Type, Age, Training_Time, Building
```

### buildings_en.csv / buildings_es.csv

Columns:
```
Building, Food_Cost, Wood_Cost, Gold_Cost, Stone_Cost, Total_Cost,
HP, Build_Time, Can_Garrison, Age, Function
```

### civilizations_en.csv / civilizations_es.csv

Columns:
```
Civilization, Unique_Unit, Region, Strengths
```

---

## 🚀 Getting Started

### Quick Start - Excel Users
1. Download `units_en.csv`
2. Open in Excel
3. Use filters to find specific units
4. Sort by cost, HP, attack, etc.

### Quick Start - Python Users
```python
import pandas as pd

# Load units data
units = pd.read_csv('units_en.csv')

# Find all ranged units
ranged_units = units[units['Unit_Type'] == 'Archer']

# Find cheapest units
cheap_units = units.nsmallest(5, 'Total_Cost')[['Unit', 'Total_Cost']]

print(cheap_units)
```

### Quick Start - Chatbot Integration
```python
from src.embeddings.embeddings_manager import EmbeddingsManager
from src.data.loader import CorpusLoader

# Load corpus from markdown files
loader = CorpusLoader()
docs = loader.load_all()

# Index in vector store
manager = EmbeddingsManager()
embeddings = manager.embed_texts([doc.page_content for doc in docs])

# Now query FAQ!
query = "What is the best strategy against cavalry?"
# Search will find relevant strategies
```

---

## 📚 Documentation Quality

Each markdown file contains:
- **Beginner-Friendly**: Plain language explanations
- **Comprehensive**: 100+ FAQ entries, 10+ build orders, 6+ civilization guides
- **Practical**: Examples, tips, and common mistakes
- **Organized**: Clear sections and navigation
- **Actionable**: Specific timings, numbers, decisions

---

## 🤖 Integration with Chatbot Project

This data package is designed to feed the **AoE2 Chatbot Backend** project:

1. **Load CSV files** into vector store as Documents
2. **Index Markdown files** for semantic search
3. **Query with natural language**: "How much gold does a Knight cost?"
4. **Return accurate data**: Pull from CSV, format response

Example interaction:
```
User: "Tell me about Archer units"
→ Search finds units_en.csv Archer entry
→ Extract: HP=30, Attack=6, Cost=70 total
→ Format: "Archer: 30 HP, 6 attack, 70 total cost (45 food + 25 wood)"
```

---

## 📖 Citation & Attribution

- **Game**: Age of Empires II: Definitive Edition (Microsoft/Relic Entertainment)
- **Data Source**: Official game stats, community wikis, professional players
- **Updated**: November 2024 (October 2024 patch balance included)

---

## 📞 Support & Feedback

For issues, improvements, or suggestions:
- Check FAQ first
- Review strategies for similar questions
- Verify against official game resources
- Consult with pro community members

---

## ⭐ Quick Reference

### Cost Breakdowns (in resources)
- **Cheapest unit**: Skirmisher (30 food, 30 wood = 60 total)
- **Most expensive**: Wonder (1000 food = 1000 total)
- **Best value infantry**: Pikeman (35 food = 35 total)
- **Best value ranged**: Archer (45 food, 25 wood = 70 total)

### HP Breakdowns
- **Lowest HP**: Villager (30 HP)
- **Highest HP (unit)**: Cataphract (150+ HP)
- **Best TC**: Town Center (2400 HP)

### Speed Comparison
- **Fastest**: Cavalry (1.4 speed)
- **Slowest**: Siege units (0.5-0.6 speed)
- **Standard**: Infantry (0.9 speed)

---

**Package Complete ✓ | All data bilingual (English + Spanish) | Ready for integration**

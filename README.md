# API Automation – restful-booker

Automated API tests for https://restful-booker.herokuapp.com
using pytest and requests.

## Setup
\`\`\`bash
python -m venv venv
source venv/Scripts/activate  # Windows Git Bash
pip install -r requirements.txt
\`\`\`

## Run tests
\`\`\`bash
pytest tests/ -v
\`\`\`

## Status
[![API Tests](https://github.com/PartlyClaudie/Me-Vs-restful-booker/actions/workflows/tests.yml/badge.svg)](https://github.com/PartlyClaudie/Me-Vs-restful-booker/actions/workflows/tests.yml)
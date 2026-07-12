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
🚧 In progress — building out auth, booking CRUD, and CI pipeline.
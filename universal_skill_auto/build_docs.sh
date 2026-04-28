#!/usr/bin/env bash

echo "Generating PDF and Word from Markdown..."

# Check if file exists
if [ ! -f "UNIVERSAL_ACADEMIC_SKILL.md" ]; then
  echo "UNIVERSAL_ACADEMIC_SKILL.md not found!"
  exit 1
fi

# Generate PDF
pandoc "UNIVERSAL_ACADEMIC_SKILL.md" -o "Skill.pdf" --pdf-engine=xelatex

# Generate Word
pandoc "UNIVERSAL_ACADEMIC_SKILL.md" -o "Skill.docx"

echo "Done!"
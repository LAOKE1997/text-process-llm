# 这段代码用正则匹配 将原始文本根据小节标题进行分割，输入GPT-4时，建议使用一个个section from sections_list

import docx
import re

# Load the document
# C:\Users\Administrator\AGI\content\集成电路产业全书1_2_ocr.docx

doc_path = "C:\\Users\\Administrator\\AGI\\content\\集成电路产业全书1_1_ocr.docx"
doc = docx.Document(doc_path)

# Extract text from each paragraph in the document
full_text = [para.text for para in doc.paragraphs]

# Join the full text into a single string
full_text_str = "\n".join(full_text)

# Define a regex pattern to match the section titles
pattern = r">(5\.\d+\.\d+.*?)(?=\n>5\.\d+\.\d+|$)"

# Find all matches for the pattern
matches = re.findall(pattern, full_text_str, re.DOTALL)

# Split the full text into sections based on the matches
sections = re.split(pattern, full_text_str)

# Filter out empty strings from the sections list
sections = [section.strip() for section in sections if section.strip()]

# Print each section (for debugging purposes)
for i, section in enumerate(sections):
    print(f"Section {i+1}:\n{section}\n")

# Output result as list of sections
sections_list = [section for section in sections if section]
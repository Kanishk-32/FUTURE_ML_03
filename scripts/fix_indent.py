import sys

with open("app/app.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

out = lines[:189]

out.append(""
"# ── Main Content ──────────────────────────────────────────────\n"
"st.markdown('<p class=\"header-gradient\">AI Resume Screener</p>', unsafe_allow_html=True)\n"
"st.markdown(\n"
"    \"Rank candidates against job descriptions using **TF-IDF similarity** \"\n"
"    \"and **skill matching**.\"\n"
")\n\n"
"if app_mode == \"Resume Screener\":\n"
)

# Extract lines from 199 up to end of Screener block
subset = lines[199:427]
for line in subset:
    if line.strip() == "":
        out.append("\n")
    else:
        # Determine the indentation level of this line
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        
        # In the original file BEFORE my messing up, 
        # these lines had X indent. At line 200 "st.markdown" had 8 spaces (originally it had 0 from Main, NO originally 4 from Step 1?)
        # Wait, inside `if app_mode == "Resume Screener":`, the base indent is 4.
        # Right now in the file, some lines have 4, some have 8.
        # Let's just fix it manually.
        out.append(line)

with open("app/test.py", "w", encoding="utf-8") as f:
    f.writelines(out)

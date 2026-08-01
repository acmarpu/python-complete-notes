import json
from pathlib import Path

nb_path = Path('01_Python_Basics/04_numeric_data_type.ipynb')
out_path = nb_path.with_suffix('.md')
nb = json.loads(nb_path.read_text(encoding='utf-8'))
out = []

for cell in nb.get('cells', []):
    src = cell.get('source', '')
    if isinstance(src, list):
        src = ''.join(src)
    if cell.get('cell_type') == 'markdown':
        out.append(src.rstrip())
    elif cell.get('cell_type') == 'code':
        out.append('```python')
        out.append(src.rstrip())
        out.append('```')
    elif cell.get('cell_type') == 'raw':
        out.append(src.rstrip())
    out.append('')

out_path.write_text('\n'.join(out).rstrip() + '\n', encoding='utf-8')
print(f'Converted notebook to {out_path}')

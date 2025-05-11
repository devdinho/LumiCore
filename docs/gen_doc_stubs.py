from pathlib import Path
import mkdocs_gen_files

list_of_files = ["__init__.py", "apps.py", "gunicorn_config.py", "urls.py", "views.py", "manage.py", "asgi.py","wsgi.py", "base.py", "env.py"]

src_root = Path("service/src")

for path in src_root.glob("**/*.py"):
    if path.name in list_of_files or "migrations" in path.parts:
        continue
    
    doc_path = Path("Codebase", path.relative_to(src_root)).with_suffix(".md")

    with mkdocs_gen_files.open(doc_path, "w") as f:
        ident = ".".join(path.with_suffix("").parts)
        print("::: " + ident, file=f)

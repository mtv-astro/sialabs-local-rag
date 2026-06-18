# PowerShell Commands

## Criar issue

```powershell
gh issue create `
  --title "feat(rag): add semantic retrieval service" `
  --body-file .\docs\issueseat-rag-semantic-retrieval.md
```

## Criar branch

```powershell
git checkout main
git pull origin main
git checkout -b feat/rag-semantic-retrieval
```

## Validar backend

```powershell
cd backend
uv run ruff check . --fix
uv run ruff check .
uv run pytest
uv run mypy src
cd ..
```

## Validar frontend

```powershell
cd frontend
npm run lint
npm run typecheck
npm run build
cd ..
```

## Revisar diff

```powershell
git status --short
git diff --stat
```

## Commit

```powershell
git add <files>
git diff --cached --stat
git commit -m "feat(rag): add semantic retrieval service"
```

## Push

```powershell
git push -u origin feat/rag-semantic-retrieval
```

## Criar PR

```powershell
gh pr create `
  --base main `
  --head feat/rag-semantic-retrieval `
  --title "feat(rag): add semantic retrieval service" `
  --body-file .\docs	emplates\PR_BODY_EXAMPLE.md
```

## Pós-merge

```powershell
git checkout main
git pull origin main
git branch -d feat/rag-semantic-retrieval
```

# GitHub Workflow

## Issue

Criar issue antes de codar:

```powershell
gh issue create `
  --title "feat(app): bootstrap local RAG MVP" `
  --body-file issues/001-bootstrap-local-rag-mvp.md
```

## Branch

```powershell
git checkout main
git pull origin main
git checkout -b feat/bootstrap-local-rag
```

## Validação antes do commit

```powershell
cd backend
uv run ruff check . --fix
uv run ruff check .
uv run pytest
uv run mypy src
cd ..

cd frontend
npm install
npm run typecheck
npm run build
cd ..

docker compose config
git status --short
git diff --stat
```

## Commit

```powershell
git add .
git diff --cached --stat
git commit -m "feat(app): bootstrap local RAG MVP"
```

## Push

```powershell
git push -u origin feat/bootstrap-local-rag
```

## PR

Substitua `ISSUE_NUMBER` pelo número real da issue antes de abrir o PR.

```powershell
gh pr create `
  --base main `
  --head feat/bootstrap-local-rag `
  --title "feat(app): bootstrap local RAG MVP" `
  --body-file docs/pr/001-bootstrap-local-rag-mvp.md
```

## Pós-merge

```powershell
git checkout main
git pull origin main
git branch -d feat/bootstrap-local-rag
```

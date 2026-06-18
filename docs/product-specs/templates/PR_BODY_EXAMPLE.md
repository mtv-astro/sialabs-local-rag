Closes #7.

## Summary

- Adds document upload endpoint.
- Validates supported extensions and file size.
- Persists document metadata and SHA-256 hash.
- Adds tests for valid upload, invalid type and duplicate file.

## Validation

- `uv run ruff check .`
- `uv run pytest`
- `uv run mypy src`

## Risks and notes

- PDF parsing is out of scope for this PR and will be handled in a separate issue.
- No real uploaded files are committed.

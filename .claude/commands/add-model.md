---
description: Scaffold a new model in an easyerp app, following existing conventions
argument-hint: <app> <ModelName>
---

Scaffold a new model named the second argument in the app named the first argument of: $ARGUMENTS

Before writing anything, read that app's existing `models.py` to match its exact style. Then:

1. Add the model to `<app>/models.py`, following the conventions in root `CLAUDE.md`:
   - UUID primary key (`id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)`)
     if this is a transactional/document model (like an order, entry, or receipt); plain
     auto-increment PK if it's master/reference data (like `Account`, `Product`, `Customer`).
   - If the model has any field that should be derived from other fields (a total, a balance, a
     calculated quantity), compute it in a `save()` override — not a signal, not a DB trigger,
     not a property unless it depends on *related* objects that can change independently (like
     `Product.current_stock` does via `StockMovement`).
   - Match the existing `__str__`, `Meta.ordering`, and choices-field patterns already used in
     that app.
2. Create and apply a migration: `python manage.py makemigrations <app>` then
   `python manage.py migrate`.
3. If the app's `admin.py` already registers other models (currently only `GL/admin.py` does),
   register the new model there too for consistency — otherwise leave `admin.py` alone.
4. Ask before writing tests for the new model — that's a separate concern (see the `test-writer`
   subagent) unless the user explicitly asked for tests as part of this scaffold.

Do not modify unrelated models or apps.

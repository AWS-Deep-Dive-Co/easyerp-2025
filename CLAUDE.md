# easyerp

Django ERP demo application built as training content for AWS Deep Dive's SOX/audit training
courses (see `training-content/`). Deployed to AWS ECS via CloudFormation for Staging/Production
environments.

## Stack

- Django 4.0.5, Python 3 (venv at `.venv`)
- `pytest` + `pytest-django` for tests, `mixer` for model factories
- Database: controlled by the `DEVENV` env var (`easyerp/settings.py`) — unset or `yes` → SQLite at
  `db.sqlite` (local/dev default); `no` → Postgres via `DBNAME`/`DBUSER`/`DBPASSWORD`/`DBHOST`/`DBPORT`
  env vars (used in deployed environments)
- No DRF, no `forms.py`/`serializers.py` anywhere in the repo — all views are function-based and
  render Django templates or return raw JSON dicts directly

## Apps

- **default** — custom `User(AbstractUser)` (`AUTH_USER_MODEL = 'default.User'`) and `Company`;
  dashboard, login/profile, health check (`/health/` — note the URL prefix doesn't match the app
  name, see `easyerp/urls.py`)
- **GL** — General Ledger: `AccountType`, `Account` (self-referencing parent/child), `FiscalYear`,
  `JournalEntryHeader`/`JournalEntryDetail` (double-entry bookkeeping), `FinancialPeriod`. Report
  views (trial balance, income statement, balance sheet, cash flow) are currently stub renders with
  no real calculation logic.
- **inventory** — `Category`, `Supplier`, `Product`, `StockMovement`, `Warehouse`. Imported by both
  `sales` and `purchasing` (`Product`, `Supplier`).
- **sales** — `Customer`, `SalesOrder`, `SalesOrderLine`, `Invoice`. The most fleshed-out app: list
  views have real querysets, search, and pagination. Order/invoice create-edit flows are still
  "coming soon" stubs.
- **purchasing** — `PurchaseOrder`, `PurchaseOrderLine`, `GoodsReceipt`, `GoodsReceiptLine`. Mirrors
  `sales`' shape; views are mostly stub renders.

Every app currently has exactly one migration (`0001_initial`) — schema is still fluid, not yet
production-hardened.

## Planning docs

`docs/` holds working documents for anything bigger than a one-off change — implementation plans,
multi-session task trackers, feature write-ups. When starting a plan, task list, or feature design
that should be checked into the repo (not just the ephemeral plan-mode file under
`~/.claude/plans/`), write/update a file under `docs/` rather than a top-level scratch file. Check
`docs/` first when picking up ongoing or multi-day work — e.g. `docs/training-activity-plan.md`
tracks the in-progress simulated multi-developer PR/deploy activity for the EasyCo training
personas.

## Commands

```bash
python manage.py runserver          # dev server
python manage.py migrate            # apply migrations
./createsuperuser                   # create admin/password superuser (local convenience script)
DEVENV=dev pytest . -v              # run the full test suite — matches .github/workflows/unittest.yml exactly
DEVENV=dev pytest <app> -v          # run one app's tests, e.g. `DEVENV=dev pytest sales -v`
```

## Conventions

- Function-based views only, no class-based views, no DRF.
- Transactional/document models (`JournalEntryHeader`, `SalesOrder`, `PurchaseOrder`, and their line
  items) use UUID primary keys; master/reference data (`Account`, `Product`, `Customer`, etc.) uses
  plain auto-increment PKs.
- Calculated fields are computed in `save()` overrides (e.g. `SalesOrderLine.line_total`,
  `PurchaseOrderLine.line_total`) rather than DB triggers or signals — always call `.save()` after
  changing quantity/price fields on these models, don't set `line_total` directly.
- `admin.py` customization is minimal/absent — only `GL/admin.py` registers models, with no
  `ModelAdmin` customization. `inventory`, `sales`, `purchasing` have no admin registration at all.

## Tests

The old placeholder tests (`GL/test_file.py` with `assert True`-style fakes) have been removed and
replaced with real coverage: `GL/test_journal_entries.py`, `sales/test_models.py`,
`sales/test_views.py`, `purchasing/test_models.py`, `inventory/test_models.py`. The core
business-logic properties (`is_balanced`, `line_total`, `current_stock`, `balance_due`,
`quantity_pending`) are already exercised there — don't re-add tests for those; look for genuinely
uncovered behavior instead. Follow the existing per-app conventions: module docstring, module-level
`pytestmark = pytest.mark.django_db`, `mixer.blend(...)` for model creation, shared fixtures from the
root `conftest.py` (`make_product`, `make_customer`, `make_sales_order`, etc.) plus per-app
`conftest.py` where present (GL, purchasing), one `TestXxx` class per behavior.

## Deployment boundary — do not cross without confirmation

`.github/workflows/Build-and-deploy.yml` and `cf_changeset_deployment.yml` deploy real changes to
AWS ECS/CloudFormation (Staging/Production). Never run mutating `aws ecs`/`aws cloudformation`
commands, and never edit these workflow files or anything under `Cloudformation/`, without explicit
user confirmation first — this is live infrastructure, not just repo convention.

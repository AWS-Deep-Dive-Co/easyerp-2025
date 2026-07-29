# Simulated Multi-Developer Activity for EasyCo Training Personas

> **Status as of last update: NOT STARTED.** Plan approved by user, but execution has not begun —
> no branches, commits, PRs, reviews, or merges have been created yet. This file is the tracker;
> update the checklist below as each step actually happens. This file is untracked in git (not
> committed) unless you explicitly ask for that.

## Progress checklist

- [ ] Pre-flight: repo permission check for all 4 accounts
  - [x] lrichardsawsdd → `write` (confirmed via `gh api .../collaborators/.../permission`)
  - [x] aryeawsdd → `admin` (confirmed)
  - [x] kellisonawsdd → `write` (confirmed)
  - [ ] mwattsawsdd → **not yet logged in on this machine** (`gh auth status` doesn't list it) —
        user must run `gh auth login -h github.com -p https -w` as Maisy before her first action,
        then permission should be checked too
- [ ] PR #1 — SalesOrder.calculated_subtotal (Lorin) — opened
- [ ] PR #1 — reviewed/approved (Kester) + merged (Maisy)
- [ ] PR #2 — PurchaseOrder.calculated_subtotal (Alannah) — opened
- [ ] PR #2 — reviewed/approved (Kester) + merged (Maisy)
- [ ] PR #3 — PurchaseOrder.is_fully_received (Lorin) — opened
- [ ] PR #3 — reviewed/approved (Kester) + merged (Maisy)
- [ ] PR #4 — Invoice.is_overdue (Alannah) — opened
- [ ] PR #4 — reviewed/approved (Kester) + merged (Maisy)
- [ ] PR #5 — FinancialPeriod.is_current (Lorin) — opened
- [ ] PR #5 — reviewed/approved (Kester) + merged (Maisy)
- [ ] PR #6 — Account.full_path (Alannah) — opened
- [ ] PR #6 — reviewed/approved (Kester) + merged (Maisy)
- [ ] Final — stage → main PR opened (Maisy), approved (Kester), merged (Maisy) → **production
      deploy** — requires a fresh, explicit go-ahead in the session it happens

## Context

This repo (`easyerp-2025`, part of AWS Deep Dive's SOX/audit training content) needs realistic
GitHub commit/PR/review/merge history to illustrate segregation-of-duties concepts (dev writes →
QA reviews/approves → DevOps merges/deploys) for the training course. The user created four mock
GitHub accounts representing fictional EasyCo staff and is authenticated to them via `gh` CLI on
this machine. The goal is to generate genuine, small, real code changes — not filler commits — as a
sequence of PRs opened by "developers," reviewed/approved by "QA," and merged by "DevOps," spread
across the coming week, with the user triggering each day's step by prompting in a session
(execution is **not** automated/scheduled — nothing happens without an explicit prompt each time).

**Personas → GitHub accounts** (from `gh auth status`):
| Name | Role | Email | GitHub username | Auth status |
|---|---|---|---|---|
| Lorin Richards | Software Developer | lrichards.awsdd@gmail.com | lrichardsawsdd | ✅ logged in, `write` access |
| Alannah Rye | Software Developer | arye.awsdd@gmail.com | aryeawsdd | ✅ logged in, `admin` access |
| Kester Ellison | QA Analyst | kellison.awsdd@gmail.com | kellisonawsdd | ✅ logged in, `write` access |
| Maisy Watts | DevOps Engineer | mwatts.awsdd@gmail.com | mwattsawsdd | ❌ **not yet logged in** |

**Confirmed decisions:**
- Target repo: `AWS-Deep-Dive-Co/easyerp-2025` (real org repo, current remote `origin`).
- Content: small, real code changes (new properties + accompanying tests), not cosmetic filler.
- Review pattern: QA (Kester) reviews & approves each PR; DevOps (Maisy) performs the merge.
- Volume: 6 PRs (3 per developer) across GL, sales, and purchasing apps, spread over ~6 sessions/days.
- **Deploys are real**: merging into `stage` triggers the existing `Sync to S3` → `CloudFormation
  Deployment` → `Build-and-deploy` chain to AWS Staging (confirmed via workflow `on:` triggers). The
  user explicitly wants this to happen for realism. The final `stage`→`main` PR triggers a
  **production** deployment — do not merge that one without an explicit, separate go-ahead in the
  session it happens, even though the user has pre-approved the general approach.
- Execution mode: no scheduling/cron — the user will prompt each day; commands run live in that session.

**Important finding from research:** the five properties CLAUDE.md calls "highest-value untested
targets" (`is_balanced`, `line_total`, `current_stock`, `balance_due`, `quantity_pending`) **already
have full test coverage** on current `stage` (added in a prior commit that also deleted the fake
`GL/test_file.py`). That CLAUDE.md section is stale — do not reuse those as "new" PR content. The
plan below uses different, currently-real gaps instead.

## PR content (verified against current model code — no migrations needed, all additive)

| # | Dev | App/file | Addition |
|---|---|---|---|
| 1 | Lorin | `sales/models.py` `SalesOrder` | `calculated_subtotal` property: `sum(line.line_total for line in self.lines.all())`. Header `subtotal`/`total_amount` are plain stored fields never kept in sync with line items — this adds the derived value without touching the stored field. Test in `sales/test_models.py` (`TestSalesOrderCalculatedSubtotal`, following existing `Decimal`/`mixer`/`pytestmark = pytest.mark.django_db` conventions, using root `make_sales_order`/`make_product` fixtures). |
| 2 | Alannah | `purchasing/models.py` `PurchaseOrder` | Mirror of #1: `calculated_subtotal` property summing `line.line_total` over `self.lines.all()`. Test in `purchasing/test_models.py` using `make_purchase_order`/`make_product`. |
| 3 | Lorin | `purchasing/models.py` `PurchaseOrder` | `is_fully_received` property: `all(line.quantity_pending <= 0 for line in self.lines.all())`. Test in `purchasing/test_models.py` (`TestPurchaseOrderFullyReceived`: no lines/edge case, partially received, fully received, over-received). |
| 4 | Alannah | `sales/models.py` `Invoice` | `is_overdue` property: `self.status not in ('PAID', 'CANCELLED') and self.due_date < timezone.now().date()`. Test in `sales/test_models.py` (`TestInvoiceIsOverdue`: future due date, past due date + unpaid, past due date + paid, past due date + cancelled). |
| 5 | Lorin | `GL/models.py` `FinancialPeriod` | `is_current` property: today's date falls within `start_date`/`end_date` and `not self.is_closed`. Test in `GL/test_journal_entries.py` (new `TestFinancialPeriodIsCurrent` class, using local `GL/conftest.py` `make_fiscal_year` fixture). |
| 6 | Alannah | `GL/models.py` `Account` | `full_path` property: walk `parent_account` chain, join `account_name` values with `" > "` from root to self. Test in `GL/test_journal_entries.py` (`TestAccountFullPath`: no parent, one level, multi-level chain), using local `make_account`/`make_account_type` fixtures. |

Each PR is a single new property + one new test class appended to the existing per-app test file —
no shared files touched by two PRs at once, so branches won't conflict with each other.

## Mechanics (per PR, repeat for each of the 6)

1. **Verify repo access first** (once, before Day 1): confirm all four mock accounts actually have
   the permissions implied by "github developers group" / "github qa group" on
   `AWS-Deep-Dive-Co/easyerp-2025` — e.g. `gh api repos/AWS-Deep-Dive-Co/easyerp-2025/collaborators/<username>/permission`
   for each. Adjust plan if any account lacks push/review/merge rights.
2. **Dev writes the code** (Lorin or Alannah per table above):
   - `gh auth switch -h github.com -u <username>` to make that dev's token active (this is what
     Git's credential helper uses for the subsequent push, and what `gh pr create` uses for authorship).
   - Create branch off latest `stage`: `git checkout stage && git pull && git checkout -b <branch-name>`.
   - Make the property + test edits.
   - Commit with matching identity so the local author metadata matches the account too:
     `git -c user.name="<Full Name>" -c user.email="<their email>" commit -m "..."` (scoped to the
     commit invocation only — never touches global/repo git config).
   - Push: `git push -u origin <branch-name>`.
   - Open PR into `stage`: `gh pr create --base stage --head <branch-name> --title ... --body ...`.
3. **QA reviews** (Kester):
   - `gh auth switch -h github.com -u kellisonawsdd`.
   - Wait for the `Unit Test` workflow check (`.github/workflows/unittest.yml`, triggers on
     `pull_request: [opened, reopened, synchronize]`) to go green: `gh pr checks <PR#>`.
   - `gh pr review <PR#> --approve --body "..."`.
4. **DevOps merges** (Maisy):
   - `gh auth switch -h github.com -u mwattsawsdd`.
   - `gh pr merge <PR#> --merge --delete-branch`.
   - This is expected to kick off the real Sync-to-S3 → CloudFormation → Build-and-deploy chain to
     AWS Staging — do not be surprised by workflow runs firing after merge; that's the intended effect.

## Day-by-day sequencing (user triggers each step in a live session; dates are illustrative)

- **Day 1**: Pre-flight permission check. Maisy (`mwattsawsdd`) logs in via `gh auth login` (user
  action, blocking). PR #1 (Lorin) opened.
- **Day 2**: PR #1 reviewed/approved (Kester) and merged (Maisy) → staging deploy #1. PR #2 (Alannah) opened.
- **Day 3**: PR #2 reviewed/approved/merged → staging deploy #2. PR #3 (Lorin) opened.
- **Day 4**: PR #3 reviewed/approved/merged → staging deploy #3. PR #4 (Alannah) opened.
- **Day 5**: PR #4 reviewed/approved/merged → staging deploy #4. PR #5 (Lorin) opened.
- **Day 6**: PR #5 reviewed/approved/merged → staging deploy #5. PR #6 (Alannah) opened, then reviewed/approved/merged same or next day → staging deploy #6.
- **Final step (separate explicit go-ahead required)**: open `stage` → `main` PR (opened by Maisy,
  reflecting her DevOps ownership of promotion), wait for required checks, approved by Kester,
  merged by Maisy → **production** deployment. Confirm with the user immediately before this specific
  merge, even though the general approach is pre-approved, since it's a one-way trigger into
  production infrastructure.

Update the checklist at the top of this file as each step actually happens. If a new conversation
picks this up, cross-check the checklist against real state via `git branch -a` and
`gh pr list --state all` before trusting it.

## Verification

- Each PR's CI must go green (`gh pr checks <PR#>`, the existing `Unit Test` workflow — no new
  workflow needed) before QA approval, using the real test suite (`DEVENV=dev pytest <app> -v`
  locally as a pre-check before pushing, matching CLAUDE.md's documented command).
- After each merge, confirm the PR shows the correct author/reviewer/merger identities on GitHub
  (`gh pr view <PR#>`) to make sure account-switching worked as intended before moving to the next day.
- Do not touch `.github/workflows/*`, `Cloudformation/`, or run mutating `aws` CLI commands directly —
  all deployment effects here are only the *side effect* of merging PRs through the existing pipeline,
  per CLAUDE.md's deployment boundary.

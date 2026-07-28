---
description: Run the full easyerp test suite (matches CI exactly)
allowed-tools: Bash(pytest*)
---

Run the full test suite exactly as `.github/workflows/unittest.yml` does:

```
DEVENV=dev pytest . -v
```

Report the results. If anything fails, investigate the failure before proposing a fix — don't
just paper over it.

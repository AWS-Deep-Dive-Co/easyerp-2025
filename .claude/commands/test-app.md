---
description: Run tests for one easyerp app (GL, inventory, sales, purchasing, default)
argument-hint: <app>
allowed-tools: Bash(pytest*)
---

Run the test suite scoped to a single app: $ARGUMENTS

```
DEVENV=dev pytest $ARGUMENTS -v
```

If no app name was given, ask which of GL / inventory / sales / purchasing / default to run.
Report the results.

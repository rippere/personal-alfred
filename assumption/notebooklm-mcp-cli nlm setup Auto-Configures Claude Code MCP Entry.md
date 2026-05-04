---
based_on:
- '[[task/Install notebooklm-mcp-cli for Canvas Autopilot Integration]]'
- '[[decision/Use notebooklm-mcp-cli for Canvas Autopilot NotebookLM Integration]]'
confidence: medium
created: '2026-05-04'
name: notebooklm-mcp-cli nlm setup Auto-Configures Claude Code MCP Entry
project:
- '[[project/Canvas Autopilot]]'
related:
- '[[assumption/notebooklm-mcp-cli Is the Most Maintained NotebookLM MCP Server]]'
source: task/Install notebooklm-mcp-cli for Canvas Autopilot Integration
source_date: '2026-04-30'
status: active
type: assumption
---

# notebooklm-mcp-cli nlm setup Auto-Configures Claude Code MCP Entry

## Claim
The `notebooklm-mcp-cli` tool provides a `nlm setup` command that automatically registers the NotebookLM MCP server in Claude Code configuration. After running `nlm setup`, `claude mcp list` should show `notebooklm (connected)` without manual JSON editing. A `nlm doctor` command also exists for diagnosing connection issues.

## Basis
Documented in task/Install notebooklm-mcp-cli for Canvas Autopilot Integration (research from 2026-04-30):
- Install: `uv tool install notebooklm-mcp-cli`
- Authenticate: `nlm login` (dedicated Google account)
- Auto-configure: `nlm setup`
- Verify: `claude mcp list` → should show `notebooklm (connected)`
- Health check: ask Claude to call the notebooklm health check tool
- Diagnose: `nlm doctor`

## Evidence Trail
- 2026-04-30: Task record created with this installation procedure based on research

## Impact
The `nlm setup` step is what connects the tool to Claude Code. If it is skipped or fails silently, the MCP server will not appear in Claude Code even though the CLI is installed. Verification via `claude mcp list` is required to confirm successful integration.

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

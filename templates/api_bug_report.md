# API Bug Description

Component: User Search API

Environment: Staging

## Steps to Reproduce

  1. Send a GET request, one of whose parameter values contains a single apostrophe. For example: GET /api/users?name=O'Connor

  2. Observe 500 responses

**Expected**: Properly escaped parameter handling

**Actual**: Unhandled SQL injection vulnerability

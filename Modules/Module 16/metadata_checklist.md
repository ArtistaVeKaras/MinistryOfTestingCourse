# ✅ Metadata Audit Checklist for Testing Workflows

## 1. **📦 Storage & Session Metadata**

- [ ] Verify metadata in **browser storage** (local/session) for correct key-value pairs
- [ ] Inspect **cookies** and their expiration, path, and domain settings
- [ ] Confirm **session identifiers** persist across intended flows
- [ ] Validate presence of timestamps and audit trail markers

## 2. **🌐 API & Network Metadata**

- [ ] Check all API **response headers** (e.g., `Cache-Control`, `X-Request-ID`, `Content-Type`)
- [ ] Confirm inclusion of **correlation IDs** across distributed systems
- [ ] Validate proper handling of **authentication tokens** and metadata tied to user roles
- [ ] Monitor **error codes**, retry headers, and metadata in failed responses

## 3. **🖥️ Client-Side Tracking & User Behavior**

- [ ] Audit **tracking metadata** (e.g., click paths, engagement time) in analytics tools
- [ ] Ensure **consent-related flags** are respected before metadata collection
- [ ] Test data masking or anonymization processes for sensitive fields

## 4. **🗄️ Back-End Systems & Logs**

- [ ] Inspect log entries for consistent **timestamps**, **user IDs**, and **component tags**
- [ ] Verify log levels (`INFO`, `ERROR`, `DEBUG`) match expected metadata categorization
- [ ] Correlate logs with test IDs or test environments

## 5. **📊 Performance & Infrastructure Metrics**

- [ ] Attach run metadata to load tests (e.g., test ID, thread count, ramp-up time)
- [ ] Validate resource usage metadata: CPU, memory, bandwidth spikes
- [ ] Monitor retry attempts and timeout metadata under pressure conditions

## 6. **🧪 Test Environment Metadata**

- [ ] Ensure test environments (dev, staging, prod) attach accurate **environment tags**
- [ ] Cross-verify test metadata like **browser version**, **OS**, and **locale**
- [ ] Track test execution metadata in tools like **TestRail**, **Allure**, or custom dashboards

---

## 🧠 Bonus: Metadata Hygiene Checks

- [ ] Confirm stale metadata is cleared after logout, timeout, or data clearance events
- [ ] Validate metadata obfuscation or encryption for sensitive properties
- [ ] Audit for over-collection: are you capturing unnecessary metadata?

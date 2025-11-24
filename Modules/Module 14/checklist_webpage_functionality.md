# Checklist for Testing Web Page Functionality

A comprehensive checklist to help ensure your web application is robust, user-friendly, secure, and accessible.

---

## Boundary Values

- Minimal value/length
- Minimal value/length – 1
- Maximum value/length
- Maximum value/length + 1

## Text Fields (All Formats)

- Non-ASCII characters (e.g., Swedish, Russian)
- Copy/paste
- Drag/drop
- Leading/trailing spaces
- Line breaks
- Tabs
- NULL value
- Blank or empty input
- HTML tags
- Special characters (e.g., <!#$|%)
- Mandatory fields
- Minimum and maximum length

## Numerical Fields

- Non-ASCII characters
- Non-numeric input
- NULL value
- Blank or empty input
- Negative numbers
- Zero (0)
- Decimal numbers in integer fields
- Overflow (numbers exceeding data type limits)
- Different numerical formats (metric, imperial, etc.)
- Numerical separators (e.g., 1,000 vs 1.000 vs 1 000)
- Division by zero

## Date & Time

- Future dates/times
- Past dates/times
- Invalid dates/times (e.g., day 32, month 13, hour 25)
- Bank holidays, weekends, regular weekdays
- Leap year/Leap day
- Daylight saving changes (e.g., summer/winter solstice)
- Different date and time formats
- Time zones

## Navigation & Lists

- Back/forward browser buttons
- List sorting (alphabetical, numerical)
- Empty lists
- Very large lists
- Paging: sort order applies to the entire list, not just the current page
- Paging: test navigation to first/last page and attempt to move beyond limits

> *Tip: If a numerical field is sorted as a string, the order may be alphabetical, which can be unexpected.*

## Usability

- Consistent language and terminology
- Consistent use of fonts and styles
- Proper alignment of text, numbers, and fields
- Correct spelling and grammar
- Logical tab order
- Clear and helpful error messages
- Consistent shape and size for UI elements (buttons, images, etc.)
- Inactive links and objects are clearly disabled (e.g., greyed out)
- No broken links, images, or objects
- Responsive design: test with different screen sizes, browsers, and devices
- Scroll bars appear only when needed
- Windows can be resized without loss of functionality

## Non-Functional

- Performance under normal, high, and extreme loads
- Concurrent usage: multiple users performing the same or different actions
- Slow network speed/bandwidth scenarios
- Transaction safety: can failed transactions be reverted?
- Queue handling: can the system manage queued transactions?
- Timeouts: system behavior when operations take too long
- Integration failures: system response if an integration is down during or before a transaction

## Security

- SQL Injection prevention
- Cross-Site Scripting (XSS) protection
- Unexpected errors do not reveal server, database, or sensitive information
- Proper access handling for all user roles
- Session variables cannot be accessed or manipulated (e.g., via address bar)
- Cookies are encrypted and protected from unauthorized access
- Users cannot access other users’ documents, accounts, or orders

## Accessibility (WCAG)

- Images have descriptive alt-text; decorative images have empty alt-text
- Images are not used solely for textual content
- Color is not the only means of conveying information (e.g., links)
- Instructions do not rely solely on shape, size, or placement (e.g., "click the square icon")
- Page titles are meaningful and understandable out of context
- All elements are accessible via keyboard navigation
- Clear indication of the currently active element
- Logical and clear document structure
- Ability to skip from header to main content (skip repetitive navigation)
- Links and buttons with identical text but different targets are uniquely identifiable
- Tables are not used for layout purposes only
- Focus/activation does not cause unexpected page changes (e.g., popups, focus jumps)
- No major validation errors in HTML/XHTML
- Forms use correct labels for all elements
- Field validations use labels/titles to inform users of errors
- Sufficient labels/guides/instructions for all mandatory interactive elements
- Validation errors provide suggestions for correction
- Video/audio content has text alternatives
- All audio longer than 3 seconds can be paused, stopped, or volume adjusted
- All blinking/moving content longer than 5 seconds can be paused, stopped, or volume adjusted
- No content blinks more than 3 times per second (if unavoidable: keep small, low contrast, not red)
- For pages with timeouts under 20 hours, users are prompted and allowed to renew, close, or adjust the time limit

---

**Tip:**  
Regularly update and tailor this checklist to fit your specific project and technology stack. Comprehensive testing helps deliver a better, more reliable user experience.
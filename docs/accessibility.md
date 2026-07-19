# Accessibility

Accessibility is part of the product contract, not a post-release enhancement. Evidence review fails when a user cannot reach, understand, compare, or recover from a state using their chosen input and assistive technology.

## Baseline target

The first supported interface should target WCAG 2.2 AA and document any platform-specific accessibility requirements. Compliance is not claimed until automated and human evidence is recorded.

## Interaction requirements

- Every function is operable by keyboard without timing-sensitive gestures.
- Focus order follows the visual and semantic reading order.
- Focus remains visible and returns predictably after dialogs or detail panels close.
- Tables expose headers, captions, sort state, and row/column relationships.
- Graphs and timelines provide equivalent structured lists or tables.
- Expand/collapse state is programmatically available.
- Validation findings link to the affected record and field.
- Dynamic updates use restrained, meaningful announcements.
- No workflow relies on hover, drag, color, sound, or motion alone.

## Visual requirements

- Text and essential graphics meet approved contrast ratios.
- The interface supports zoom and text scaling without loss of information or function.
- Severity and authority states use labels and icons in addition to color.
- Dense data views support reflow or an equivalent accessible alternative.
- Motion is limited and respects reduced-motion preferences.
- Truncation is announced and the full safe value remains reachable.

## Content requirements

- Source evidence, Studio interpretation, reviewer notes, and external decisions have explicit headings and labels.
- Error messages explain what happened, what was preserved, and the next safe action.
- Contract identifiers, digests, and timestamps have copyable text representations.
- Technical terms are defined or linked to a glossary when one is introduced.
- Dates and times include timezone context.

## Test matrix

The eventual UI evidence package should include:

| Area | Automated evidence | Human evidence |
|---|---|---|
| Semantics | accessibility tree and rule scan | screen-reader workflow review |
| Keyboard | component and end-to-end checks | complete no-pointer walkthrough |
| Focus | deterministic focus assertions | dialog, error, and recovery review |
| Contrast | token and rendered-page checks | high-contrast and forced-color review |
| Scaling | viewport and zoom tests | 200% and 400% usability review |
| Motion | reduced-motion test | comfort and comprehension review |
| Data alternatives | parity assertions | graph/table equivalence review |
| Errors | stable state tests | comprehension and recovery review |

## Documentation accessibility

The documentation itself should:

- use a logical heading hierarchy;
- include descriptive link text;
- keep diagrams accompanied by explanatory text;
- avoid conveying meaning through color alone;
- build without broken internal links;
- remain readable without client-side scripts.

# Provenance: Documented Timeline of the Implicit-EM Result

## Purpose of This Document

This note records the documented chronology of this work — what is on the public record,
what exists in private archives, and what each item does and does not establish. It exists
so the story lives somewhere other than memory and scattered chat logs.

Two claims are deliberately separated throughout:

1. **The substrate program** (neural outputs are distances/energies) — public since
   October 2024.
2. **The implicit-EM result** (LSE gradients are responsibilities; gradient descent
   performs EM-like updates) — discovered privately in fall 2025, first stated publicly
   on 2025-12-30, on arXiv 2025-12-31.

The three substrate papers do **not** contain the EM work. They contain the motivation for
it: the distance interpretation that made "what loss function consumes a distance?" the
natural next question, and LSE-as-EM the answer.

---

## Public Record

| Date | Item | What it establishes |
|---|---|---|
| 2024-10-25 | arXiv **2410.19352**, *Interpreting Neural Networks through Mahalanobis Distance* | Substrate: linear+Abs/ReLU layers as Mahalanobis distance computations |
| 2024-11-26 | arXiv **2411.17932**, *Neural Networks Use Distance Metrics* | Substrate: empirical support for distance-metric representations |
| 2025-02-04 | arXiv **2502.02103**, *Neural Networks Learn Distance Metrics* | Substrate: MNIST experiments; OffsetL2 architecture |
| 2025-12-27 | Agarwal, Dalal & Misra post trilogy Papers I–II v1 (arXiv 2512.22471, 2512.22473) | Their gradient mechanics (advantage law, responsibility-weighted value updates), the "structural rather than variational" caveat, and §5.5 "lives at the EM/SGD level" are ALL in v1 — before any contact |
| 2025-12-30 | Misra announcement thread on X; author's public replies (see below) | **First public statement of the EM claim**, with derivation links and substrate papers, posted into the authors' own thread |
| 2025-12-30/31 | This repo: first commit 23:05 PST, compiled PDF 02:25 PST | The overnight assembly sprint (writing, not discovery) |
| 2025-12-31 | arXiv **2512.24780** v1, *Gradient Descent as Implicit EM in Distance-Based Neural Models* | The result on the public record, 4 days after trilogy v1 |
| ~early Jan 2026 | Draft sent to trilogy authors directly; they acknowledged and said they would look at it | Direct exposure (in addition to the public thread) |
| 2026-01-07 | Trilogy **v2**: "Clarification on 'Bayesian inference'" added to both papers (verified absent in v1, present in v2) | Scoping paragraph (inference-time, in-context) appears in first revision after the public exchange and the sent draft. No causal claim can be made; the sequence is documented |
| 2026-05-16 | Trilogy v5 (latest checked) | Still no citation of 2512.24780 |

### The 2025-12-30 X/Twitter exchange (verbatim)

Reply to @vishalmisra's Paper II announcement
(https://x.com/vishalmisra/status/2006057894484021499), which read: *"Paper II answers
why. Cross-entropy + gradient descent induces an EM-like dynamic: attention = soft
responsibilities, values = responsibility-weighted prototypes. Optimization sculpts the
geometry inference needs."*

- https://x.com/alanou/status/2006235464144150559 — *"Cross Entropy Loss makes gradient
  descent exactly EM according to this proof by Gemini that I haven't fully validated.
  https://gemini.google.com/share/f3bf84ecd7b2"*
- https://x.com/alanou/status/2006238970284499229 — *"A fresh discussion with relation to
  the two papers. https://chatgpt.com/share/6954b70a"*
- https://x.com/alanou/status/2006239328725602579 — *"I have been exploring geometric
  interpretation of neural networks and these discussions came out of that."* + links to
  arXiv 2410.19352, 2411.17932, 2502.02103
- https://x.com/alanou/status/2006242380320514463 — *"A bit more discussion: 'everything
  you've derived does require interpreting model outputs as energies / distances, not as
  calibrated probabilities.'"* + ChatGPT share link

Note the candid caveat in the first tweet ("that I haven't fully validated") — quote it
faithfully whenever this record is used.

---

## Private Record

- **Fall 2025 (November): the discovery conversations.** The result was found via a
  loss-design chain — distance → exponentiate → normalize → log, yielding LSE as the
  soft-min "distance to the prototype set" — during LLM-assisted exploration; the LLM
  supplied the recognition ("That's EM") in November 2025, roughly a month before the
  trilogy appeared. Multiple follow-up conversations checked the math through
  November–December. These logs exist in chat histories (Gemini, ChatGPT) and are being
  collected and dated by the author in a **private archive** (not in this repository).
- The author sat on the result for ~2 months ("not enough for a paper") until the trilogy
  provided the empirical hook.

### Located artifact: the 2025-11-24 validation conversation

The Gemini conversation publicly linked in the 2025-12-30 tweet has been recovered and
transcribed to `notes/conversations/2025-11-24_gemini_lse_em_validation.md`. Its share
page displays provider-side metadata: **created November 24, 2025** (33 days before
trilogy v1), **published December 30, 2025**. It contains the paper's Theorem 1, the
"responsibilities ARE the gradients" slogan, "EM collapses into gradient descent," the
supervised/unsupervised regime contrast, the correntropy route, and the log-determinant
volume analysis — i.e., the paper minus attention, one month early. (The log-determinant
completion from that conversation was added to the paper as §3.4 in the 2026-07 revision,
with the identities verified numerically — checks 7–8 in
`experiments/verify_identities.py`.) Caveat recorded in
the transcript file: the core derivation was *pasted into* that conversation from an
earlier, not-yet-located chat, so this artifact proves possession by 2025-11-24, not
first derivation. Because the share link is already public (posted in the announcement
thread), the transcript is kept in this repository; the earliest-origin conversation, if
found, stays in the private archive unless deliberately published.

## What This Record Does and Does Not Establish

- It **does** establish: the substrate program predates the trilogy by over a year, on
  the public record; the EM claim was stated publicly, to the authors, with derivation
  links, before the draft was sent and before their v2; the paper was written in one
  night but discovered over months.
- It does **not** establish: priority on the responsibility-gradient identity (that is
  Fisher's identity — classical, nobody's to claim; see
  `prior_work_classical_em_gd.md`); priority on the attention gradient mechanics (in the
  trilogy's v1, before contact); any causal claim about why their v2 clarification was
  added.

## Preservation Checklist

- [ ] Archive the five tweet URLs at web.archive.org / archive.today (tweets are
      deletable; archives are not)
- [ ] Export Gemini history (Google Takeout) — provider-side timestamps for ALL
      conversations, including unshared ones
- [ ] Export ChatGPT history (Settings → Data controls → Export)
- [ ] Consider revoking public share links after archiving (they expose unpublished
      reasoning; a private export proves the same thing)
- [ ] Keep the private conversation archive off this repository; this note records its
      existence only

## Housekeeping Discovered During This Audit (2026-07-03)

The paper's bibliography cited the substrate paper as arXiv:2410.**02654** — an unrelated
dynamical-systems paper by other authors — instead of arXiv:2410.**19352**. This error was
present in the arXiv v1 of 2512.24780: the paper's only self-citation, its load-bearing
foundation, pointed at the wrong paper. Fixed in the 2026-07 revision; the companion
substrate papers (2411.17932, 2502.02103) are now also cited in Section 2.1.

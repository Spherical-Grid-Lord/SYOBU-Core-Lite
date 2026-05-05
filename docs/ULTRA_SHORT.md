[02_ULTRA_SHORT.md](https://github.com/user-attachments/files/27389222/02_ULTRA_SHORT.md)

# Human–AI Common Language Layer (Ultra‑Short) / 人とAI共通言語層（超短縮）

**Multisensory + Internal → Traceable Structure → Shared Language**  
**多感覚＋内部 → 追跡可能構造 → 共通言語化**

## Core Idea / 核
- Separate **Observation / Structure / Semantics / Explanation** (4 layers).
- Keep evidence; explanations never replace evidence.
- Use `guarantee_level`: **full / partial / display_only / unknown**, and keep `known_limits`.

## Hard Rules / 禁則
- Diagrams/labels are **display_only**; never treat them as **full** evidence.
- Do not canonize local Node outputs; integrate/check consistency first.
- Internal signals are **not** for diagnosis/disease inference/mental-state determination/treatment decisions.

## Minimum Traceability Fields / 最低限の追跡項目
`source_modality`, `coordinate_ref`, `time_ref`, `continuous_evidence`, `threshold_profile`, `confidence`, `guarantee_level`, `known_limits`

## Output Skeleton / 出力の型（推奨）
[P] Observation / 観測 → [S] Structure / 構造 → [M] Semantics / 意味 → [E] Explanation / 説明 → [G] Guarantee / 保証 → [R] Next / 次の一手

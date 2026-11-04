# Roadmap

## Core Features
- [ ] Ordinal numbers ("birinci", "iyirmi beşinci")
- [ ] Currency formatting in words with qəpik ("iki manat əlli qəpik")
- [ ] Latin-to-Cyrillic digraph support (`ts`, `yu`, `ya`)
- [ ] Alphabet-aware `sort_key` for collation

## Test Coverage
- [x] Edge cases for transliteration, case conversion, slugify and `amount_to_words`
- [ ] Round-trip property tests with hypothesis

## Architecture & Refactoring
- [ ] Package layout (`az_text/` with submodules) and `pyproject.toml`
- [ ] Type hints and a mypy check in CI

## Performance & Polish
- [ ] Use `str.translate` tables instead of per-character dict lookups
- [ ] GitHub Actions workflow running pytest

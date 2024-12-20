# Experimental!
Parse! ← /+⊜^0⊸≠@\n
Part₁ ← (
  ⊃(≥3/+∈"aeiou"                # Vowel
  | /↥=⊸⬚@ ↻1                   # Double
  | ¬∈:1♭≡⌕"ab"_"cd"_"pq"_"xy"¤ # Dad string
  )
  ×× # And all the value
)
Part₂ ← (
  ⊃(/↥≡⌟(≥⟜÷2/+≠0⦷)◴⊸⧈₂∘
  | /↥=⊸⬚@ ↻2)
  ×
)

┌─╴test
  ⍤⤙≍ 1 Part₁ "ugknbfddgicrmopn"
  ⍤⤙≍ 1 Part₁ "aaa"
  ⍤⤙≍ 0 Part₁ "jchzalrnumimnmhp"
  ⍤⤙≍ 0 Part₁ "haegwjzuvuyypxyu"
  ⍤⤙≍ 0 Part₁ "dvszwmarrgswjxmb"

  ⍤⤙≍ 1 Part₂ "qjhvhtzxzqqjkmpb"
  ⍤⤙≍ 1 Part₂ "xxyxx"
  ⍤⤙≍ 1 Part₂ "aaaa"
  ⍤⤙≍ 0 Part₂ "aaa"
  ⍤⤙≍ 0 Part₂ "uurcxstgmygtbstg"
  ⍤⤙≍ 0 Part₂ "ieodomkazucvgmuy"
└─╴

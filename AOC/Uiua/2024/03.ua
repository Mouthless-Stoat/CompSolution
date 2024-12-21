Part₁ ← /+/×⍉ ⋕↘0_1 regex $ mul\((\d+),(\d+)\)
Part₂ ← Part₁▽⬚1\(↥₀↧₁+)+⊙¯∩⌕"do()","don't()".

┌─╴test
  $ xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
  .
  ⍤⤙≍ 161 Part₁
  ⍤⤙≍ 48 Part₂
└─╴

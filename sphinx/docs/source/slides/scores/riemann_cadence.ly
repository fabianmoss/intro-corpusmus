% add to all score examples
%%%%%%%%%%%%%%%%%%%%%%%%%%%
\version "2.18.2"
#(set-global-staff-size 20)
\paper {
  indent = 0\mm
  line-width = 110\mm
  oddHeaderMarkup = ""
  evenHeaderMarkup = ""
  oddFooterMarkup = ""
  evenFooterMarkup = ""
}

% remove footer
\header {
  tagline = ""
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%

% remove footer
\header {
  tagline = ""
}

\score {

\new Staff <<

  \new Voice = "first"
    \relative c'' { \voiceOne
        <e g c>4
        <ees aes c>4
        <e g c>4
        <e gis b>4
        <e g c>1
     }
  \new Voice = "second"
    \relative c' { \voiceTwo
      c4 aes c e c1
    }
>>

\layout {
   \context {
     \Score
     \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/16)
   }
 }

}

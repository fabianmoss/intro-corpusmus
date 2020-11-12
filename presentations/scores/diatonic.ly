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

\relative c' {
        \override Staff.TimeSignature.stencil = ##f
         aes1 \bar ""
         ees'1 \bar ""
         bes1 \bar ""
         f'1 \bar ""
         c1 \bar ""
         g'1 \bar ""
         d1 \bar ""
         a'1 \bar ""
         e1 \bar ""
       }

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
        <c g'>1 \bar ""
        <e b'> \bar ""
        <gis dis'> \bar ""
       }

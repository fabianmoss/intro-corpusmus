#!/bin/sh

cd scores
lilypond -fpdf -dbackend=eps  *.ly
rm *.eps
rm *.count
rm *.texi
rm *systems.tex

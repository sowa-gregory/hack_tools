Tool to crack pdf files protected with PESEL password.

PESEL is national identifier for Polish citizens issued by the polish government.
The identifier is widely adopted in communication with each government service and majority of public service providers.
Generally, polish people, memorizes their own PESELs.
From business point of view, PESEL seems to be perfect password to encrypt documents to email.
Only recipient knows it. It is not necessary to manage passwords. Finally, PESEL is quite complicated (11 digits) and not so easy to guess.
 
This repository contains all necessary scripts to build docker image, which allows to effectively crack any pdf file, encrypted with PESEL.
Average cracking time is around couple of minutes (using typical modern CPU). 
The speed is a result of limited set of guesses (algorithmically generated), which need to be tested to find correct password.
Candidates generator outputs only values, which conforms to PESEL identifier specification.

encrypt pdf
qpdf --encrypt userpasswd pesel 256 -- test_konto.pdf test_konto_enc.pdf

